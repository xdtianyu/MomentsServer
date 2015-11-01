# MomentsServer
MomentsServer is server side for moment, it's still under development.

**Dependency**

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


