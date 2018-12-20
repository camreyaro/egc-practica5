DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

STATIC_ROOT = '/app/static/'
MEDIA_ROOT = '/app/static/media/'
ALLOWED_HOSTS = ['*']

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

BASEURL = 'http://localhost:$PORT'

APIS = {
    'authentication': 'http://localhost:$PORT',
    'base': 'http://localhost:$PORT',
    'booth': 'http://localhost:$PORT',
    'census': 'http://localhost:$PORT',
    'mixnet': 'http://localhost:$PORT',
    'postproc': 'http://localhost:$PORT',
    'store': 'http://localhost:$PORT',
    'visualizer': 'http://localhost:$PORT',
    'voting': 'http://localhost:$PORT',
}
