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

**Day 1 Summary:** Project-Application-URL

\--------------------

**Day 2:**
by default -> no python template

1. **render templates:**

render(request,html\_file,{})

\#renders html page: takes 3 parameters: request object, html file from templates/, context/dynamic data(optional)

\#render dynamic content

Note: Django template renders from server so is SEO friendly

\#if multiple folder: use path-> folder/file.html

\#templates folder is taken as root folder by default in Django

\#keys taken as variable in template -> call key {{ key }}

2\. **serial number use:**

{{ forloop.counter }} -> starts from 1

{{ forloop.counter0 }} -> starts from 0

**Layout Break**

\--------------------

**Day 3:**

1. **Makes file for modules, if run stored in db**

python manage.py makemigrations

2\. **stores in db -> table**

python manage.py migrate

3\. **Create user that is super user for Django admin panel**

python manage.py createsuperuser

4\. **Types of views in Django:** function based, classic based - object oriented, generic view

5\. **Handles python's images**

pip install Pillow

\--------------------

**Day 4:**

New Product Module

1. **defining meta data ->** class Meta:
2. **ModelForm ->**  it is a class, present attributes in form directly, by default inherits Form class
3. **makes the form elements in <p>** **->** category\_form.as\_p in html
4. **generates token, in backend Django check it for no SQLinjection->** {% csrf\_token %}

\--------------------

**Day 5:**

**Product form ->** CRUD operation

