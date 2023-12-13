#!/bin/sh

if [ "$DT" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec $@