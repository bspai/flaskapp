# flaskapp
This is a skeleton for application using flask framework along with configurations for production ready server using nginx and uwsgi.
This is tested on Ubuntu 16.04.

Note: This setup is created for a specific project at the time of creation. In future this may be extended for generalazing.

### Steps to set-up on Ubuntu 16.04:
Create a username *flask* in Ubuntu and give sudo privilege and login as *flask* user.

Clone this repo to home folder and rename the folder as myproject.

Install python,pip,nginx as below,
```
  sudo apt-get update
  sudo apt-get install python-pip python-dev nginx
```

Install python virtual environment as below,
```
  sudo pip install virtualenv
```

Copy the ~/myproject/uwsgi-service/uwsgi.service to /etc/systemd/system and run
```
  sudo systemctl start uwsgi.service
```
Reconfigure default ports on /etc/nginx/sites-available/default from 80 to some other port, say 8088, wherever you see the configurations.

Copy the ~/myproject/nginx/myproject to /etc/nginx/sites-available/ and run
```
  sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
  sudo service nginx restart
```

You should see "Hello There!" on the browser screen when you browse for http://localhost


#### References:
1. https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04
2. https://www.digitalocean.com/community/tutorials/how-to-set-up-uwsgi-and-nginx-to-serve-python-apps-on-centos-7


### Steps to run flask sample app with Docker container
In this section you will find steps to create docker image and run docker container locally and use the sample flask application. 

1. Change directory to docker directory.
```
  cd docker
```
You will find below contents,
- *app*, a directory which contains python files related to sample application. 
- *default*, a nginx default configuration file which actually to overide port 80 for nginx inside container.
- *docker-compose.yml*, a docker-compose configuration file for maintaining the docker container.
- *supervisord.conf*, a supervisord configuration file for configuring nginx and uwsgi processes inside conatiner.
- *imgdoc*, a directory containing Dockerfile for creating docker image and a nginx configuration file for the directing traffic to uwsgi through unix socket app_site.conf

2. Build the docker image
```
  docker build -t nginxpy:2 imgdoc
```

3. Run the docker container,
```
  docker-compose up -d
```
4. Verification,
You should see "Hello There!" on the browser screen when you browse for http://localhost:8180

Note: docker-compose configuration is exposing container port 80 through host port 8180. You can update this according your requirements.
