"""
    Development Django settings for machina-demo demo project
    =========================================================

    This files imports the `base` settings and can add or modify previously defined settings to
    alter the configuration of the application for development purposes.

    For more information on this file, see https://docs.djangoproject.com/en/dev/topics/settings/
    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/dev/ref/settings/

"""

import socket

from captcha.constants import TEST_PRIVATE_KEY
from captcha.constants import TEST_PUBLIC_KEY

from .base import *  # noqa


# APP CONFIGURATION
# ------------------------------------------------------------------------------

INSTALLED_APPS += (  # noqa: F405
    'debug_toolbar',
)


# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------

MIDDLEWARE += (  # noqa: F405
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


# DEBUG CONFIGURATION
# ------------------------------------------------------------------------------

DEBUG = True


# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]
INTERNAL_IPS = ['127.0.0.1', ]
ADMINS = ()
MANAGERS = ()


# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------

TEMPLATES[0]['OPTIONS']['context_processors'] += (  # noqa: F405
    'demo_project.context_processors.webpack', )
TEMPLATES[0]['OPTIONS']['loaders'] = (  # noqa: F405
    # Disables cached loader if any
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------

STATICFILES_DIRS = (
    MACHINA_MAIN_STATIC_DIR,  # noqa: F405
    str(PROJECT_PATH / 'demo' / 'static' / 'build_dev'),  # noqa: F405
    str(PROJECT_PATH / 'demo' / 'static' / 'build'),  # noqa: F405
    str(PROJECT_PATH / 'demo' / 'static'),  # noqa: F405
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


# RECAPTCHA CONFIGURATION
# ------------------------------------------------------------------------------

RECAPTCHA_PUBLIC_KEY = TEST_PUBLIC_KEY
RECAPTCHA_PRIVATE_KEY = TEST_PRIVATE_KEY


# WEBPACK-DEV-SERVER CONFIGURATION
# ------------------------------------------------------------------------------

WEBPACK_DEV_SERVER_PORT = get_envsetting('WEBPACK_DEV_SERVER_PORT', 8080)  # noqa: F405
WEBPACK_DEV_SERVER_URL = 'http://localhost:{port}'.format(port=WEBPACK_DEV_SERVER_PORT)

# Dynamically set a boolean indicating if the webpack dev server is started.
webpack_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    webpack_sock.bind(('localhost', WEBPACK_DEV_SERVER_PORT))
    WEBPACK_DEV_SERVER_STARTED = False
except socket.error as e:
    WEBPACK_DEV_SERVER_STARTED = (e.errno == 98)
webpack_sock.close()


# ENV-SPECIFIC CONFIGURATION
# ------------------------------------------------------------------------------

try:
    # Allow the use of a settings module named "settings_env" that is not contributed to the
    # repository (only when dev settings are in use!).
    from .settings_env import *  # noqa
except ImportError:
    pass
