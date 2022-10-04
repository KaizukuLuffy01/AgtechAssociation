# AgtechAssociation


## Installation
2 ways to install this project are as described below:
- Using Docker
- Orthodox Development Base

### Docker Installation
#### Prerequisites:
- Docker

Git clone the project:
```
$ git clone https://github.com/umairnsr87/AgtechAssociation.git
```

Now change the database configurations according to your system database:

#### find and change the values in AgtechAssociation/settings.py 

##### From 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

##### To
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "name of database",
        'USER': "username in postgres",
        'PASSWORD': "password of the above user",
        'HOST': "localhost",
        'PORT': 5432,
    }
}
```


### - For Docker development
### Run the following commands:
```
$ docker build .
$ docker run -p 8000:8000 <container_id>
```

This will start up your containers with above images and you will be able to use the application on
 http://0.0.0.0:8000/

### Orthodox Installation

# yet to be completed 