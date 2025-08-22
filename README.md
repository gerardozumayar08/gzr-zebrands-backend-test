# gzr-zebrands-backend-test
Backend technical test. Basic catalog system to manage products

---

## Requweiremenst

- Python 3.18
- Docker
- PostgreSQL 15
- poetry==1.4.2

---

## Install a local run

1. **Clona el repositorio**

```bash
> git clone https://github.com/gerardozumayar08/gzr-zebrands-backend-test.git
> cd gzr-zebrands-backend-test
```
2. **Setteing .evn file**

```bash
environment=local
language=en
## LOCAL ##
DB_PASSWORD=password
DB_NAME=gzr-database
DB_HOST=127.0.0.1
DB_USER=user
DB_PORT=5432
```

3. a **Run with docker*

```bash
> docker-composer up
```

3. b **Run in terminal*
```bash
> pip install pipenv
> pipenv shell --anyway
> pip install poetry==1.4.2
> poetry install --only main
> poetry run uvicorn --reload --host=0.0.0.0 --port=8080 app.api.main:app
```