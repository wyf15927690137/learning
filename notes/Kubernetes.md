```sh
minikube version
minikube start
kubectl version
kubectl cluster-info
kubectl get nodes

```

create and deploy an app

```sh
kubectl get nodes
kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1
kubectl get deployments

# in a new terminal
kubectl proxy
curl http://localhost:8001/version
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME
curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/

```

view pods and node

```sh
kubectl get pods
kubectl describe pods
# in a new terminal
kubectl proxy
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME
curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/proxy/
kubectl logs $POD_NAME
kubectl exec $POD_NAME -- env
kubectl exec -ti $POD_NAME -- bash
cat server.js
curl localhost:8080
```

expose kubernetes app outside the cluster

```sh
kubectl get pods
kubectl get services
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080
kubectl get services
kubectl describe services/kubernetes-bootcamp
export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT
curl $(minikube ip):$NODE_PORT

kubectl describe deployment
kubectl get pods -l app=kubernetes-bootcamp
kubectl get services -l app=kubernetes-bootcamp
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME
kubectl label pods $POD_NAME version=v1
kubectl describe pods $POD_NAME
kubectl get pods -l version=v1

# delete services
kubectl delete service -l app=kubernetes-bootcamp
kubectl get services
curl $(minikube ip):$NODE_PORT
kubectl exec -ti $POD_NAME -- curl localhost:8080

```

scale the app

```sh
kubectl get deployments
kubectl get rs
kubectl scale deployments/kubernetes-bootcamp --replicas=4
kubectl get pods -o wide
kubectl describe deployments/kubernetes-bootcamp

# balance the load
kubectl describe services/kubernetes-bootcamp
export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT
curl $(minikube ip):$NODE_PORT

kubectl scale deployments/kubernetes-bootcamp --replicas=2
kubectl get deployments
kubectl get pods -o wide
```

rolling update

```sh
kubectl get deployments
kubectl get pods
kubectl describe pods
kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=jocatalin/kubernetes-bootcamp:v2
kubectl get pods

kubectl describe services/kubernetes-bootcamp
export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT
curl $(minikube ip):$NODE_PORT
kubectl rollout status deployments/kubernetes-bootcamp
kubectl describe pods

# v10 not exsit, roll back
kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=gcr.io/google-samples/kubernetes-bootcamp:v10
kubectl get deployments
kubectl get pods
kubectl describe pods
kubectl rollout undo deployments/kubernetes-bootcamp
kubectl get pods
kubectl describe pods
```

create pod through yml:

```yaml
---
apiVersion: v1
kind: Pod
metadata:
 name: yfw-pod
 labels:
  app: web
spec:
 containers:
  - name: frontend
    image: nginx
    ports:
    - containerPort: 80
```

```
kubectl apply -f pod-example.yaml
```

```
kubeadm --kubernetes-version=v1.26.0 
```

# how to build k8s cluster env:

### on master node:

```sh
cat /etc/hosts
```

```
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
10.134.176.64 master
10.134.176.73 node01
```

```sh
systemctl stop firewalld
systemctl disable firewalld
setenforce 0
cat /etc/selinux/config
cat /etc/sysconfig/selinux
```

### enable route forward:

```sh
vi /etc/sysctl.d/k8s.conf
```

```
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1 
net.ipv4.ip_forward = 1
```

```sh
sysctl -p /etc/sysctl.d/k8s.conf
```

### install docker, kubeadm, kubectl, kubelet

```sh
#docker pull images
bash pull-image.sh
```

