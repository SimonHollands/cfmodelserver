# Serve a Yolo Model for the CrowdFactor App [![CircleCI](https://circleci.com/gh/SimonHollands/cfmodelserver.svg?style=svg)](https://circleci.com/gh/SimonHollands/cfmodelserver)
![image](https://user-images.githubusercontent.com/22828446/68315875-52def480-006d-11ea-8f59-48ffc1b16ec0.png)

* [CrowdFactor Deployed on Heroku](https://crowdfactor.herokuapp.com/)
* [CrowdFactor Github](https://github.com/SimonHollands/crowdfactor3)


## Useage
```
The model looks for an image here to make the next prediction:
S3:/data/{surfbreak}/frame_last.jpg

Predicted images with bounding boxed are saved here: 
S3:/data/{surfbreak}/pred.jpg

So the api can now work for any break, as long as the data is in the correct place on the other end
```

## Setting up an EC2 Instance to serve the model
```
Step 1: https://us-west-1.console.aws.amazon.com/ec2/
Step 2: Launch Instance
Step 3: Search in AWS Marketplace for Deep Learning AMI (I have been using the linux ones)
Step 4: Select, checkout the pricing then continue.
Step 5: Choose an instance (m5.large works), Next configure instance details
step 6: "Configuration Instance": Under IAM role: select full_s3_access (note I created this role in my IAM user)
step 7: "Configuration Security Groups": Add rule, choose HTTP
Step 8: Review and launch (may have to make new keys)
```

## Launching Server on EC2 Instance
```
Step 1: Go to EC2 page, connect, copy paste SSH into terminal to connect to instance. (Do it from the directory where the keys are)
$ git clone https://github.com/SimonHollands/cfmodelserver
$ cd cfmodelserver
$ sudo pip3 install -r requirements.txt
$ screen python3 api.py
```
press control a, then cnt d to detach screen (allows it to keep running after terminal dies)

## Access API Endpoint
```
Find your EC2 instance Public IP
```

