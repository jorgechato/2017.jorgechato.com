import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
        "*",
        "0.0.0.0",
        "localhost",
        ]

SITE_ID = 1

# Application definition
INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',

        'emoji',
        'import_export',
        'robots',
        'gunicorn',
        'ckeditor',
        'posts',
        'profiles',
        'me',
        ]

if DEBUG:
    INSTALLED_APPS += [
            'django_extensions',
            'autofixture',
            ]
    pass

MIDDLEWARE = [
        'django.middleware.gzip.GZipMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]

ROOT_URLCONF = 'chato.urls'

TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
                ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'profiles.context_processors.header',
                    ],
                },
            },
        ]

WSGI_APPLICATION = 'chato.wsgi.application'


# Password validation
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

# Ckeditor config
CKEDITOR_CONFIGS = {
        'default': {
            'skin': 'moono',
            'toolbar_OrggueToolbar': [
                {'name': 'document', 'items': ['Source', '-', 'Save',
                    'NewPage', 'Preview', 'Print', '-', 'Templates']},
                {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste',
                    'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
                {'name': 'links', 'items': ['Link', 'Unlink']},
                {'name': 'insert', 'items': ['Iframe', 'Image','Upload', 'Table',
                    'HorizontalRule', 'Smiley', 'SpecialChar']}, '/',
                {'name': 'basicstyles', 'items': [
                    'Bold', 'Italic', 'Underline', 'Strike',
                    'Subscript', 'Superscript', '-', 'RemoveFormat']},
                {'name': 'paragraph', 'items': [
                    'NumberedList', 'BulletedList', '-', 'Outdent',
                    'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                    'JustifyLeft', 'JustifyCenter', 'JustifyRight',
                    'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language']},
                {'name': 'colors', 'items': ['TextColor', 'BGColor']},
                {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
                {'name': 'styles', 'items': ['Styles', 'Format', 'FontSize']},
                ],
            'toolbar': 'OrggueToolbar',
            'tabSpaces': 4,
            'allowedContent': True,
            'extraPlugins': ','.join(
                [
                    'image2',
                    'iframe',
                    'div',
                    'autolink',
                    'autoembed',
                    'embedsemantic',
                    'autogrow',
                    'widget',
                    'lineutils',
                    'clipboard',
                    'dialog',
                    'dialogui',
                    'elementspath'
                    ]),
                }
        }
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = True
CKEDITOR_ALLOW_NONIMAGE_FILES = False


# Internationalization
LANGUAGE_CODE = 'es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'compass/out'),
        )

CKEDITOR_UPLOAD_PATH = "uploads/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

try:
    from chato.local_settings import *
except ImportError:
    from github import Github
    from instagram.client import InstagramAPI
    from os import environ

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = environ.get('SECRET_KEY')

    github_api = Github(environ.get('git_user'), environ.get('git_pass'))

    access_token = environ.get('access_token')
    client_secret = environ.get('client_secret')
    instagram_api = InstagramAPI(access_token=access_token, client_secret=client_secret)

    email = environ.get('email')

    # Database
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': environ.get('NAME'),
                'USER': environ.get('USER'),
                'PASSWORD': environ.get('PASSWORD'),
                'HOST': environ.get('HOST'),
                'PORT': environ.get('PORT'),
                }
            }
