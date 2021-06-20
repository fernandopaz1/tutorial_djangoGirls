"""
Django settings for blogDjango project.

Generated by 'django-admin startproject' using Django 2.2.24.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

import dj_database_url
import django_heroku
from django.core.management.utils import get_random_secret_key

import environ
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True


# Application definition

INSTALLED_APPS = [
    "blog.apps.BlogConfig", 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blogDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DEBUG = True
SECRET_KEY =  get_random_secret_key()
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABSE_URL')
    )
}

# # print(os.environ.get('.env'))
# if  os.environ.get('DEBUG'):
#     print("Debug is enabled.")
#     DEBUG = True
#     SECRET_KEY =  env.str('SECRET_KEY')
#     # When not specified, ALLOW_HOSTS defaults to:
#     ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']
#     DATABASES = {
#         'default': {
#             'ENGINE': env.str('DATABASE_ENGINE'),
#             'NAME': env.str('DATABASE_NAME'),
#             'USER': env.str('DATABASE_USER'),
#             'PASSWORD': env.str('DATABASE_PASSWORD'),
#             'HOST': env.str('DATABASE_HOST'),
#             'PORT': env.str('DATABASE_PORT'),
#             'TEST': {
#                 'NAME': env.str('TEST_DATABASE_NAME'),
#             },
#         }
#     }
# else:
#     DEBUG = False
#     SECRET_KEY =  get_random_secret_key()
#     print("Debug is disabled.")
#     ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': 'django_girls',
#             'USER': 'django',
#             'PASSWORD': 'django',
#             'HOST': '127.0.0.1',
#             'PORT': '5432',
#         }
#     }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
# Activate Django-Heroku.
django_heroku.settings(locals())

STATIC_FILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'