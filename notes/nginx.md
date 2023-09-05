# Use nginx container:

## nginx + tomcat:

```sh
docker pull tomcat

sudo docker run -d --name test_tomcat -v /data/yanfeiw/use_nginx/tomcat_mount_dir/webapps:/usr/local/tomcat/webapps -v /data/yanfeiw/use_nginx/tomcat_mount_dir/logs:/usr/local/tomcat/logs -p 35527:8080 tomcat

# there must be a index.html file in the path: /data/yanfeiw/Files/use_nginx/tomcat_mount_dir/webapps/ROOT/index.html
```

```html
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>This is a test file!</h1>
<h1>Welcome to tomcat,yfw!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>


</body>
</html>
```

```sh
http://shsidock1:35527/index.html
http://shsidock1:35527/index3.html
```



## agent tomcat container:

### use custom html file:

```sh
# --volumes-from ==  -v /data/yanfeiw/Files/use_nginx/tomcat_mount_dir/webapps:/usr/local/tomcat/webapps -v /data/yanfeiw/Files/use_nginx/tomcat_mount_dir/logs:/usr/local/tomcat/logs
	# the mount set as tomcat container above
docker run -d --name test_nginx --volumes-from test_tomcat -v /data/yanfeiw/Files/use_nginx/nginx_mount_dir/logs:/var/log/nginx -v /data/yanfeiw/Files/use_nginx/nginx_mount_dir/html:/usr/share/nginx/html -p 80:80  nginx 

docker exec -it test_nginx /bin/bash
# check the nginx config
/usr/sbin/nginx -t
```

### agent tomcat:

### inside the nginx container : config nginx:

```sh
# inside nginx container
apt-get update
apt-get install vim

vim /etc/nginx/nginx.conf
```



```nginx
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    #include /etc/nginx/conf.d/*.conf;

    upstream backend {
        server 10.134.176.64:30050;
    }
    
    server {
        listen  80;
        # server_name won't work when listen is set
        server_name  10.244.1.83;

        location / {
            index index.html index.html;
            # the proxy server address
            # proxy_pass http://10.134.176.64:30050;
            proxy_pass http://10.134.176.64:30050/index3.html;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         }
    }
}
```

```sh
# mount the nginx config file
docker run -d --name test_nginx -v /data/yanfeiw/use_nginx/nginx_mount_dir/config/nginx.conf:/etc/nginx/nginx.conf -p 80:80 nginx
```

```nginx
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}

http {
    # include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                        '$status $body_bytes_sent "$http_referer" '
                        '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    #include /etc/nginx/conf.d/*.conf;

    upstream backend {
        server 10.134.176.64:30050;
    }
    
    server {
        listen  80;
        # server_name won't work when listen is set
        server_name  10.244.1.83;

        location / {
            index index.html index.htm;
            # the proxy server address
            proxy_pass http://10.134.176.64:30050/index3.html;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
}   
```

```nginx
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}

http {
    # include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                        '$status $body_bytes_sent "$http_referer" '
                        '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    #include /etc/nginx/conf.d/*.conf;

    #upstream backend {
        #server 10.134.176.64:30050;
    }
    
    server {
        listen  80;
        # server_name won't work when listen is set
        server_name  10.244.1.83;

        location ~/test1/ {
            proxy_pass http://10.134.176.64:30050;
        }
        
        location ~/test2/ {
            proxy_pass http://10.134.176.64:30055;
        }
    }
}   
```

Load balance:

```
    upstream myserver {
        server 208.208.128.122:8081;
        server 208.208.128.122:8082;
    }
    server {
        listen       80;
        server_name  208.208.128.122;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            root   html;
            proxy_pass   http://myserver;
            #proxy_pass   http://127.0.0.1:8081;
            index  index.html index.htm;
    }

```

![image-20230705162524370](C:\Users\yanfeiw\AppData\Roaming\Typora\typora-user-images\image-20230705162524370.png)

```
sudo docker run -itd -v /data/yanfeiw/use_nginx/tomcat_mount_dir/webapps:/usr/local/tomcat/webapps -v /data/yanfeiw/use_nginx/tomcat_mount_dir/logs:/usr/local/tomcat/logs -p 35529:8080 tomcat

sudo docker run -itd -v /data/yanfeiw/use_nginx/nginx_mount_dir/config/nginx.conf:/etc/nginx/nginx.conf -p 35528:80 nginx

access 
	http://10.134.176.107:35529/
	http://10.134.176.107:35529/vol/index2.html
	http://10.134.176.107:35529/mxv/index4.html
```

nginx agent:

two location agent:

```nginx
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    #include /etc/nginx/conf.d/*.conf;

    # upstream backend {
    #     server 110.134.176.107:35527;
    # }
    
    server {
        listen  80;
        # server_name won't work when listen is set
        server_name  shsidock1;

        location ~ /vol/ {
            proxy_pass http://10.134.176.107:35529;
        }
        
        location ~ /mxv/ {
            proxy_pass http://10.134.176.107:35529;
        }
    }
}
```

```nginx
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    #include /etc/nginx/conf.d/*.conf;

    # upstream backend {
    #     server 110.134.176.107:35527;
    # }

    upstream myserver {
        server 10.134.176.107:30557;
        server 10.134.176.107:35529;
    }
    server {
        listen  80;
        # server_name won't work when listen is set
        server_name  shsidock1;

        location / {
            root html;
            proxy_pass http://myserver;
            index index.html index.htm;
        }
    }
}
```

