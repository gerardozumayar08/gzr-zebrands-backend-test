#!/bin/bash
cd /app

if [[ "$1" == "shell" ]]; then
    exec /bin/bash

elif [[ "$1" == "generate-revision" ]]; then
    exec python -m alembic revision --autogenerate

elif [[ "$1" == "update-migrations" ]]; then
    exec poetry run alembic upgrade head

elif [[ "$1" == "cron-job" ]]; then
    export PYTHONPATH=$PYTHONPATH:/app
    exec python app/cronjobs/"$2".py

else
    exec poetry run uvicorn --host=0.0.0.0 --port=8080 app.api.main:app --timeout-keep-alive=90
fi
