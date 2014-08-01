__author__ = 'Travis'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wealthy',
    }
}
INTERNAL_IPS = ("127.0.0.1", "10.0.2.2")