FROM python:3.12-alpine

RUN apk update \
    && apk add --no-cache \
    gcc \
    musl-dev \
    && rm -rf /var/cache/apk/*


COPY . /app/back
WORKDIR /app/back

RUN pip install -r requirements.txt

ENTRYPOINT ["/app/back/entrypoint.sh"]
CMD ["/usr/local/bin/gunicorn","-b", "0.0.0.0:8000", "-w", "2","-t", "60", "back.wsgi"]
