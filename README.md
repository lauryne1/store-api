# store-api

## Clone the project
```bash
$ git clone https://github.com/lauryne1/store-api.git
$ git checkout develop
$ cd store-api
```


## Create and activate virtual environment
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

## Install dependencies
```bash
(venv) $ pip install -r requirements.txt
```

## Configure database connection

```bash
(venv) $ cp .env.example .env
```

Adapt `.env` to your environment.

## Execute migrations

```bash
(venv) $ python3 manage.py migrate
```


## Run the server
```bash
(venv) $ python3 manage.py runserver
```
