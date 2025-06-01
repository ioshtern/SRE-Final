# shuup_tests/settings.py
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'shuup',
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:', 
    }
}
