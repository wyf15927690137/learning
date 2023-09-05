To allow remote connect, edit pg_hba.conf file:

```
# "local" is for Unix domain socket connections only
local   all             all                                     scram-sha-256
# local   all             all             0.0.0.0/0               scram-sha-256
# IPv4 local connections:
host    all             all             127.0.0.1/32            scram-sha-256
host    all             all             0.0.0.0/0            scram-sha-256
```

