"""
Django settings for pybursa project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k)y(g1he0#8l1u-ondz^ez8tyvlpymvku5oevvogs4+v3ow)10'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

TEMPLATE_DEBUG = True

#ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'quadratic',
    'courses',
    'students',
    'coaches',
    'feedback',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pybursa.urls'

WSGI_APPLICATION = 'pybursa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), '/static/',)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates'), 'quadratic/templates']

ADMINS = (('admin', 'sashappyth@gmail.com'), )

EMAIL_HOST = 'localhost'

EMAIL_PORT = 1025
#EMAIL_HOST_USER = 'admin'
#EMAIL_HOST_PASSWORD = 'admin'

LOGGING = {
    'version': 1,
    'loggers': 
        {
            'courses': {
                'handlers': ['console', 'file_courses'],
                'level': 'DEBUG',
                },
            'students': {
                'handlers': ['console', 'file_students'],
                'level': 'DEBUG',
                },
        },
    'handlers':
        {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
                },
            'file_courses': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(BASE_DIR, 'logs', 'courses.log'),
                'formatter': 'simple',
                },
            'file_students': {
                'level': 'WARNING',
                'class': 'logging.FileHandler',
                'filename': os.path.join(BASE_DIR, 'logs', 'students.log'),
                'formatter': 'verbose',
                },
        },
    'formatters':
        {
            'verbose': {
                 'format': '%(levelname)s %(asctime)s \nModule: %(module)s \nFunction: %(funcName)s \nMessage: %(message)s\n\n'
                },
            'simple': {
                'format': '%(levelname)s %(message)s'
                },
        },
    }