```sh
docker pull cnych/kube-apiserver-amd64:v1.10.0
docker pull cnych/kube-scheduler-amd64:v1.10.0
docker pull cnych/kube-controller-manager-amd64:v1.10.0
docker pull cnych/kube-proxy-amd64:v1.10.0
docker pull cnych/k8s-dns-kube-dns-amd64:1.14.8
docker pull cnych/k8s-dns-dnsmasq-nanny-amd64:1.14.8
docker pull cnych/k8s-dns-sidecar-amd64:1.14.8
docker pull cnych/etcd-amd64:3.1.12
docker pull cnych/flannel:v0.10.0-amd64
docker pull cnych/pause-amd64:3.1



docker tag cnych/kube-apiserver-amd64:v1.10.0 k8s.gcr.io/kube-apiserver-amd64:v1.10.0
docker tag cnych/kube-scheduler-amd64:v1.10.0 k8s.gcr.io/kube-scheduler-amd64:v1.10.0
docker tag cnych/kube-controller-manager-amd64:v1.10.0 k8s.gcr.io/kube-controller-manager-amd64:v1.10.0
docker tag cnych/kube-proxy-amd64:v1.10.0 k8s.gcr.io/kube-proxy-amd64:v1.10.0
docker tag cnych/k8s-dns-kube-dns-amd64:1.14.8 k8s.gcr.io/k8s-dns-kube-dns-amd64:1.14.8
docker tag cnych/k8s-dns-dnsmasq-nanny-amd64:1.14.8 k8s.gcr.io/k8s-dns-dnsmasq-nanny-amd64:1.14.8
docker tag cnych/k8s-dns-sidecar-amd64:1.14.8 k8s.gcr.io/k8s-dns-sidecar-amd64:1.14.8
docker tag cnych/etcd-amd64:3.1.12 k8s.gcr.io/etcd-amd64:3.1.12
docker tag cnych/flannel:v0.10.0-amd64 quay.io/coreos/flannel:v0.10.0-amd64
docker tag cnych/pause-amd64:3.1 k8s.gcr.io/pause-amd64:3.1
```

```sh
docker images |grep gcr.io
```

```sh
yum list kubeadm
yum install kubeadm-1.10.0-0
yum install kubelet-1.10.0-0
yum install kubectl-1.10.0-0
```

### config kubeadm

```sh
docker info
Cgroup Driver: cgroupfs  ---->  systemd
vi /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
cgroupfs  ---->  systemd
fail-swap-on=false

systemctl daemon-reload
```

### initial cluster

```sh
# unoccupy a port
yum install -y netstat
netstat -tunlp | grep 8080
    --------------------------
    tcp     0    0 0.0.0.0:8080     0.0.0.0:*    LISTEN     1232/docker-proxy
kill -s 9 1232
```

```sh
# reset the cluster
kubeadm reset -f
rm ~/.kube/config
sudo rm -r /etc/cni/net.d

sudo systemctl restart kubelet
sudo systemctl restart docker
sudo systemctl daemon-reload
sudo cat /var/lib/kubelet/config.yaml | grep group
docker info

systemctl status kubelet

sudo rm /etc/containerd/config.toml
sudo systemctl restart containerd

# initial thea cluster
kubeadm init --kubernetes-version=v1.10.0 --pod-network-cidr=10.244.0.0/16 --apiserver -advertise-address=<masterIP>
setenv PATH "/usr/sbin:$PATH"
sudo kubeadm init --apiserver-advertise-address=10.134.176.64 --pod-network-cidr=10.244.0.0/16

bash
kubectl apply -f ./kube-flannel.yml
kubectl get pods --all-namespaces
kubectl get nodes


```

```sh
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

### config network

```sh
wget https://raw.githubusercontent.com/coreos/flannel/v0.10.0/Documentation/kube-flannel.yml
kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/v0.20.2/Documentation/kube-flannel.yml
kubectl apply -f kube-flannel.yml

kubectl apply -f https://github.com/coreos/flannel/raw/master/Documentation/kube-flannel.yml (can not use sudo permission or will report errors)



https://github.com/flannel-io/flannel/releases

kubectl apply -f https://github.com/coreos/flannel/raw/master/Documentation/kube-flannel.yml
```

```sh
# view all pods
kubectl get pods --all-namespaces
# view nodes
kubectl get nodes
# view component status
kubectl get cs
```

### on node:

```sh
# config /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
10.134.176.64 master
10.134.176.73 node01

systemctl stop firewalld
systemctl disable firewalld
setenforce 0

# enable route forward
sudo vi /etc/sysctl.d/k8s.conf

net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1

sysctl -p /etc/sysctl.d/k8s.conf

