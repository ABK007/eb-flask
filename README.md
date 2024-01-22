**Introduction:**
This repository is for simlple app containing signup form. The purpose of this app is to learn deployment of Flask web app on AWS using Elastic Beanstalk and database integration using AWS service DynamoDB (NoSQL).

**Elastic Beanstalk Deployment Issues**

**Problem 1:**
The main issue in deploying the app was conflict in dependencies for AWS.
The three main libraries that are conflicting were:
1. awscli
2. awsebcli
3. boto3

**Reason:**
These libraries use botocore for for their functions and each library need different version of the
botocore to work.

**Solution:**
I have searched the internet to find the compatible versions of these libraries.
Following are the versions that are compatible with each other:
1. awscli==1.16.9
2. awsebcli==3.14.5
3. boto3==1.8.9



**Problem 2:**
The problem was that pywin32==306, pywin32-ctypes==0.2.2 are used for pythhon in windows but not for linux. Our AWS environment is linux and python 3.11.

**Solution:**
Remove the pywin==306 from requirements.txt and replace it with pypiwin32==223.



**Problem 3:**
Installed the latest version of python 3.12 which introduced new updates while removing old packages on which the existing dependencies require to work properly. In short, other dependencies were not updated yet with the latest python version.

**Solution:**
Always install older version of the python by at least one version from the latest i-e 3.11 instead of 3.12
This also applies to other libraries and python packages.



**Problem 4:**
Whenever you see the following error it means that there is a compatibility issue between one of the python dependencies in the requirement.txt:

Getting requirements to build wheel ... error
  error: subprocess-exited-with-error

  × Getting requirements to build wheel did not run successfully.
  │ exit code: 1
  ╰─> [54 lines of output]
      running egg_info
      writing lib3\PyYAML.egg-info\PKG-INFO
      writing dependency_links to lib3\PyYAML.egg-info\dependency_links.txt
      writing top-level names to lib3\PyYAML.egg-info\top_level.txt


  note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

× Getting requirements to build wheel did not run successfully.
│ exit code: 1
╰─> See above for output.

note: This error originates from a subprocess, and is likely not a problem with pip.

**Solution:**
Try to install different versions especially the later versions then the existing you are trying to install.



**Problem 5:**
Requirements.txt added windows related dependencies pywin and pypiwin because of the windows operating system which are now giving error while compiling in the linux operating system of the ec2 instance.

**Solution:**
Remove theses dependencies and other which are not compatible with server operating system from the requirements.txt file and then deploy the app.
