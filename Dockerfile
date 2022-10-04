FROM python:3.8-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /app

RUN apk update && apk add libxml2-dev

# upgrading pip
RUN pip install --upgrade pip

# copying requirements
COPY ./requirements.txt /app

# updating the environments for postgres and installing packages for postgres
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev

# installing requirements
RUN pip install -r requirements.txt


# copy project
COPY . /app

#running migrations
RUN python manage.py migrate

# load existing dummy data
# comment this line to not load the dummy data(for production)
RUN python manage.py loaddata webapp/preload_data/preloaded_data.json

# removing environment file
RUN rm .env

# exposing 8000 port for development
EXPOSE 8000

# running the server
CMD [ "python3", "manage.py" , "runserver", "0.0.0.0:8000"]