docker pull cnych/kube-proxy-amd64:v1.10.0
docker pull cnych/flannel:v0.10.0-amd64
docker pull cnych/pause-amd64:3.1
docker tag cnych/kube-proxy-amd64:v1.10.0 k8s.gcr.io/kube-proxy-amd64:v1.10.0
docker tag cnych/flannel:v0.10.0-amd64 quay.io/coreos/flannel:v0.10.0-amd64
docker tag cnych/pause-amd64:3.1 k8s.gcr.io/pause-amd64:3.1
```

```sh
# change docker cgroups
vi /etc/docker/daemon.json
    {
      "exec-opts": ["native.cgroupdriver=systemd"]
    }

            sudo systemctl restart docker

cat /var/lib/kubelet/config.yaml |grep group
cgroupDriver: systemd


```

# Some  operation:

```sh
kubectl create -f pod-example.yaml
kubectl apply -f pod-example.yaml

# view pod
kubectl get pods
kubectl describe pod yfw-pod

# view pod logs
kubectl logs -f --tail 200 -n kube-flannel kube-flannel-ds-zzllr
kubectl get events --namespace=kube-system
kubectl describe pod/coredns-787d4945fb-p4bcx -n kube-system
```

create deployment to manage pods:

```sh
kubectl version
kubectl cluster-info
# Pods that are running inside Kubernetes are running on a private, isolated network. By default they are visible from other pods and services within the same kubernetes cluster, but not outside that network.
kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.39 -- /agnhost netexec --http-port=8080
kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1
# view kubectl deployments
kubectl get deployments
# view kubectl pods
kubectl get pods
	shsirdlnx2   Ready    control-plane   21d   v1.26.0
	# the node is ready for app to deploy
# view kubectl events
kubectl get events
# view kubectl configuration
kubectl config view

kubectl describe pods/deployments/nodes
kubectl describe node shsirdlnx1

```

proxy:

```sh
# pods are running in an isolated, private network - so we need to proxy access to them so we can debug and interact with them. To do this, we'll use the kubectl proxy command to run a proxy in a second terminal window.

export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.ame}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME
curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/

# new windows
kubectl proxy
# back
curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/proxy/
kubctl logs $POD_NAME
# exec cmd in container
kubectl exec $POD_NAME -- env
kubctl exec -ti $POD_NAME -- bash
curl localhost:8080
```

create service to expose the app:

```sh
# expose the pod to outside network as service 
kubectl get deployment
kubectl get services
kubectl expose deployment hello-node --type=LoadBalancer --port=8080
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080
kubclt describe services/kubernetes-bootcamp

kubectl delete service hello-node
kubectl delete deployment hello-node
```

```sh
# use label to expose an app
kubectl get pods -l app=kubernetes-bootcamp
kubectl get services -l app=kubernetes-bootcamp
# Get the name of the Pod and store it in the POD_NAME environment variable
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
kubectl label pods $POD_NAME version=v1
kubectl describe pods $POD_NAME
kubectl get pods -l version=v1

kubectl delete service -l app=kubernetes-bootcamp
kubectl get services
kubectl exec -ti $POD_NAME -- curl localhost:8080
```

scale up the app:

```sh
kubectl get deployments
# to see the ReplicaSet
kubectl get rs

kubectl scale deployments/kubernetes-bootcamp --replicas=4
kubectl get deployments
kubectl get pods -o wide
kubectl describe deployments/kubernetes-bootcamp
```

# kubernetes deploy tomcat:

```
docker pull kubeguide/tomcat-app:v2
```

vim myweb-rc.yaml

```sh
kind: ReplicationController
metadata:
  name: myweb
spec:
# Pod的数量
  replicas: 1
# spec.selector与spec.template.metadata.labels，这两个字段必须相同，否则下一步创建RC会失败。
  selector:
    app: myweb
  template:
    metadata:
      labels:
        app: myweb
#   容器组的定义
    spec:
      containers:
#       容器名称
        - name: myweb
#         容器对应的镜像
          image: kubeguide/tomcat-app:v1
          ports:
#         在8080端口上启动容器进程，PodIP与容器端口组成Endpoint，代表着一个服务进程对外通信的地址
          - containerPort: 8080
          env:
#此处如果在未安装域名解析的情况下，会无法将mysql对应的IP解析到env环境变量中，因此先注释掉！
#          - name: MYSQL_SERVICE_HOST
#            value: 'mysql'
          - name: MYSQL_SERVICE_PORT
            value: '3306'
