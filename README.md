# CMS

TO RUN THIS PROJECT SUCCESSFULLY FOLLOW THIS STEPS


1) Download this repo in folder called CMS
2) In folder before the manage.py setup your virtual env
3) Activate your virtual env then install this following python libs into your virtual env
  asgiref==3.6.0
  Django==4.1.7
  django-filter==22.1
  djangorestframework==3.14.0
  importlib-metadata==6.1.0
  Markdown==3.4.1
  mysqlclient==2.1.1
  PyJWT==2.6.0
  pytz==2022.7.1
  sqlparse==0.4.3
  tzdata==2022.7
  zipp==3.15.0
4) create database called cms (if any other name then make respective changes)
5) Run following commands to migrate changes to database
  python manage.py makemigrations
  python manage.py migrate
  
SET UP IS DONE NOW YOU CAN RUN FOLLOWING COMMAND TO START YOUR SERVER
  python manage.py runserver

Following are the link for better navigation of the project:

For account management
http://127.0.0.1:8000/register
http://127.0.0.1:8000/login
http://127.0.0.1:8000/logout

For content management
http://127.0.0.1:8000/content/list
http://127.0.0.1:8000/content/detail/1
http://127.0.0.1:8000/content/detail/2 (Add form data to the raw forms and change method to put to update the content)
Same for deletion just change metod to delete with the same link


