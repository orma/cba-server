# Environment Variables

This project requires the following environment variables to be set before running the server. These variables should
be placed in an `.env` file under the project root.

**`DJANGO_SECRET_KEY`**

An unique, unpredictable string used to provide cryptographic signing for Django. The value for this setting could be generated using [https://www.miniwebtool.com/django-secret-key-generator/](https://www.miniwebtool.com/django-secret-key-generator/)



**`DJANGO_SETTINGS_MODULE`**

The setting module for this Django server. The default is `configs.settings.development`


**`DJANGO_DB_NAME`**

Name of the PostgreSQL database used in this project, default is `cba_wb`


**`DJANGO_DB_USER`**

The user to connect to the above PostgreSQL database


**`DJANGO_DB_PASSWORD`**

The password for the above user to connect to the PostgreSQL database


**`DJANGO_DB_HOST`**

The host that our database is running. Default is `localhost` or `127.0.0.1`


**`DJANGO_DB_PORT`**

The port that our database server is running. Default is `5432`