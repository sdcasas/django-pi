System PI
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

    $ git clone https://github.com/sdcasas/django-pi

Create and activate the virtual environment: ::

    $ cd projects/
    $ mkvirtualenv pi
    $ workon pi

Install the requirements: ::

    (pi)$ sudo apt-get install libxml2-dev libxslt-dev libjpeg-dev
    (pi)$ pip install -r deploy/requirements.txt

Create the database and the database user, install the PostGIS extensions: ::

    $ sudo -u postgres psql
    postgres=# CREATE ROLE pi LOGIN PASSWORD 'pi-123qwe' NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
    postgres=# CREATE DATABASE pi WITH OWNER = pi;
    postgres=# \connect pi
    


You have to create your own pi_project/config/settings_local.py with your local database credentials: ::

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'pi',
            'USER': 'pi',
            'PASSWORD': 'pi-123qwe',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }


Restore Database: ::

    pg_restore -p 5432 --no-owner --role=pi -d name_database filename.backup

Initialize the database and set-up the Django environment: ::

    (pi)$ cd pi_project/
    (pi)$ ./manage.py collectstatic 
    (pi)$ ./manage.py makemigrations 
    (pi)$ ./manage.py migrate 
