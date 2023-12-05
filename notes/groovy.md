```
in groovy:

set a parameter of jenkins job:


```

![image-20231030180740774](C:\Users\yanfeiw\AppData\Roaming\Typora\typora-user-images\image-20231030180740774.png)

```groovy
how to get the variable

stage("test")
{
	echo changelist
	ehco ChangeLiST
	echo "${changelist}"
}

# both ok

```

