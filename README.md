# PROPHECY-STEMI

## [Problem Definition]
![image](https://user-images.githubusercontent.com/97151697/171563811-d32765f4-b429-49be-944a-e53209ce917f.png)

build a deep learning algorithm to classify patients with STEMI or not, by using ECG and CNN 1d Model

- x = time-series data (ECG waveform)
- y = labels (STEMI or Not ; 0 or 1)
---

## [Data Preprocess]
(1) Setting
- AWS EC2 instance (type) : ecg_aws_jpt2 (g4dn.4xlarge)
- AWS S3 bucket : dr-you-ecg-20220420_mount

(2) Data Resource
 Data | source | train | test 
 ---|---|---|---|
KOMATE | Severance, Seoul (internal) | 11394 | 50
[PTB_XL](https://physionet.org/content/ptb-xl/1.0.1/) | open ECG data (external) | - | 21837

(3) Preprocessing Code
Code | preprocessing | make a label table | make datasets
---|---|---|---|
 [KOMATE](https://github.com/kyulee-jeon/PROPHECY-STEMI/blob/main/Code/Make%20label%20table%20and%20datasets%20of%20KOMATE.ipynb) | X (privacy) | O | O
 [PTB_XL](https://github.com/kyulee-jeon/PROPHECY-STEMI/blob/main/Code/Preprocess%2C%20Make%20label%20table%20and%20datasets%20of%20PTB_XL.ipynb) | O | O | O

waveform should have a numpy array shape (total count, 5120, 8)
- 5120 rows = 500 Hz * 10 seconds + 120 padding
- 8 columns = 8 leads (I, II, V1, V2, V3, V4, V5, V6)

---

## [Model build, train and test]
There are two models - (1) model from Attia, and (2) the simpler one.

### (1) [Model](https://github.com/kyulee-jeon/PROPHECY-STEMI/blob/main/Code/Model%20and%20Visualization.ipynb)

- Training 

Train data  |	Batch size | 	Epochs  |	Loss function  |	Class weight 
---|---|---|---|---|
11394 |	128 |	50  |	Categorical cross-entropy  |	{0:1, 1:10} 
  

- Test Result  

Test data | 	AUROC score  |	Loss  |	Accuracy  |	Sensitivity 
---|---|---|---|---|
50|	0.925|	0.5283|	0.90	|0.8
  
Confusion Matrix |	AUROC
---|---|
![image](https://user-images.githubusercontent.com/97151697/171569562-1c4b9ca0-1d5e-41cb-b2f4-97f95cc6d8a6.png) | ![image](https://user-images.githubusercontent.com/97151697/171569589-e71c8c22-c252-4d33-82cf-6dd72e512b60.png)


### (2) [simple Model and GradCam](https://github.com/kyulee-jeon/PROPHECY-STEMI/blob/main/Code/simple%20Model%20and%20Visualization.ipynb)

- Training 

Train data  |	Batch size | 	Epochs  |	Loss function  |	Class weight 
---|---|---|---|---|
11394 |	128 |	50  |	Categorical cross-entropy  |	{0:1, 1:10} 
  

- Test Result  

Test data | 	AUROC score  |	Loss  |	Accuracy  |	Sensitivity 
---|---|---|---|---|
50|	0.935|	0.5137|	0.90	|0.75

- Visualization (GradCam)
![TP_lead I](https://user-images.githubusercontent.com/97151697/171570893-135387c1-67ee-4228-9300-e04db44e596d.png)
![TP_lead II](https://user-images.githubusercontent.com/97151697/171570911-9e078dbd-ca37-4e43-8a69-9efbc773286c.png)
![TP_lead V1](https://user-images.githubusercontent.com/97151697/171570931-41909c80-6ead-463a-9994-6571367bf502.png)
![TP_lead V2](https://user-images.githubusercontent.com/97151697/171570945-fc61034a-bfb9-4ee5-b034-b872e8611326.png)
![TP_lead V3](https://user-images.githubusercontent.com/97151697/171570967-dc997356-68d2-44d5-863c-fe11a3e9e70a.png)
![TP_lead V4](https://user-images.githubusercontent.com/97151697/171570990-3421a922-ea50-445d-b862-3c7f0ce6de48.png)
![TP_lead V5](https://user-images.githubusercontent.com/97151697/171571013-b18916a0-b827-4265-add3-dcbf6a77e5f6.png)
![TP_lead V6](https://user-images.githubusercontent.com/97151697/171571034-c539476a-f3f5-4f75-ac0d-8b886e3fe03c.png)



---

(+) visualize the waveform of the data that algorithm tell us it's not STEMI but it was.
- [extract and show FN waveform](https://github.com/kyulee-jeon/PROPHECY-STEMI/blob/main/Code/extract%20and%20show%20FN%20waveform.ipynb)