```

```
kubectl create -f myweb-rc.yaml
```

```
kubectl delete deployment DEPLOYMENT_NAME -n NAMESPACE_NAME
kubectl delete pod POD_NAME -n NAMESPACE_NAME
kubectl delete svc SERVICE_NAME -n NAMESPACE_NAME

kubectl delete rc mysql
kubectl delete rc myweb
kubectl delete pod mysql-27274
kubectl delete svc mysql
kubectl delete svc myweb

```

deploy nginx:

```sh
kubectl create deployment nginx --image=nginx:1.14-alpine
# expose as service
kubectl expose deployment nginx --port=80 --type=NodePort
kubectl get pods,svc
kubectl describe svc ngix 
    Name:                     nginx
    Namespace:                default
    Labels:                   app=nginx
    Annotations:              <none>
    Selector:                 app=nginx
    Type:                     NodePort
    IP Family Policy:         SingleStack
    IP Families:              IPv4
    IP:                       10.103.176.21
    IPs:                      10.103.176.21
    Port:                     <unset>  80/TCP
    TargetPort:               80/TCP
    NodePort:                 <unset>  32405/TCP
    Endpoints:                10.244.1.7:80
    Session Affinity:         None
    External Traffic Policy:  Cluster
    Events:                   <none>
  
http://10.134.176.73:32405/
```


# Pod Related:

```sh
kubectl create namespace dev
kubectl run nginx --image=nginx:latest --port=80 --namespace=dev
# view pod info
kubectl get pod -n dev -o wide
```

```sh
NAME    READY   STATUS    RESTARTS   AGE   IP           NODE         NOMINATED NODE   READINESS GATES
nginx   1/1     Running   0          21m   10.244.1.9   shsirdlnx1   <none>           <none>
```

```sh
# view pod detailed info
kubectl describe pod nginx -n dev
# how to access the pod
	# on the node which the pod is running on
		curl http://10.244.1.9:80
```

```sh
# delete pod
kubectl delete pod nginx -n dev
# check
kubectl get pod -n dev
# if the pod restart
kubectl get deploy -n dev
kubectl delete deploy nginx -n dev
```

use yaml: pod-nginx.yaml

```yml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  namespace: dev
spec:
  containers:
  - image: nginx:latest
    name: pod
    ports:
    - name: nginx-port
      containerPort: 80
      protocol: TCP
```

```
kubectl create -f pod-nginx.yaml
kubectl delete -f pod-nginx.yaml
```

When the type of Service is `NodePort`, the Service maps the Pod port to the Node port, and the outside of the cluster can access the Pod in the Service through `NodeIP:NodePort`

Pods under the same Service can communicate with each other directly based on PodIP.

Cluster IP is a virtual IP, which is actually a fake IP network.

![image-20230129102213380](C:\Users\yanfeiw\AppData\Roaming\Typora\typora-user-images\image-20230129102213380.png)

# Pod controller:

## ReplicaSet (RS):

### pc-replicaset.yml:

```yml
apiVersion: apps/v1
kind: ReplicaSet   
metadata:
  name: pc-replicaset
  namespace: dev
spec:
  replicas: 3
  selector: 
    matchLabels:
      app: nginx-pod
  template:
    metadata:
      labels:
        app: nginx-pod
    spec:
      containers:
      - name: nginx
        image: nginx:1.17.1
```

```sh
kubectl create -f pc-replicaset.yml
kubectl get rs pc-replicaset -n dev -o wide
```

### scale replicas:

```sh
kubectl edit rs pc-replicaset -n dev
# edit number of replicas to 6

kubectl get rs -n dev

# through command
kubectl scale rs pc-replicaset --replicas=2 -n dev
```

### upgrade images:

```sh
kubectl get rs -n dev -o wide
kubectl edit rs pc-replicaset -n dev
# -image:nginx:1.17.2
kubectl get rs -n dev -o wide

