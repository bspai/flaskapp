# flaskapp
This is a skeleton for application using flask framework along with configurations for production ready server using nginx and uwsgi.
This is tested on Ubuntu 16.04.

Note: This setup is created for a specific project at the time of creation. In future this may be extended for generalazing.

### Steps to set-up:
Create a username *flask* in Ubuntu and give sudo privilege and login as *flask* user.

Clone this repo to home folder and rename the folder as myproject.

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
