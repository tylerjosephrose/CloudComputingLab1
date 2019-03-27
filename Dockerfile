FROM python

ADD requirements.txt /requirements.txt

# install deps
RUN pip install -r /requirements.txt

# put code in the container
RUN mkdir /code/
WORKDIR /code/
ADD . /code/

# Start the django server
RUN cd /code
CMD python manage.py runserver 0.0.0.0:80


