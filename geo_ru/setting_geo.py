DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'db1',
        'USER':'geo_ru',
        'PASSWORD':'12345',
        'HOST':'localhost',
        'PORT':'',
    }
}
