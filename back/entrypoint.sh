#!/bin/sh

echo "Migrando DB..."
python manage.py reset
echo "DB migrado"

eval "$@"
