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

BASEURL = 'https://decide-docker.herokuapp.com'

APIS = {
    'authentication': 'https://decide-docker.herokuapp.com',
    'base': 'https://decide-docker.herokuapp.com',
    'booth': 'https://decide-docker.herokuapp.com',
    'census': 'https://decide-docker.herokuapp.com',
    'mixnet': 'https://decide-docker.herokuapp.com',
    'postproc': 'https://decide-docker.herokuapp.com',
    'store': 'https://decide-docker.herokuapp.com',
    'visualizer': 'https://decide-docker.herokuapp.com',
    'voting': 'https://decide-docker.herokuapp.com',
}