# through command
kubectl set image rs pc-replicaset nginx=nginx:1.17.1 -n dev
```

### delete replica:

```sh
kubectl delete rs pc-replicaset -n dev
(kubectl delete -f pc-replicaset.yml)
```

Deployment:

# k8s label resources:

## command create label:

```sh
kubectl create -f pod-nginx.yaml
# label the resources
kubectl label pod nginx version=1.0 -n dev
# view label
kubectl get pod nginx -n dev --show-labels
# update the resources
kubectl label pod nginx version=2.0 -n dev --overwrite
kubectl get pod nginx -n dev --show-labels
# search labels
kubectl get pod -n dev -l version=2.0 --show-labels
kubectl get pod -n dev -l version!=2.0 --show-labels
# delete labels
kubectl label pod nginx version- -n dev
```

## config labels:

pod-nginx-label.yml

```yml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  namespace: dev
  labels:
    version: "3.0" 
    env: "test"
spec:
  containers:
  - image: nginx:latest
    name: pod
    ports:
    - name: nginx-port
      containerPort: 80
      protocol: TCP
```

```sh
kubectl apply -f pod-nginx-label.yml
# change version 3.0 to 4.0 and apply again
```

# Pod controller--deployment:

## command create deployment:

```sh
# create deployment
kubectl create deployment nginx --image=nginx:latest --port=80 --replicas=3 -n dev
# view deployment
kubectl get deployment -n dev
kubectl get deploy -n dev

kubectl get pods -n dev
kubectl describe deployment nginx -n dev
# delete the deployment
kubectl delete deployment nginx -n dev
```

## config a deployment:

### deploy-nginx.yml

```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
  namespace: dev
spec:
  replicas: 3
  selector:
    matchLabels:
      run: nginx
  template:
    metadata:
      labels:
        run: nginx
    spec:
      containers:
      - image: nginx:latest
        name: nginx
        ports:
        - containerPort: 80
          protocol: TCP
```

```sh
kubectl create -f deploy-nginx.yml
kubectl delete -f deploy-nginx.yml
```

```sh
kubeclt apply -f deploy-nginx.yml
# change version 3.0 to 4.0 and apply again
```

# K8S service:

realize service discovery and load balance

## create service which could be accessed inside the cluster:

```sh
kubectl create deployment nginx --image=nginx:latest --port=80 -n dev
# --type=ClusterIP
	# could only be accessed inside the cluster
kubectl expose deployment nginx --name=svc-nginx1 --type=ClusterIP --port=80 --target-port=80 -n dev

# view service info
kubectl get svc svc-nginx1 -n dev -o wide
```

```
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE   SELECTOR
svc-nginx1   ClusterIP   10.96.111.23   <none>        80/TCP    61s   app=nginx
```

the CLUSTER-IP is the ip of this service.

```sh
# access the pod of the corresponding service on the node which pod runs on
curl 10.96.111.23:80
curl http://10.96.111.23:80
```

## create service which could be accessed outside the cluster:

```sh
kubectl create deployment nginx --image=nginx:latest --port=80 -n dev
kubectl expose deployment nginx --name=svc-nginx2 --type=NodePort --port=80 --target-port=80 -n dev
kubectl get svc svc-nginx2 -n dev -o wide
```

```
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE   SELECTOR
svc-nginx1   ClusterIP   10.96.111.23     <none>        80/TCP         14m   app=nginx
svc-nginx2   NodePort    10.105.213.248   <none>        80:31998/TCP   74s   app=nginx
```

```sh
#  access in browser
http://10.134.176.73:31998
```

## delete service:

```
kubectl delete svc svc-nginx1 -n dev
kubectl delete svc svc-nginx2 -n dev
```

## config service:

### svc-nginx.yml:

```yml
apiVersion: v1
kind: Service
metadata:
  name: svc-nginx1
  namespace: dev
spec:
  clusterIP: 10.96.111.23 #settle intranet ip
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    run: nginx
  type: ClusterIP
```

access service:

```sh
kubectl describe svc hello-python-service
```

```
Name:                     hello-python-service
Namespace:                default
Labels:                   <none>
Annotations:              <none>
Selector:                 app=hello-python
Type:                     NodePort
IP Family Policy:         SingleStack
IP Families:              IPv4
IP:                       10.101.160.137
IPs:                      10.101.160.137
Port:                     <unset>  6000/TCP
TargetPort:               5000/TCP
NodePort:                 <unset>  30683/TCP
Endpoints:                10.244.1.68:5000,10.244.1.69:5000,10.244.1.70:5000
Session Affinity:         None
External Traffic Policy:  Cluster
Events:                   <none>
```

```sh
# on woker node
	# through cluster ip (virtual ip)
		curl 10.101.160.137:6000
	# through pod ip
		curl 10.244.1.68:5000
		curl 10.244.1.69:5000
		curl 10.244.1.70:5000
