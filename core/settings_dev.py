from .settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DB_NAME"), 
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASS"),
        'HOST': os.getenv("DB_HOST"), 
        'PORT': os.getenv("DB_PORT"),
    }
}

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID") 
#print(AWS_ACCESS_KEY_ID)

AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY") 
#print(AWS_SECRET_ACCESS_KEY)
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME") 
#print(AWS_STORAGE_BUCKET_NAME)

AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME") 
#

STORAGES = {
    "default" : {
        "BACKEND":"storages.backends.s3.S3Storage",
        "OPTIONS":{
            "file_overwrite" : False,
        }
    },"staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },

}


