import os
from common import *

# Django settings for damncms project.

SITE_URL = 'http://localhost:8080'

STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
STATIC_URL = '/static/'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
	'default': {
		'ENGINE': 'django_mongodb_engine', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'damncms_dev',					# Or path to database file if using sqlite3.
		'USER': '',						# Not used with sqlite3.
		'PASSWORD': '',					# Not used with sqlite3.
		'HOST': 'localhost',			# Set to empty string for localhost. Not used with sqlite3.
		'PORT': 27017,					# Set to empty string for default. Not used with sqlite3.
	},
	'damncms_media': {
		'ENGINE': 'django_mongodb_engine', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'damncms_media_dev',					# Or path to database file if using sqlite3.
		'USER': '',						# Not used with sqlite3.
		'PASSWORD': '',					# Not used with sqlite3.
		'HOST': 'localhost',			# Set to empty string for localhost. Not used with sqlite3.
		'PORT': 27017,					# Set to empty string for default. Not used with sqlite3.
	}
}

SITE_ID = '4f11ffc0d64beac85a00001d'

# Make this unique, and don't share it with anybody.
SECRET_KEY = ')(SKEKD=d9fk32l)Wdflk43(z4(n7wz8)z8psr1p6uk@0twuebkc!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
# 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	# Uncomment the next line to enable the admin:
	'django.contrib.admin',
	# Uncomment the next line to enable admin documentation:
	# 'django.contrib.admindocs',
	'django_mongodb_engine',
	'djangotoolbox',
	'permission_backend_nonrel',
	'tastypie',
	'simpleapp',
)

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'verbose': {
			'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
		},
		'simple': {
			'format': '%(levelname)s %(message)s'
		},
	},
	'handlers': {
		'null': {
			'level':'DEBUG',
			'class':'django.utils.log.NullHandler',
		},
		'console':{
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',
			'formatter': 'simple'
		},
		'log_file':{
			'level': 'DEBUG',
			'class': 'logging.handlers.RotatingFileHandler',
			'filename': 'log/damn-cms/django.log',
			'maxBytes': '16777216', # 16megabytes
			'formatter': 'verbose'
		},
		'mail_admins': {
			'level': 'ERROR',
			'class': 'django.utils.log.AdminEmailHandler',
			'include_html': True,
		}
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
		'apps': { # I keep all my apps here, but you can also add them one by one
			'handlers': ['log_file'],
			'level': 'DEBUG',
			'propagate': True,
		},
	}
}