# outside the cluster
kubectl get svc hello-python-service
```

```
NAME                   TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
hello-python-service   NodePort   10.101.160.137   <none>        6000:30683/TCP   6m34s
```

```sh
http://shsirdlnx1:30683
```

# K8s  mysql:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mysql-pv-volume
  namespace: yanfei-dev
  labels:
    type: local
spec:
  storageClassName: manual
  capacity:
    storage: 20Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/data/users/yanfei/Files/LearnDocker/Kubernetes/mysql"

---

apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pv-claim
  namespace: yanfei-dev
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi
      
```

```sh
kubectl apply -f mysql-pv.yml
```

```yml
apiVersion: v1
kind: Service
metadata:
  name: mysql
  namespace: yanfei-dev
spec:
  ports:
  - port: 3306
  selector:
    app: mysql
  clusterIP: None

---

apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysql
  namespace: yanfei-dev
spec:
  selector:
    matchLabels:
      app: mysql
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - image: mysql:5.6
        name: mysql
        env:
          # Use secret in real usage
        - name: MYSQL_ROOT_PASSWORD
          value: password
        ports:
        - containerPort: 3306
          name: mysql
        volumeMounts:
        - name: mysql-persistent-storage
          mountPath: /var/lib/mysql
      volumes:
      - name: mysql-persistent-storage
        persistentVolumeClaim:
          claimName: mysql-pv-claim
```

```sh
kubectl apply -f mysql-deploy.yml
```

```
kubectl exec -it mysql-79c846684f-ngvjp -n yanfei-dev -- bash
mysql -u root -p
password

kubectl port-forward mysql-79c846684f-ngvjp 3306:3306 -n yanfei-dev
```



# How to use local built images (need to import in k8s lib):

```
docker save hello-python -o hello-python.tar

ctr -n=k8s.io images import hello-python.tar
crictl images
```

# How to use ingress manage service (still fail):

```sh
wget https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.5.1/deploy/static/provider/cloud/deploy.yaml
kubectl apply -f deploy.yaml
# delete all existed job in this namespace or will meet error
	# Error from server (Invalid): error when applying patch:
	
kubectl wait --namespace ingress-nginx --for=condition=ready pod --selector=app.kubernetes.io/component=controller --timeout=120s


kubectl create deployment demo --image=httpd --port=80
kubectl expose deployment demo
kubectl create ingress demo-localhost --class=nginx --rule="demo.localdev.me/*=demo:80"
kubectl port-forward --namespace=ingress-nginx service/ingress-nginx-controller 8080:80

curl http://demo.localdev.me:8080
```

view the group and version info of apiversion:

```sh
kubectl api-resources -o wide
# find the apiversion info of corresponding kind
```

# How to use helm:

```sh
# add repo
helm repo add stable http://mirror.azure.cn/kubernetes/charts
helm repo add aliyun https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
helm repo remove aliyun
# veiw the exsited repo
helm repo list

# deploy an app
helm search repo weave
helm install ui stable/weave-scope
helm list
kubectl get pods
kubectl get svc
```

## custom chart

```sh
helm create mychart
cd template 
kubectl create deployment myweb1 --image=nginx --dry-run -o yaml > deployment.yaml

helm install myweb1 mychart/

```

## Volume:

```

```

# Kubernetes run GPU pods:

```
cat /etc/docker/daemon.json 
```

```
{
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    }
}
```

```sh
cat /etc/containerd/config.toml
```

```sh
version = 2
[plugins]
  [plugins."io.containerd.grpc.v1.cri"]
    [plugins."io.containerd.grpc.v1.cri".containerd]
      default_runtime_name = "nvidia"

      [plugins."io.containerd.grpc.v1.cri".containerd.runtimes]
        [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.nvidia]
          privileged_without_host_devices = false
          runtime_engine = ""
          runtime_root = ""
          runtime_type = "io.containerd.runc.v2"
          [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.nvidia.options]
            BinaryName = "/usr/bin/nvidia-container-runtime"
```

