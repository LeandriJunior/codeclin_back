"""
Django settings for CodeClin project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker
import sqlalchemy as db
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d+h@b8udkb&(&3l0i=d8@_txf!5d**=zju+5pb@n&9excljle5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '*',  ".vercel.app", ".now.sh"]
CORS_ALLOW_CREDENTIALS = True


# Application definition

SHARED_APPS = (
    'django_tenants',
    'corsheaders',
    'rest_framework',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'core',

)

TENANT_APPS = (
    'clinica',
    'clinica.agenda',
    'core.user',
    'core.funcionario',
    'core.filial',
    'core.cliente'
)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = 'CodeClin.urls'

MIDDLEWARE = [
    'core.middleware.GlobalRequestMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

WSGI_APPLICATION = 'CodeClin.wsgi.application'

AUTH_USER_MODEL = 'user.User'
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        # Engine do django tenants
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': os.getenv('DATABASE_NAME', 'postgres'),
        'USER': os.getenv('DATABASE_USER', 'postgres.dvfwiijmcasfwbyopsbi'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', '9AW6bRAbyQf13R7H'),
        'HOST': os.getenv('DATABASE_HOST', 'aws-0-sa-east-1.pooler.supabase.com'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
        'OPTIONS': {'application_name': 'CodeClin - Core'},
    }
}

DB_CONNECTIONS = {
    'default': {
        'user': DATABASES['default']['USER'],
        'password': DATABASES['default']['PASSWORD'],
        'host': DATABASES['default']['HOST'],
        'port': DATABASES['default']['PORT'],
        'name': DATABASES['default']['NAME'],
        'url': f"postgresql+psycopg2://"
        f"{DATABASES['default']['USER']}:"
        f"{DATABASES['default']['PASSWORD']}@"
        f"{DATABASES['default']['HOST']}/"
        f"{DATABASES['default']['NAME']}?client_encoding=latin1",
    }
}


DB_CONNECTIONS['default']['engine'] = db.create_engine(
    DB_CONNECTIONS['default']['url'],
    pool_size=10,
    max_overflow=0,
    # https://docs.sqlalchemy.org/en/20/core/pooling.html#dealing-with-disconnects
    pool_pre_ping=True
    # DESCONMENTE SE QUISER VER AS QUERYS EXECUTADAS
    # ,
    # echo_pool="debug",
    # echo=True,
    ,
    pool_timeout=30,
)
# ABRE O POOL DE CONEXAO
with DB_CONNECTIONS['default']['engine'].connect() as conn:
    conn.execute(db.text('select 1'))

DB_CONNECTIONS['default']['conexao'] = None

DB_CONNECTIONS['default']['sessoes'] = scoped_session(sessionmaker(bind=DB_CONNECTIONS['default']['engine']))

BUCKET_NAME = os.getenv('BUCKET_NAME', '')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR],
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

DATABASE_ROUTERS = ('django_tenants.routers.TenantSyncRouter',)
# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.sep.join([os.path.dirname(os.path.dirname(__file__)), 'media', 'temp'])
MEDIA_URL = '/media/temp/'


TENANT_MODEL = "core.Conta"

TENANT_DOMAIN_MODEL = "core.Dominio"

