#!/bin/sh

# Load .env
unamestr=$(uname)
if [ "$unamestr" = 'Linux' ]; then
  export $(grep -v '^#' .env | xargs -d '\r')
elif [ "$unamestr" = 'FreeBSD' ] || [ "$unamestr" = 'Darwin' ]; then
  export $(grep -v '^#' .env | xargs -0)
fi

echo "Run migration"
alembic upgrade head

# Start server
COMMAND="$@"

echo "Command $COMMAND"

if [ "$COMMAND" ]; then
  exec $COMMAND
else
  gunicorn -c gunicorn.conf.py core.app:app
fi