```
 sudo systemctl restart containerd
```



## CRI: container run time:

```

```

forcely delete pod :

```
You can use following command to delete the POD forcefully.

kubectl delete pod <PODNAME> --grace-period=0 --force --namespace <NAMESPACE>
```

# Config nvidia GPU:



image sources:

```sh
# docker
/etc/docker/daemon.json
{ 
"registry-mirrors": [http://192.168.201.67:5000/registry] 
}


KUBELET_POD_INFRA_CONTAINER="--pod-infra-container-image=192.168.201.67:5000/registry"
```

# Image pull policy:

```
Never: use local
Always: use remote
IfNotPresent: use remote if local image not exists
```

# K8s Use private registry:

```sh
docker login -u svc_cicd -p Shang@123 https://docker-team-fidelity.artifacts.cadence.com

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
ew0KICAgICJhdXRocyI6IHsNCiAgICAgICAgICAgICJkb2NrZXItdGVhbS1maWRlbGl0eS5hcnRpZmFjdHMuY2FkZW5jZS5jb20iOiB7DQogICAgICAgICAgICAgICAgICAgICJhdXRoIjogImMzWmpYMk5wWTJRNlUyaGhibWRBTVRJeiINCiAgICAgICAgICAgIH0NCiAgICB9DQp9
```

## create base64 code:

```sh
# echo -n : without trailing newline
echo -n "test line" | base64
echo -n "dGVzdGxpbmU=" | base64 --decode

# encode the json file to base64
https://base64.guru/converter/encode/file
```



## create secret through yaml file:

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

## create secret through command line:

```sh
kubectl create secret generic regcred --from-file=.dockerconfigjson=~/.docker/config.json --type=kubernetes.io/dockerconfigjson

kubectl create secret docker-registry regcred --docker-server=docker-team-fidelity.artifacts.cadence.com  --docker-username=svc_cicd --docker-password=Shang@123 -n cluster-job2
```



Assign node by label:

```
      nodeSelector:
        Group: BigPool
        
      nodeName: shsirdlnx2
```



# report errors:

### Q:

```
 Warning  FailedCreatePodSandBox  2m59s                   kubelet            Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "8750eb9944a4692f2b61a9ab7dc18f6e1cea7f817a8b7269a5b7a0f10fd6bd67": plugin type="flannel" failed (add): failed to delegate add: failed to set bridge addr: "cni0" already has an IP address different from 10.244.0.1/24
```

### A:

```sh

# kubectl get pod -o wide
# ifconfig cni0 down
# ifconfig flannel.1 down
# ifconfig docker0 down
# ip link delete cni0
# ip link delete flannel.1
# systemctl restart docker
```

### Q:

```
journalctl -u kubelet -f 

Network plugin returns error: cni plugin not initialized
```

### A:

```
cat /etc/sysconfig/kubelet
KUBELET_EXTRA_ARGS=--cgroup-driver=systemd
（Kubelet cgroup driver: "cgroupfs" is different from docker cgroup driver: "systemd"）
```

Q:

```
Container image "hello-python:latest" is not present with pull policy of Never

```

![image-20230130104326268](C:\Users\yanfeiw\AppData\Roaming\Typora\typora-user-images\image-20230130104326268.png)

```
build hello-python image on node
```

# Q：

```sh
# view the status of the kubelet
sudo systemctl status kubelet
# detailed info
sudo journalctl -u kubelet -f
```

meet some errors:

```
0228 16:06:13.347579 2813304 run.go:74] "command failed" err="failed to run Kubelet: validate service connection: CRI v1 runtime API is not implemented for endpoint \"unix:///var/run/containerd/containerd.sock\": rpc error: code = Unimplemented desc = unknown service runtime.v1.RuntimeService"
```

A:

```sh
# restart containerd
sudo systemctl status containerd
sudo rm /etc/containerd/config.toml
sudo systemctl restart  containerd
# restart kubelet
sudo systemctl restart kubelet
```

Q: error: unable to decode "01-pv.yml": json: cannot unmarshal number into Go struct field ObjectMeta.metadata.labels of type string

```
metadata.name  metadata.labels can't only container number
```

# while running pod:

