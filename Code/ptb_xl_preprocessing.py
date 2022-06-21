import os
import pandas as pd
import numpy as np
import datetime as datetime
import wfdb
import ast

def load_raw_data(df, sampling_rate, path):
		if sampling_rate == 100 :
				data = [wfdb.rdsamp(path+f) for f in df.filename_lr]
		else:
				data = [wfdb.rdsamp(path+f) for f in df.filename_hr]
		data = np.array([signal for signal, meta in data])
		return data

path = '/home/ubuntu/dr-you-ecg-20220420_mount/ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.1/'
sampling_rate = 500

# Load and convert annotation data
df_Y = pd.read_csv(path + 'ptbxl_database.csv', index_col = 'ecg_id')
df_Y.scp_codes = df_Y.scp_codes.apply(lambda x: ast.literal_eval(x))

# Load raw signal data
X = load_raw_data(df_Y, sampling_rate, path)

# Load scp_statements.csv for diagnostic aggregation
agg_df = pd.read_csv(path + 'scp_statements.csv', index_col = 0)
agg_df = agg_df[agg_df.diagnostic == 1]

def aggregate_diagnostic(y_dic):
		tmp = []
		for key in y_dic.keys():
				if key in agg_df.index:
						tmp.append(agg_df.loc[key].diagnostic_class)
		return list(set(tmp))

# Apply diagnostic superclass
df_Y['diagnostic_superclass'] = df_Y.scp_codes.apply(aggregate_diagnostic)

# x dataset - padding and edit
X_dataset = []
for i in X:
    df_ecg = pd.DataFrame(i)
    nm = df_ecg[[0, 1, 6, 7, 8, 9, 10, 11]]
    nm_numpy = nm.to_numpy()
    pad_ecg = np.pad(nm,((120,0),(0,0)),'constant',constant_values=0) # Lead zero padded to 5120
    X_dataset.append(pad_ecg)
    
X_dataset = np.array(x_testset)
