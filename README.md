# remote-incubator

## Table of contents
* [Overview and Technical Aspects](#overview-and-technical-aspects)
* [System Settings and Installation](#system-settings-and-installation)
* [Run](#run)
* [Technologies Used](#technologies-used)
* [Bug Request](#bug-request)


## Overview ad Technical Aspects
This is backend API for the project <b>"Remote Incubator"</b> (a commercial e-tutorial) was being developed by a company named <b>"Fame Technologies pvt. ltd."</b> situated at Bangalore where I had been selected to work in this project as to develop the Backend API for the project in my four months internship/training period.
This Api consists endpoints for the followings:- 
  1. HTTP Services/requests (GET, POST, PUT, DELETE) for a user's login, registration logics i.e Registration table, login table, Address table, etc.
  2. HTTP Services/requests for Admin side like managing documents/video, give access to the paid user, etc.
  3. Payment Gateway
  4. Autogerated mailing System
  
## System Settings/Installation
  If you don't have python3 install on your system the do the following steps:- </br>
  #### For Linux  or macOS users:
     `$ sudo apt-get install python3 `
    
  Then You need to install pip so that you can download depedencies for the project. </br>
     ```
      $ sudo apt-get install python3-pip 
     ```
     </br>
      Then Install "vitualenv" python module so that you will have more than one python install side by side.Virtualenv is a tool used to create an isolated Python 
      environment. This environment has its own installation directories and environment. This doesn't share libraries with other environments.
      It is very helpful for the application required separate environments on the same server. </br>
      To install virtualenv module run the following command:- </br>
      ```
      $ pip3 install virtualenv
      ```
      </br>
      Run the following command to create virtual environment folder in the project's root directory. </br>
      `$ virtualenv venv`, where 'venv' is the name of your virtual environment for new python installed. </br>
      
Now you have to create some environment variables assigned your secret keys like database credential, your payment gateway credentials, etc. </br>
In ~/.barshrc file, you can add following variables at the bottom of the ~/.bashrc file which have been used in this project.
```
DB_USER="YOUR_DATABASE_USERNAME"
DB_PASSWORD="YOUR_DATABASE_PASSWORD"
EMAIL_ID="YOUR_GMAIL_ID"
EMAIL_PASS="YPUR_GMAIL_PASSWORD"
RAZOR_KEY="YOUR_RAZORPAY_APP_KEY"
RAZOR_SECRET_KEY="YOUR_RAZORPAY_SECRET_KEY"
export DB_USER
export DB_PASSWORD
export EMAIL_ID
export EMAIL_PASS
export RAZOR_KEY
export RAZOR_SECRET_KEY
```
<b>NOTE: </b> </br>
1. YOUR HAVE REGISTER IN [RAZORPAY](https://www.razorpay.com/) TO GET REQUIRED API KEYS.
2. INSTALL MYSQL AND CONFIGURE, IF YOU DON'T HAVE BEFORE.
     
  #### For Windows users:
  Since I am not a windows OS user, I can't the exact procedure to install and configure all above mentionded dependencies.
  1. Install python3 (Refer a good video or blog or official website documentation).
  2. Create a virtual environment for the python installed for the project.
  3. Create all above environment variables (Refer a video/blog on how to create environment variables in windows).
  #### YET IF YOU ARE HAVING PROBLEM RUNNING THE PROJECT ON WINDOWS JUST LET ME KNOW.
  <b>NOTE: </b> </br>
     1. YOUR HAVE REGISTER IN [RAZORPAY](https://www.razorpay.com/) TO GET REQUIRED API KEYS.
     2. INSTALL MYSQL AND CONFIGURE, IF YOU DON'T HAVE BEFORE.
     </br>
 Activate the virtual environment using following commmand- </br>
```
source PATH/bin/activate
```
where PATH is the absolute path of your virtual environment(venv).

## Run 
To install all python modules required for this project ensure that virtual env(venv) is activated and run the following command:- </br>
```
(venv) pip install -r requirements.txt
(venv) python run.py
```

## Technologies Used

![WhatsApp Image 2020-07-23 at 20 30 21](https://user-images.githubusercontent.com/42790586/88302454-7fce5700-cd23-11ea-974d-77e2da56acad.jpeg)

## Bug Request
If you find any bug or have any suggestion, feel free to let me know @ hbr8218@gmail.com
