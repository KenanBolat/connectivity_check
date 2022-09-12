FROM python:3.9-alpine3.13
LABEL maintainer='Kenan BOLAT'

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./scripts/run.sh /scripts/run.sh
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
            build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
      then /py/bin/pip install -r /tmp/requirements.dev.txt ;  \
    fi &&\
    # rm -rf /tmp && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chmod -R 755 /vol

ENV PATH="/scripts:/py/bin:$PATH"
CMD ["run.sh"]