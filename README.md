Development Setup
=================

Install git, python2.7, virtualenvwrapper, python-pip, postgres using apt-get

For development:

Fetch the repository and set upstream

    git clone git@github.com:nishant8887/webapp-aproposdrive.git
    git remote add upstream ssh://567d174f89f5cffebf0001d6@webapp-aproposdrive.rhcloud.com/~/git/webapp.git/

Install postgres and change access method to "trust" in

    /etc/postgresql/<version>/main/pg_hba.conf

Make postgres settings as follows

    psql -U postgres

in postgres shell

    CREATE USER root;
    ALTER ROLE root WITH SUPERUSER;
    ALTER ROLE root WITH CREATEUSER;
    ALTER ROLE root WITH CREATEDB;
    ALTER ROLE root WITH REPLICATION;

List all users and check if root has all previleges

    \du

Exit postgres shell

    \q   

Get into your repo directory

    mkvirtualenv aproposdrive
    cd wsgi
    pip install -r requirements.txt

Create database and migrate initial schema

    createdb -U root root
    createdb -U root aproposdrive
    cd aproposdrive
    python manage.py migrate

Check if everyting is working fine

    python manage.py runserver

visit in browser

    http://localhost:8000

Make changes and then push the repo upstream

    git push origin master
    git push upstream master (to deploy)

Jenkins:
========

Jenkins deployed at url

    https://jenkins-aproposdrive.rhcloud.com/

SSH:
====

You can ssh to check on the instance

    ssh 567d174f89f5cffebf0001d6@webapp-aproposdrive.rhcloud.com

To create a superuser

    python $OPENSHIFT_REPO_DIR/wsgi/aproposdrive/manage.py createsuperuser

Website:
========

Visit website url at

    http://webapp-aproposdrive.rhcloud.com/
