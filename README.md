# MomentsServer
[MomentsServer](https://github.com/xdtianyu/MomentsServer) is server side of [Moments](https://github.com/xdtianyu/Moments), it's still under development.

Dependencies
-------

    pip3 install PyMySQL
    pip3 install flask
    pip3 install Flask-SQLAlchemy

**Create mysql database and import test data**

1\. Login to your MYSQL console.

    mysql -uroot -p

2\. Create `moments` database

    CREATE DATABASE moments DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;

3\. Import test data

    use moments;
    source sql/moments.sql;

Deployment
-------

1\. Using `python3` command line

Run `python3 server.py` and it's be deployed at `http://$YOUR_SERVER_IP$:5000`

2\. I suggest that you should use `uwsgi` and `nginx`

    apt-get install uwsgi uwsgi-plugin-python3
    cp uwsgi.ini /etc/uwsgi/apps-available/moments.ini
    cd /etc/uwsgi/apps-enabled
    ln -s ../apps-available/moments.ini
    service uwsgi restart

Default `chdir` in `moments.ini` is `/opt/MomentsServer`, change this to your clone path.

Add the following lines to your nginx site config

```
    location / {
        try_files $uri @moments;
    }

    location @moments {
       include uwsgi_params;
       uwsgi_pass unix:/run/uwsgi/app/moments/socket;
    }
```

LICENSE
-------

```
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
```
