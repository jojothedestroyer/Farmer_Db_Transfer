"""
Django settings for GCNA_db project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURIT7Y WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t97pv)5u0g@zz5jqmx_=t+i#u$f1n=_40ivty73x+57o71h8*z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ["192.168.42.50","127.0.0.1",'192.168.1.198','192.168.1.51','192.168.1.161:8000','.vercel.app', '192.168.1.30']
ALLOWED_HOSTS = ['*']
# APP_NAME = os.environ.get("FLY_APP_NAME")
# ALLOWED_HOSTS = [f"{APP_NAME}.fly.dev"]


CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# Application definition


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gcna_data',
    'import_export',
    'formtools',
    'chartjs',
    'crispy_forms',
    'pwa',
    'celery',
    'matplotlib',
    'reportlab',
    'corsheaders',    
    'calculation',


    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'GCNA_db.urls'
CORS_ALLOW_ALL_ORIGINS = True

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

WSGI_APPLICATION = 'GCNA_db.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join('/data', 'db.sqlite3'),  
#     }
# }
# DATABASES = {
#     "default": env.dj_db_url("DATABASE_URL", default="sqlite:///db.sqlite3"),
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/js','serviceworker.js')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), 
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False  # Note: SSL is deprecated, use TLS instead

EMAIL_HOST_USER = 'reportmail121@gmail.com'  # Enter your Gmail email address
# EMAIL_HOST_PASSWORD = 'gmailpassword456'     # Enter your Gmail password or an App Password
EMAIL_HOST_PASSWORD = 'ndlz emqt oabo twpu'     # Enter your Gmail password or an App Password





PWA_APP_NAME = 'GCNA'
PWA_APP_DESCRIPTION = "Form storage and organization system."
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/images/images.png',
        'sizes': '160x160'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/images/images.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/images/images.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'
PWA_APP_SHORTCUTS = [
    {
        'name': 'Shortcut',
        'url': '/target',
        'description': 'Shortcut to a page in my application'
    }
]
PWA_APP_SCREENSHOTS = [
    {
      'src': '/static/images/images.png',
      'sizes': '750x1334',
      "type": "image/png"
    }
]


















# FlyV1 fm2_lJPECAAAAAAAArwHxBCbSN/CiKrUBmTtVo7bUT0JwrVodHRwczovL2FwaS5mbHkuaW8vdjGYAJLOAAu0rh8Lk7lodHRwczovL2FwaS5mbHkuaW8vYWFhL3YxxDyCC7Qars9pCatWv6U5ozygJKi+6F/HVWvLWIcjKZJANxCpCiTlosWxOKIbpwyiIE/qs1HBsE6FXLXTJozETleBK4QJ8V/t0sXgHRaejTKQCHrU+z9SkrfwEU8xGzOsBv2sYGzRk6yy8BoG0s/0GoojQONovu+Ss8rWK78++eKfFi3tZDn5GUrCw6V2uxCRgaZkamFuZ28DBZGBrGxpdGVmcy1jbG91ZAPEIIBLex0uEJEZ7DzOUgzvZacc07Xic1BLZyD33nab1zSk,fm2_lJPETleBK4QJ8V/t0sXgHRaejTKQCHrU+z9SkrfwEU8xGzOsBv2sYGzRk6yy8BoG0s/0GoojQONovu+Ss8rWK78++eKfFi3tZDn5GUrCw6V2u8QQRuKt7SuieZg1s7Tw00wPhMO5aHR0cHM6Ly9hcGkuZmx5LmlvL2FhYS92MZYEks5mdHc3zwAAAAEibJVVCpHOAAtjawzEENXI9UA/WoDfoCTvdk8ShfbEILPplRPD4gZ9R/JZh+mvijuuH61HLZHe8ucJMci7fbNb









