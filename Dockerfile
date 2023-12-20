FROM python:3.12-alpine3.19

RUN apk add --no-cache build-base

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["entrypoint.sh"]