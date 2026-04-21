

```shell
sudo apt-get install postgresql
sudo -u postgres createdb graspdb
sudo -u postgres createuser ros -P
sudo -u postgres psql
GRANT ALL PRIVILEGES ON DATABASE graspdb TO ros;
\q
```





```shell
sudo pico /etc/postgresql/9.3/main/postgresql.conf
listen_addresses = '*'
```





```shell
sudo pico /etc/postgresql/9.3/main/pg_hba.conf
host    graspdb         ros             192.168.1.0/24       md5
```


