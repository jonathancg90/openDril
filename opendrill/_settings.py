from os.path import join, dirname, realpath
import dj_database_url
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


ROOT_PATH = realpath(join(dirname(__file__), '..'))

SECRET_KEY = '##57y%+wx#h)0n^rdvi62$b36!gx5lqjf@wxp2k5#t&d6j3!vg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

PAGINATE_SIZE = 5

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.mail',
    'crispy_forms',
    'djcelery',
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

ROOT_URLCONF = 'opendrill.urls'

WSGI_APPLICATION = 'opendrill.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = '/static/'
STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MANDRILL_API_KEY = "PJInNsWGJMsrdyzcbdLtJA"
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

#celery

# import djcelery
# djcelery.setup_loader()
#
# BROKER_URL = 'redis://localhost:6379/0'
# CELERY_IMPORTS = ('apps.mail.tasks',)
# CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

try:
    import djcelery
    djcelery.setup_loader()

    BROKER_URL = 'redis://localhost:6379/0'

    CELERYD_LOG_COLOR = True ### turns the output colors to black.
    CELERY_IMPORTS = ('apps.mail.tasks') ### specify the route of the tasks file.
    CELERY_ALWAYS_EAGER = True ### True for development mode, so the process are executed locally.
    CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

    from local_settings import *

except ImportError:
    pass

try:
    import sys
    TESTING = 'test' == sys.argv[1]
except IndexError:
    TESTING = False