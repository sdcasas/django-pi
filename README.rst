Sistemas Cámara de Senadores
=====================================


Descripcion
===========


Requirements
============

Before you can run this project, the following packages need to be installed:

Debian 8+
---------

* python-dev
* postgresql
* postgresql-server-dev-all
* python-virtualenv
* libevent-dev
* postgis
* postgresql-x.x-postgis-scripts


Instalación
===========

Clone the repository: ::

    $ git clone https://bitbucket.org/sdcasas/senado.git

Create and activate the virtual environment: ::

    $ cd projects/
    $ mkvirtualenv senado
    $ workon senado

Install the requirements: ::

    (senado)$ sudo apt-get install libxml2-dev libxslt-dev libjpeg-dev
    (senado)$ pip install -r deploy/requirements.txt

Create the database and the database user, install the PostGIS extensions: ::

    $ sudo -u postgres psql
    postgres=# CREATE ROLE senado LOGIN PASSWORD 'senado-123qwe' NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
    postgres=# CREATE DATABASE senado WITH OWNER = senado;
    postgres=# \connect senado
    


You have to create your own senado_project/config/settings_local.py with your local database credentials: ::

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'senado',
            'USER': 'senado',
            'PASSWORD': 'senado-123qwe',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }


Restore Database: ::

    pg_restore -p 5432 --no-owner --role=senado -d name_database filename.backup

Initialize the database and set-up the Django environment: ::

    (senado)$ cd senado_project/
    (senado)$ ./manage.py collectstatic 
    (senado)$ ./manage.py makemigrations 
    (senado)$ ./manage.py migrate 
