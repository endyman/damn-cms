DAMN CMS - Django (restful) Api using MongoDB and Nginx
=======================================================

There are almost no projects without demand for a backend to provide and manage data.
Often this backend is only providing collections of simple data models.

Specially if you have to deal with Mobile application or web projects an easy to setup backend can save a life.

The idea of damn cms is to provide you with a sample implementation of all the building blocks.
Everything was already there but it took quite a while to make all the components play nice.

The Core of the CMS is Django-nonrel - a django fork supporting non-relational databases.
MongoDB is used as a database using the Django MongoDB Engine backend. MongoDB is solid NoSQL Database with lots of useful feature like GridFS, Geo Indexes and Map Reduce. The key feature of MongoDB is GridFS here as it can be used as the Django Storage Engine, too. By using GridFS we have a scalable HighPerfomant Distributed Filesystem to store our binary data without the need to care about replication across multiple instances. While we can also build Websites with this setup the main focus is an API so I decided to go with Tastypie after evaluation various options. With Tastypie you can easily expose your models by building REST Resources. Tastypie already includes Serializers for JSON, XML and Binary Plist out of the box.

With this software stack we have:

- a scalable CMS system on top of MongoDB
- an easy to use admin interface to edit data of our models
- a powerful an flexible REST Api supporting XML,JSON, PLIST
- Optional Resource Level Authorization and Authentication including User Account and API Keys
- Support for binary Data Field in our models which link to data stored in GridFS
- the system can be used to host several different API's concurrently
- and we can do everything else you can do with Django included :-)

For production I already included configs for uWSGI and NginX as well as for the NginX GridFS module. With this setup you can easily serve thousands of requests and extend capacity on demand as the system already is build to scale across multiple servers.
 


Pre-requisits
-------------

**OSX:**  

[Mercurial 2.0.2 for OS X 10.7](http://mercurial.berkwood.com/binaries/Mercurial-2.0.2-py2.7-macosx10.7.zip)

[git-1.7.8.3-intel-universal-snow-leopard.dmg](http://code.google.com/p/git-osx-installer/downloads/detail?name=git-1.7.8.3-intel-universal-snow-leopard.dmg&can=3&q=)

[MongoDB 2.0.2 OSX 64bit](http://fastdl.mongodb.org/osx/mongodb-osx-x86_64-2.0.2.tgz)


**Debian**
TODO: add debian dependencies

Installation Requirements:
--------------------------

Setup a new virtual Environment for the project:

    $ sudo easy_install virtualenv
	$ virtualenv damn-cms
	$ cd damn-cms
	
Next activate the environment:	

    $ . /bin/activate
	(damn-cms)$
	
run the pip installer to install required packages:

	(damn-cms)$ pip install -r PROJECT_ROOT/REQUIREMENTS.txt
	...
	Successfully installed pymongo Django djangotoolbox django-mongodb-engine permission-backend-nonrel tastypie mimeparse python-dateutil lxml PyYAML biplist path
	Cleaning up...
	(damn-cms)$
	
clone the damn-cms into PROJECT_ROOT:
    
    (damn-cms)$ git clone https://github.com/..... PROJECT_ROOT
	
alternatively un-tar dman-cms into PROJECT_ROOT:

    (damn-cms)$ mkdir PROJECT_ROOT && cd PROJECT_ROOT
    (damn-cms)$ tar -xvzf damn-cms.tar.gz

Starting in development mode:
-----------------------------

**Start mongoDB:**

	(damn-cms)$ sudo mongod &

**Initalize the database and set admin user:**

	(damn-cms)$ cd PROJECT_ROOT && ./manage.py syncdb
	
**Collect static files (required for django admin):**

	(damn-cms)PROJECT_ROOT$ ./manage.py collectstatic
	
**Set the siteid**

    (damn-cms)PROJECT_ROOT$ ./manage.py tellsiteid
   

Copy this id and set SITE_ID in settings/development.py to it   

**Start django dev server:**

	(damn-cms)PROJECT_ROOT$ ./ manage.py runserver 0.0.0.0:8080
	
	
	
You should now be able to access the admin interface and login [here](http://localhost:8080/admin/)


TODO: documentation on production setup
	



