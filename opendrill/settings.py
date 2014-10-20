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

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mail',
    'crispy_forms',
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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

# STATICFILES_DIRS = (
#     join(ROOT_PATH, 'static'),
#     join(ROOT_PATH, 'media')
# )

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

# Parse database configuration from $DATABASE_URL
#import dj_database_url
#DATABASES['default'] = dj_database_url.config()


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/static/'
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )