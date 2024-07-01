# How to host a MySQL server remotely, we're gonna run it on a Linux server
"""
We're going to run it on a Linux server and be able to access it from any machine we'd like
 assuming that we setup the permissions and the rest correctly

1) Setup Linux server to host MySQL
2) Get users configured in MySQL
3) Use some kind of code (this specific script) and try and connect to the server
"""

"""
1) Linux server

# he uses a sponsor Linode.com server hosting site
#  if it can run on Linux you can host it on Linode

whatever service you use for the hosting remember these two:
- Linode Label: mysql-server  # just name of the server
- Root Password: passwrd  # self explanatory

SSH into server, using a program called 'PuTTY'


address of the server or IPv4 Adress

when you connect to the server you need to download the MySQL server
    sudo apt-get install mysql-server


Now we need to configure it and allow remote access, because otherwise it's localhost
(localhost would be running everything on the website for example)
    sudo mysql_secure_installation utility

proccess:
- type y for VALIDATE PASSWORD PLUGIN and choose password strength
- add root password
- 'remove anonymous users?' - just means that noone can enter root if not on 
    same machine as the server

now we need to setup basic firewall
    sudo ufw enable
    sudo ufw allow mysql  # allows MySQL to bypass firewall

Server Binding
- cd into:  cd /etc/mysql/mysql.conf.d
- to modify specific file we use nano (basic text editor):  nano mysqld.cnf
- scroll down (with arrows) until you reach "bind-adress" 
    at the start it'll be '127.0.0.1' which is just the localhost
    we change it to '0.0.0.0' so that anything can access this server (binding to any IP adress)
- CTRL + S - to save
- CTRL + X - exit

we want to make sure that MySQL is always running on this server
    sudo systemctl start mysql   # starts the service
    sudo systemctl enable mysql  # make it run continously
now we restart it to make sure that the settings are saved
    sudo systemctl restart mysql # restarts it

now we need to setup a user which will access and setup basic database
we go into the MySQL settings and start modiffying things
    mysql -u root -p  # -u root is user root, -p is password but you leave it blank so it asks you for it

Now we're in the MySQL console, you can also write queries in here and grant access to specific users
    CREATE DATABASE IF NOT EXISTS test;
now we're gonna give access to our user to this specific database on our MySQL server
    GRANT ALL ON test.* TO tim@172.168.1.4 IDENTIFIED BY "StrongPassword123456"

    # Grant access to all on all tables in database test  test.*, you can also specific ones test.users
    #  you could give them just viewing permission - GRANT SELECT
    #  or maybe just GRANT SELECT, UPDATE
    #  or perhaps GRANT SELECT, CREATE, DELETE
    #  and finally GRANT ALL
    # to user@IP, we need to get the public IP adress of the machine that's going to be accessing this
    #  here we just put example '172.168.1.4'
    # IDENTIFIED BY "password" - with this password the machine will be able to access this remote server (i.e. "StrongPassword123456")

now we're done on the Linux server
"""


import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="172.105.24.35", # instead of localhost we use SSH IP adress of our server that we created
    user="tim",
    passwd="StrongPassword123456",

    # connects to specific database
    database="test"
    )

mycursor = db.cursor()
mycursor.execute("SHOW TABLES")
print(mycursor.fetchone())
# if you run this and it has no errors then everything is working 

