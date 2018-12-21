FROM nginx:1.14

WORKDIR /app

RUN apt-get update 
RUN apt-get install -y python-pip python-dev
RUN pip install uwsgi
RUN pip install supervisor
RUN pip install flask
COPY app_site.conf /etc/nginx/conf.d/

