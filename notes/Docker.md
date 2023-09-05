```shell
docker pull python:latest
docker image ls
docker image rm image_name

# build a image
# -t: tag the image
docker build -t getting-started .

# start a container
# -d: detach -p: map port
docker run -dp 3000:3000 getting-started

# view running container
docker ps
# stop running container
docker stop <container-id>
# once a container is stopped, can rm it
docker rm <container-id>
docker rmi <image-id>

# create a remote repo named getting-started
docker login -u yanfeiw
pw: wyf15927690137
docker tag getting-started yanfeiw/getting-started
# push to remote
docker push yanfeiw/getting-started

docker push yanfeiw/test-nginx:tagname
docker pull yanfeiw/getting-startted

docker search centos
sudo usermod -aG docker yanfeiw && newgrp docker

# to persist data
docker volume create todo-db
docker run -dp 3000:3000 -v todo-db:/etc/todos getting-started
# to inspect where data is stored in disk
docker volume inspect todo-db

# view all the container (including exited container) 
docker ps -a
```

use ubuntu docker:

```
# --rm : rm the current container if exit the container
docker run -it --rm ubuntu /bin/bash
```

use nginx:

```shell
# --name: specify container name
docker run --name webserv -d -p 80:80 nginx
# step into  a detached container
docker exec -it webserv /bin/bash
docker exec -it <container-id> /bin/bash
# operate homepage
ls /usr/share/nginx/html/index.html
echo '<h>Hello , World</h1>' > /usr/share/nginx/html/index.html	
docker diff webserv
# save the current docker container as a new image (add a new layer to the current docker image)
docker commit --author "yanfeiw" --message "change the homepage" webserv nginx:v2

# view the change to the images
docker images
docker history nginx:v2
docker history nginx

# start the new v2 nginx
docker run --name webserv2 -d -p 8082:82 nginx:v2
# view container logs
docker logs webserv2
# delete a running container
docker rm -f webserv2
```

```sh
# inside the nginx container
apt-get udpate
apt-get install vim
vim /usr/share/nginx/html/index.html
```



use dockerfile to operate images:

```shell
# import a blank image
FROM scratch
# each RUN cmd will add one docker layer
RUN apt-get upate
RUN ...
# so
RUN cmd1 \
	&& cmd2 \
	&& cmd3 \
	&& cmd4 
	
# build a image (specify the dockerfile path): the docker path is the context path, when build images, will send the context to the docker damon(docker engine)
docker build -t nginx:v3 .
# run the new image
docker run --name webserv3 -d -p 8083:80 nginx:v3

# save the image as tar package
docker save nginx:v3 | gzip > nginx.v3.tar.gz
docker load -i nginx.v3.tar.gz
```

create private docker repo

```shell
docker run --name myregistry -d -p 8084:5000 registry:2.6.2
docker ps
docker tag nginx:v3 
```

use docker volume

```shell
docker exec -it mysql /bin/bash
mysql -uroot
```

```mysql
show databases;
create database docker;
show databases;
```

```shell
docker rm -f mysql1

# view docker volume
docker volume ls
docker inspect mysql1 (mounts: name , destination)
# -v : specify the name (mounts) and destination of volume
docker run  --name mysql2 -v mysql:/var/lib/mysql -d -p 3309:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=true mysql:5.7
docker ps
# without mounts
docker exec -it mysql2 /bin/bash
mysql
show databases;
# delete a volume
docker volume rm mysql

```

docker net work

```
# if two containers are in the same network, they can talk to each other

# create a net work
docker network create todo-app

```

install docker on centos

```
sudo yum install -y yum install http://mirror.centos.org/centos/7/extras/x86_64/Packages/slirp4netns-0.4.3-4.el7_8.x86_64.rpm
sudo yum install docker-ce-20.10.21
```





docker install  mongo

```sh
docker pull mongo:latest
docker pull mongo:3.4.24
# run mongodb container
docker run -itd --name mongo -p 27017:27017 mongo --auth
	# --name 'mongo': name the container to run
	# mongo : the name of the local images (if not latest, mongo:version )
	# --auth: need pw to access the service
	# -i: interactive
	# -t: start command line
	# -v: map volume
	# -d: background
	# -p: map port
	# -e username='yanfeiw' : set env
	# --prrevileged: use real root permission
docker run -itd --name 'testmongo' -v /var/lib/mongo:/data/db -p 27017:27017 mongo:3.4.24	
# step into container
docker exec -it mongo bash
# in docker shell
mongo
# view docker container log
docker logs mongo (container name)

dcoker stop edf20ea94acb
docker rm edf20ea94acb
```

use Dockerfile create python container:

Dockerfile:

```
FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/app/main.py"]
```

```sh
# docker build image
docker build -f Dockerfile -t hello-python:latest .
docker image ls
# docker run container
docker run -p 5001:5000 hello-python

access http://localhost:5001
```

