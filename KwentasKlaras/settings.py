"""
Django settings for KwentasKlaras project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
import mimetypes
mimetypes.add_type("text/css", ".css", True)
PORT = os.getenv("PORT", "10000")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SESSION_ENGINE = "django.contrib.sessions.backends.db"  # Store sessions in the DB
SESSION_COOKIE_AGE = 1209600  # 2 weeks (should match login expiry)
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Prevents auto logout on browser close


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!#rx%wi3#35boq)q&9e9me)&83*bwvy(@t9q1*t293-@_sh%-g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['kwentas-kla.onrender.com', 'KwentasKlarasPMIS.pythonanywhere.com', '127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'unfold',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'KwentasApp',
    'django.contrib.humanize',
    'easyaudit',
    'maintenance_mode',
    'tailwind',
    'theme',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'easyaudit.middleware.easyaudit.EasyAuditMiddleware',
    'maintenance_mode.middleware.MaintenanceModeMiddleware'
]

ROOT_URLCONF = 'KwentasKlaras.urls'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'KwentasKlaras.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = [
       BASE_DIR / 'KwentasApp' / 'static',
]

# The directory where collectstatic will gather all static files.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')




# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'

AUTH_USER_MODEL = 'KwentasApp.CustomUser'

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 1209600

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
# Make sure the HttpOnly flag is set for the session cookie
SESSION_COOKIE_HTTPONLY = True

# Make sure the HttpOnly flag is set for the CSRF cookie
CSRF_COOKIE_HTTPONLY = True



LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.template': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'kwentasklarasboljoon@gmail.com'
EMAIL_HOST_PASSWORD = 'hvab euhu zpvu syvg'

# Enable all events for auditing
DJANGO_EASY_AUDIT_WATCH_LOGIN_EVENTS = True  # For login/logout events
DJANGO_EASY_AUDIT_WATCH_CRUD_EVENTS = True  # For Create/Update/Delete events

# To record IP addresses for login events
DJANGO_EASY_AUDIT_REMOTE_IP_ADDRESS_FIELD = 'REMOTE_ADDR'

# Exclude specific models (e.g., login/registration) from CRUD auditing
DJANGO_EASY_AUDIT_EXCLUDED_MODELS = ['auth.User']  # Exclude User model to avoid login/register CRUD tracking
# Enable request event tracking
DJANGO_EASY_AUDIT_WATCH_REQUEST_EVENTS = True
# Example: Exclude requests to static files and Django admin
DJANGO_EASY_AUDIT_EXCLUDE_REQUESTS = [
    r'^/static/',
    r'^/admin/',
]

MAINTENANCE_MODE = False
MAINTENANCE_MODE_TEMPLATE = "maintainance.html"  # Fix typo here: 'maintainance' -> 'maintenance'
MAINTENANCE_MODE_IGNORE_ADMIN_SITE = False
MAINTENANCE_MODE_STATE_FILE_PATH = "C:/Users/Hanz Archer/Desktop/KwentasKlaras/maintenance_mode_state.txt"

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"


















