create centos deployment:

```sh
kubectl run centos --image=centos:7 --restart=Never --dry-run=client -o yaml > centos-pod.yaml
```

vim

```yaml
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    run: centos
  name: centos
  namespace: yanfei-dev
spec:
  containers:
  - image: centos:7
    name: centos
    # command: ["/bin/sleep", "3650d"]
    # resources: {}
    # securityContext:
    #   privileged: true
    command:
      - /usr/sbin/init
    securityContext:
      privileged: true
  dnsPolicy: ClusterFirst
  restartPolicy: Never
status: {}

```

```
kubectl apply -f centos-pod.yaml -n <namespace-name>
```

```
kubectl exec -ti centos -- bash
```

```
yum update
```



config ssh:

sudo docker run -itd --name test_clarity --privileged centos7

```sh
yum install openssh-server openssh-clients passwd net-tools -y
systemctl start sshd
systemctl status sshd
```

```
passwd root
abc123
```

outside the container:

```sh
ssh podip -l root
```

config vnc:



```
yum install tigervnc-server
vncserver 
    abc123

vncserver -kill :1
```





xstartup:

```
yum install epel-release vim -y
yum groupinstall "Xfce" -y
vim ~/.vnc/xstartup
```

```sh
#!/bin/sh

unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
startxfce4
```





gnome:

```
yum -y groupinstall "X Window System"
yum -y groupinstall "GNOME Desktop"
vim ~/.vnc/xstartup
```

ssh login with passwd:

```
from machine1 login machine2
on machine1:
	ssh-keygen (enter)
	ssh-copy-id -i ~/.ssh/id_rsa.pub user@machine2
```

# k8s clarity config:

```
passwd
Shang1234
```

