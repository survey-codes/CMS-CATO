# CMS-CATO
Backend for the website of the SME Technology Group CATO.

### Directory Tree ###
TODO: Add rest of files and folders
```

├── main (Main application of the project, use it to add main templates, statics and root routes)
│   ├── fixtures
│   │   ├── dev.json (Useful dev fixtures, by default it creates an `admin` user with password `admin`)
│   │   └── initial.json (Initial fixture loaded on each startup of the project)
│   ├── migrations
│   ├── static (Add here the main statics of the app)
│   ├── templates (Add here the main templates of the app)
│   ├── admin.py
│   ├── apps.py
│   ├── models.py (Main models like City, Config)
│   ├── tests.py (We hope you will put some tests here :D)
│   └── views.py
├── media
├── projectCato
│   ├── settings
│   │   ├── partials
│   │   │   └── util.py (Useful functions to be used in settings)
│   │   ├── common.py (Common settings for different environments)
│   │   ├── development.py (Settings for the development environment)
│   │   └── production.py (Settings for production)
│   ├── urls.py
│   └── wsgi.py
├── scripts
│   ├── command-dev.sh (Commands executed after the development containers are ready)
│   ├── command-prod.sh (Commands executed after the build process are ready. Heroku magic!)
│   └── wait-for-it.sh (Dev script to wait for the database to be ready before starting the django app)
├── static
├── Dockerfile (Instructions to create the project image with docker)
├── Makefile (Useful commands)
├── Procfile (Dokku or Heroku file with startup command)
├── README.md (This file)
├── app.json (Dokku deployment configuration)
├── docker-compose.yml (Config to easily deploy the project in development with docker)
├── manage.py (Utility to run most django commands)
└── requirements.txt (Python dependencies to be installed)
└── test-requirements.txt (Python test dependencies to be installed)
```

### How to run the project ###

The project use docker, so just run:

```
docker-compose up
```

> If it's first time, the images will be created. Sometimes the project doesn't run at first time because
> the init of postgres, just run again `docker-compose up` and it will work.

### Tip ###

To remove the docker containers including database (Useful sometimes when dealing with migrations):

```
docker-compose down --volumes
```
 
And again run:

```
docker-compose up --build
```


*CMS-CATO app will run in url `localhost:8010`*

To recreate the docker images after dependencies changes run:

```
docker-compose up --build
```


### Accessing Administration

The django admin site of the CMS-CATO project can be accessed at `localhost:8010/admin`

By default the development configuration creates a superuser with the following credentials:

```
Username: admin
Password: admin
```

## Production Deployment: ##

The project is Heroku ready, this are the steps to deploy it in your dokku server:

```
Coming...
```

