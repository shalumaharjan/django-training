# **Django**



**1. virtualenv**

**2. Django webframework: Web development**

* templates (UI/web pages)
* routing (URL)
* model (db -> tables)
* form
* static files (images/js/css/icons)
* media files (uploads = docs,images...)
* file system (settings.py, model.py, urls.py)
* Django admin (site manager, model customize, permission, group)
* Database (MySQL/PostgreSQL configuration)
* .env (dotenv or environ)
* Serializers (API)
* Email (verification)
* Authentication \& Authorization
* Bootstrap or tailwind

**3.** **Django RestFramework: Rest API development**

* Serializers
* JWT Authentication
* Postman (testing)
* React.js (api - integration)

&#x09;

Project Basis - Ecommerce App

(Extra : Elastic Search and Object Storage)

AWS S3 bucket (or minio or cloudflare R2 or garage)





## **Commands:**

1\. **Installing virtualenv in the project**

python -m venv env

\#here 'env' is the identifier for virtual environment. It can be named as any identifier.



2\. **Activate virtual environment**

\#for windows

env\\Scripts\\activate



\#for MAC and Linux

source \\env\\bin\\activate



3\. **Create a requirements.txt**

pip freeze > requirements.txt

\# it will list all the packages installed with version so that no need to install packages manually one by one when the project is shift or access from another directory or machine



4\. **Installing Django in the project root folder**

pip install Django



5\. **Check the installed packages**

pip freeze requirements.txt



6\. **Add packages to requirements.txt**

pip freeze > requirements.txt



7\. **Creating Django project**

django-admin startproject <project\_name>

for example:

django-admin startproject project\_ecommerce



8\. **Make application**

python manage.py startapp app\_ecomweb



9\. **Run the server**

python manage.py runserver



settings.py -> register

views.py -> functions

**Django works:** MVT(Model-db Views-business logic Template-UI)



Day 1 Summary: Project-Application-URL