```
Warning  FailedScheduling  32s   default-scheduler  0/2 nodes are available: 1 Insufficient nvidia.com/gpu, 1 node(s) had untolerated taint {node-role.kubernetes.io/control-plane: }. preemption: 0/2 nodes are available: 1 No preemption victims found for incoming pod, 1 Preemption is not helpful for scheduling..
```

```
kubectl taint nodes --all node-role.kubernetes.io/control-plane-
```

# How to config Nvidia GPU:

```
https://github.com/NVIDIA/k8s-device-plugin#quick-start

need to config docker and containerd
```

# Pod Unexpected Admission Error

![image-20230517095805860](C:\Users\yanfeiw\AppData\Roaming\Typora\typora-user-images\image-20230517095805860.png)

```
remove the node and then rejoin it
```

Kubelet error

```sh
# sudo journalctl -u kubelet -f
May 17 15:46:17 shsirdlnx1 kubelet[219599]: E0517 15:46:17.489737  219599 run.go:74] "command failed" err="failed to validate kubelet flags: the container runtime endpoint address was not specified or empty, use --container-runtime-endpoint to set"
May 17 15:46:17 shsirdlnx1 systemd[1]: kubelet.service: main process exited, code=exited, status=1/FAILURE
May 17 15:46:17 shsirdlnx1 systemd[1]: Unit kubelet.service entered failed state.
May 17 15:46:17 shsirdlnx1 systemd[1]: kubelet.service failed.
May 17 15:46:27 shsirdlnx1 systemd[1]: kubelet.service holdoff time over, scheduling restart.
May 17 15:46:27 shsirdlnx1 systemd[1]: Stopped kubelet: The Kubernetes Node Agent.
May 17 15:46:27 shsirdlnx1 systemd[1]: Started kubelet: The Kubernetes Node Agent.
May 17 15:46:27 shsirdlnx1 kubelet[220502]: Flag --cgroup-driver has been deprecated, This parameter should be set via the config file specified by the Kubelet's --config flag. See https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ for more information.
```

```
sudo s
```

Config AMD gpu:

```
--allow-privileged=true for both kube-apiserver and kubelet

/etc/kubernetes/manifests/kube-apiserver.yaml
	- --allow-privileged=true
/etc/sysconfig/kubelet
	KUBELET_KUBECONFIG_ARGS="--allow-privileged=true"
	KUBELET_ARGS="--allow-privileged=true"
```

label a node:

```
kubectl label nodes <node-name> <key>=<value>
# remove
kubectl label nodes <node-name> <label-key>-
```

change apiserver port range:

```
vim /etc/kubernetes/manifests/kube-apiserver.yaml
# add this line, kubelet will auto restart the apiserver, wait for a few min and then the cluster will be ready
- --service-node-port-range=30000-32767
```







Nvidia and AMD GPU plugin

```
https://github.com/NVIDIA/k8s-device-plugin

```

k8s make a node unschedulale

```
kubectl cordon shsirdlnx2
kubectl uncordon shsirdlnx2
```

self define custom resources in k8s

```bash
#!/bin/bash
kubectl proxy &
pid=$!
nodes=$(kubectl get node | awk '{print $1}' | tail -n $(( $(kubectl get node | wc -l) - 1 )))
for node in $nodes
do
    curl --header "Content-Type: application/json-patch+json" \
    --request PATCH \
    --data '[{"op": "add", "path": "/status/capacity/millennium.com~1vn", "value": "6"}]' \
    http://localhost:8001/api/v1/nodes/$node/status
done
kill $pid
```

clean custom resources in k8s

```bash
#!/bin/bash
kubectl proxy &
pid=$!
nodes=$(kubectl get node | awk '{print $1}' | tail -n $(( $(kubectl get node | wc -l) - 1 )))
for node in $nodes
do
    curl --header "Content-Type: application/json-patch+json" \
    --request PATCH \
    --data '[{"op": "remove", "path": "/status/capacity/millennium.com~1vn"}]' \
    http://localhost:8001/api/v1/nodes/$node/status
done
kill $pid
```

```
ssh millennium@shsirdlnx2 -p 30723
```

![image-20231204102602881](C:\Users\yanfeiw\AppData\Roaming\Typora\typora-user-images\image-20231204102602881.png)
