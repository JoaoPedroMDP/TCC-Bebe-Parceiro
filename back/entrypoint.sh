#!/bin/sh

echo "Migrando DB..."
python manage.py migrate --noinput
echo "DB migrado"

eval "$@"
