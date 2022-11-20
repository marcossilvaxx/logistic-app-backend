FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD cd app/settings/ && sleep 15 && python run_db_migration.py database_init.sql && python run_db_seed.py && cd ../../ && python run.py