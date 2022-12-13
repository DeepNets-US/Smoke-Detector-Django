# Smoke-Detector-Django

This is a Web Deployment of the Smoke Detector, a Dense Neural Network Model. The model had an Training Accuracy of 99.98%, a Validation Accuracy of 99.97%, and Testing Accuracy of 0.9996%. 

This is also available on Kaggle : 
https://www.kaggle.com/code/utkarshsaxenadn/smoke-detection-dense-network-acc-99-98#Dense-Neural-Network

---
Download the folder in Zip format, unzip it and open the command prompt. Make sure that you have Django installed.
After opening the command prompt, run the below command:

```
python ./manage.py runserver
```

In case of any error, first run: 


```
python ./manage.py migrate
```

Then run :

```
python ./manage.py runserver
```

Imports Required : 
Make sure that you have downloaded the following modules : 

1. Django
2. Numpy
3. Sklearn
4. Keras
5. Tensorflow

If these modules are not installed you may get the respective errors,

Django : The backend will not run and you will not get the port link.

Numpy & Sklearn : The preprocessing will not take place. 

Tensorflow & Keras : This is used for loading the model, so without this model will not exist.

Hope You enjoyed. 
