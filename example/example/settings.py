"""
Django settings for example project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-zta41a7+#1v=uv30j%9dxtbfh9*#=dt6l(m9$ce8p20p_=n@s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'thorbanks',

    'shop',

    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'example.urls'

WSGI_APPLICATION = 'example.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
]


# Bank links
BANKLINKS = {
    'swedbank': {
        'PRINTABLE_NAME': 'Swedbank',
        'REQUEST_URL': 'https://pangalink.net/banklink/swedbank',
        'SND_ID': 'uid513131',
        'PRIVATE_KEY': os.path.join(BASE_DIR, 'certs', 'swed_key.pem'),
        'PUBLIC_KEY': os.path.join(BASE_DIR, 'certs', 'swed_cert.pem'),
        'TYPE': 'banklink',
        'IMAGE_PATH': 'swedbank.png',
        'ORDER': 1,
    },
    'seb': {
        'PRINTABLE_NAME': 'SEB',
        'REQUEST_URL': 'https://pangalink.net/banklink/seb',
        'SND_ID': 'uid513157',
        'PRIVATE_KEY': os.path.join(BASE_DIR, 'certs', 'seb_key.pem'),
        'PUBLIC_KEY': os.path.join(BASE_DIR, 'certs', 'seb_cert.pem'),
        'DIGEST_COUNTS_BYTES': True,
        'TYPE': 'banklink',
        'IMAGE_PATH': 'seb.png',
        'ORDER': 2,
    },
    'danske': {
        'PRINTABLE_NAME': 'Danske Bank',
        'REQUEST_URL': 'https://pangalink.net/banklink/sampo',
        'SND_ID': 'uid513160',
        'PRIVATE_KEY': os.path.join(BASE_DIR, 'certs', 'danske_key.pem'),
        'PUBLIC_KEY': os.path.join(BASE_DIR, 'certs', 'danske_cert.pem'),
        'ENCODING': 'ISO-8859-1',
        'TYPE': 'banklink',
        'IMAGE_PATH': 'danske.png',
        'ORDER': 3,
    },
}
# Here you can customize where the bank logos are (used by the PaymentFormMixin). This is relative to STATIC_URL and
#  must end with slash
# BANKLINK_LOGO_PATH