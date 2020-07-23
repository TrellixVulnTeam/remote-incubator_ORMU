# remote-incubator

## Table of contents
* [Overview](#overview)
* [Technical Aspect](#technical-aspect)
* [System Settings](#system-settings)
* [Installation](#installation)
* [Run](#run)
* [Technologies Used](#technologies-used)
* [Bug Reques](#bug-request)
* [Credits](#credits)

## Overview/Technical Aspects
This is backend API for the project <b>"Remote Incubator"</b> (a commercial e-tutorial) for a company named "Fame Technologies pvt. ltd." situated at Bangalore from where I have done my four months internship/training.
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
     2. INTALL MYSQL, IF YOU DON'T HAVE BEFORE.
