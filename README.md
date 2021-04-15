# CMS-CATO

CATO technology group or CATO group, an IT company has a website made in WordPress.
The site provides contact information and the services that the company offers to its clients;
However, due to the recent demand in the last year, they decided to improve the portal,
thinking about building their own platform, one that has personalization approaches and
that allows them to manage their own content to guide their customers. With this,
the CATO group wishes to adopt this solution to different systems and have a greater
commercial impact.

For this application, the Django (Backend) and Angular (Frontend) web development frameworks
were used with agile development, since it allows adapting to changing environments, also, 
reducing risks and providing better integration between the work team and The client uses a
REST Architecture for communication, but supported by a query language such as GRAPHQL
instead of RESTful.

### Directory Tree ###
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

## Development ##

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

By default the development configuration creates a superuser with the following
credentials:

```
Username: admin
Password: admin
```

### Celery task monitoring

The project has a client for monitoring asynchronous tasks with Celery.
You can access to this monitor at `localhost:5555`

### GraphQL testing client

The project has a GraphQL testing client **[GraphiQL](https://github.com/graphql/graphiql)**.
Go to `localhost:8000/graphql` and type your first query!

## Production Deployment: ##

The project is Heroku ready with
**[Build Manifest](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml)**
deploy approach. You should follow those steps to deploy it as heroku app.
> Keep in mind Docker-based deployments are limited to the same constraints that Git-based
> deployments are. For example, persistent volumes are not supported since the file system
> is ephemeral and web processes only support HTTP(S) requests.

### Prerequisites 📋 ###

The production environment requires certain configuration before deploying the docker image,
such as the database, the AWS and the CELERY settings.

### Environment variables 🛠️ ###

The system is configured using environment variables. The following is the list of
environment variables that are required or optional before deploying the system:

| Variable | Description | Required | Default |
| :--- | :--- | :---: | :--- |
| `DJANGO_SECRET_KEY` | Key used by Django for tokens like CSRF and cookies, it can be any secret key but it's recommended to generate it using https://djecrety.ir/ | **yes** | *None* |
| `RABBITMQ_USER` | Custom username for the Rabbitmq broker | **yes** | *None* |
| `RABBITMQ_PASS` | Custom password for the Rabbitmq broker | **yes** | *None* |
| `ENVIRONMENT` | Project environment settings | **no** | *development* |
| `USE_S3` | Used to turn the S3 storage on | **no** | *True* |
| `AWS_ACCESS_KEY_ID` | Your Amazon Web Services access key, as a string | **yes** | *None* |
| `AWS_SECRET_KEY_ACCESS` | Your Amazon Web Services secret access key, as a string | **yes** | *None* |
| `AWS_STORAGE_BUCKET_NAME` | Your Amazon Web Services storage bucket name, as a string | **yes** | *catobucket* |
| `AWS_REGION` | Specifies the AWS Region to send the request to | **no** | *None* |

### Backing services ⚙️ ###

As expected in a Twelve Factors App the following services needs to be configured
using environment variables as well:

| Service | Environment variable | Value | Example |
| :--- | :---: | :--- | :--- |
| Postgres Database | `DATABASE_URL` | `postgresql://<user>:<pass>@<host>:<port>/<dbname>` | `postgres://dlfgyvooqebjiq:7f5a5bfbedf60019262c16dbfa78ea1558e48f7977cb8bc91de670ff0aeeeb02@ec2-18-233-83-165.compute-1.amazonaws.com:5432/d88kfm43j69i0s` |

### Deployment ☁ ###

When having all the prerequisites and you have logged in with your Heroku client, 
clone the repository in the server, then deploy the containers with the commands:

```
heroku update beta
heroku plugins:install @heroku-cli/plugin-manifest
```

> You can switch back to the stable update stream and remove the plugin at any time with:
> ``` heroku update beta heroku plugins:install @heroku-cli/plugin-manifest ```

Then create your app using the --manifest flag. The stack of the app will
automatically be set to container:

```
heroku create <app-name> --manifest
```

> Do not forget change <app-name> for your app name

Commit your [heroku.yml](heroku.yml) to git:

```
git add heroku.yml
git commit -m "Add heroku build manifest"
```

Push the code:

```
git push heroku master
```

> Please check the [Known issues and limitations](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml#known-issues-and-limitations)
> for this approach

Finally, your application can be accessed from the Heroku [dashboard](https://dashboard.heroku.com/apps)! 🚀