Volume:

```
docker volume ls
docker volume inspect <volume name>
```

# create an image from a container:

```sh
# when a container is updated, to save the current container
docker commit <container ID>
docker images -a
# will see the new generated container, then tag it
docker tag 0c17f0798823 hello_world_nginx
```

# save image and use image:

```sh
docker save -o <image-name>.tar <image-name>:tag
docker load -i <image-name>.tar
```

```sh
docker run  --rm --gpus all -it -p 8000:5901 -v /lan/sig/cds/23.10/main/latest:/clarity -v /data/Project/nfs/GPU_related/gpu-burn:/gpu-burn  -v /data/Project/nfs:/case nvidia/cuda:12.0.0-runtime-centos7 /bin/bash
```

```sh
sudo docker run -itd --name test_clarity_gui -e USER=root -v /data/yanfeiw/Files/docker_vnc:/workspace -v /dev/shm:/dev/shm -p 6902:5902 test_gui
```

```
docker run -it --privileged==true centos7:v1 
```

# the final clarity_gui_iamge: **centos7_ssh_vnc2** on shsirdlnx1

```sh
sudo docker run -itd --name test_clarity_gui -v /data/yanfeiw/Files/docker_vnc:/workspace -p 6901:5901 --privileged centos7_ssh_vnc2
sudo docker exec -it dcbe49716194b817fb080a21fc9d7db18772abadd37d8bcb446234a226ff0b84 bash
```

# run fidelity:

```sh
docker run --rm --gpus all -it -p 8080:5901 -v /lan/sig/cds/23.10/main/latest:/clarity -v /data/Project/nfs/GPU_related/gpu-burn:/gpu-burn -v /data/Project/nfs:/case nvidia/cuda:12.0.0-runtime-centos7 /bin/bash
export CDS_LIC_FILE=6280@sjflex7.cadence.com
vncserver -depth 24 -geometry 1920x1080
```

# Use private docker registry:

```sh
docker login -u svc_cicd -p Shang@123 https://docker-team-fidelity.artifacts.cadence.com
docker tag fidelity_docker_image docker-team-fidelity.artifacts.cadence.com/fidelity_docker_image
# push to remote
docker push docker-team-fidelity.artifacts.cadence.com/fidelity_docker_image
cat ~/.docker/config.json

```

```
{
        "auths": {
                "docker-team-fidelity.artifacts.cadence.com": {
                        "auth": "c3ZjX2NpY2Q6U2hhbmdAMTIz"
                }
        }
}
```

```sh
# encode the json file to base64
https://base64.guru/converter/encode/file
```

```sh
ew0KICAgICJhdXRocyI6IHsNCiAgICAgICAgICAgICJkb2NrZXItdGVhbS1maWRlbGl0eS5hcnRpZmFjdHMuY2FkZW5jZS5jb20iOiB7DQogICAgICAgICAgICAgICAgICAgICJhdXRoIjogImMzWmpYMk5wWTJRNlUyaGhibWRBTVRJeiINCiAgICAgICAgICAgIH0NCiAgICB9DQp9
```

K8S use secret:

```yml
apiVersion: v1
kind: Secret
metadata:
  name: fidelity-secret
  namespace: cluster-job2
type: kubernetes.io/dockerconfigjson
data:
  .dockerconfigjson: ew0KICAgICJhdXRocyI6IHsNCiAgICAgICAgICAgICJkb2NrZXItdGVhbS1maWRlbGl0eS5hcnRpZmFjdHMuY2FkZW5jZS5jb20iOiB7DQogICAgICAgICAgICAgICAgICAgICJhdXRoIjogImMzWmpYMk5wWTJRNlUyaGhibWRBTVRJeiINCiAgICAgICAgICAgIH0NCiAgICB9DQp9
```



```
kubectl create secret generic regcred --from-file=.dockerconfigjson=~/.docker/config.json --type=kubernetes.io/dockerconfigjson


kubectl create secret docker-registry regcred --docker-server=docker-team-fidelity.artifacts.cadence.com  --docker-username=svc_cicd -- docker-password=Shang@123 -n cluster-job2
```



Manage docker as a non-root user

```
https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user
```

copy files inside the container to localhost

```
sudo docker cp 241bdaf44690:/var/www ./var/www
```

```
docker run -it --runtime=nvidia --gpus all docker-team-fidelity.artifacts.cadence.com/fidelity/cudagl_rocky8_xfce4_12.0.1 /bin/bash
docker run -it -u 2000 cascade /bin/bash
docker run -it -u 2000 cascade /usr/local/bin/millenniumLauncher.sh -act start -nogpu true


docker run -it -u 2000 docker-team-fidelity.artifacts.cadence.com/fidelity/cudagl_rocky8_xfce4_12.0.1:v3 /usr/local/bin/millenniumLauncher_visual.sh -act start -nogpu true
```

