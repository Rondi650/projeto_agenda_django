FROM python:3.12-alpine3.22

WORKDIR /djangoapp

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
COPY scripts/ /scripts/
RUN pip install -r requirements.txt && \
    chmod +x /scripts/commands.sh
COPY . .

EXPOSE 8000

CMD ["/scripts/commands.sh"]