FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set superuser credentials in environment variables
ENV DJANGO_SUPERUSER_EMAIL=admin@example.com
ENV DJANGO_SUPERUSER_PASSWORD=admin
ENV DJANGO_SECRET_KEY=notasecret

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN if [ "x$DJANGO_SECRET_KEY" = "xnotasecret" ] ; then export DJANGO_SECRET_KEY=`python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` ; fi

# Run migrations
RUN python manage.py wait_for_db
RUN python manage.py makemigrations
RUN python manage.py migrate
