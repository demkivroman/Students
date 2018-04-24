# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gowls7j_^qhpgl$+!il&m7h($jdkdhzlcf2zb@tr#6410t!m!s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['students.vitaliypodoba.com','demo-students.vitaliypodoba.com']

# website root urls
PORTAL_URL = 'http://students.vitaliypodoba.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER': 'students_db_user',
        'PASSWORD': 'NdOO746jyI',
        'NAME': 'students_db',
    }
}

# email settings
# please, set here your smtp server details and your admin email
ADMIN_EMAIL = 'demkivroman5@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '465'
EMAIL_HOST_USER = 'demkivroman5@gmail.com'
EMAIL_HOST_PASSWORD = 'demkivroman5'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# static files
STATIC_URL = '/static/'
STATIC_ROOT = '/path/to/folder/with/static/files/'

# media files
MEDIA_URL = '/media/'
MEDIA_ROOT = '/path/to/folder/with/media/files/'

# admins
ADMINS = (('Roman', 'demkivroman5@gmail.com'),)
MANAGERS = (('Manager','demkivroman5@gmail.com'),)











