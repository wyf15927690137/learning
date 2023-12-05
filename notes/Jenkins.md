How to create Jenkins Api token:

```
In order to generate an API token in Jenkins, we need to follow these steps:

Log in to the Jenkins instance as an administrator
Click on “Manage Jenkins” in the Jenkins dashboard
Click on the “People“
Select the user we want to generate an API token for and click on their name to access their user configuration page
Generate a token using the “Add new token” section of the user configuration page
Click on the “Copy” button to copy the token to the clipboard
Save the configurations

yanfeiw_token
1154dcd2be0ac6338b1e07afb30539744d

admin (for sigrity)
113f4b569d2a7161eb3d9bde75111d4c02

svc_cicd (for fideltiy)
110ab11e08fa74b0498ac8e22411b0a136

```

```
$ curl -X POST http://11.223.231.112:8080/job/testJob/build --user testuser:1100a338c975eb40189c3fe2cf580b2bdf
```



```sh
curl -X post http://master-sigrity.cadence.com:9090/job/AutoBuild/job/CheckCM/buildWithParameters?token=BDEE94C3-AC22-4366-8ADF-1DDB62D989BA -F username=yanfeiw -F BuildVersion=23.10.0314.413863 -F EndChange=41386
```

```bat
curl -H "Content-Type: application/json" -X post  --data-urlencode json='{"parameter":  [{"name":"EndChange","value":"413861"}]}'  http://master-sigrity.cadence.com:9090/job/AutoBuild/job/CheckCM/buildWithParameters?token=BDEE94C3-AC22-4366-8ADF-1DDB62D989BA 

```

```
curl -X post https://master-sigrity.cadence.com:9090/job/ContinuousBuild/job/Remote_Trigger/buildWithParameters?token=BDEE94C3-AC22-4366-8ADF-1DDB62D989BA -F username=yanfeiw 

```

```
fidelity Nali(svc_cicd) API token:
	110ab11e08fa74b0498ac8e22411b0a136
```

# remote trigger job through cmd

```sh
# use job token
bash
curl -X post http://si-rdtest1:9090/job/CheckBuild/job/PreCheck_ISR/buildWithParameters?token=8fbe0598-c71c-42f8-b396-dd48091f6fe7 -F username=yanfeiw -F changelist=428792
```

```sh
# use user apitoken
curl -X POST http://admin:113f4b569d2a7161eb3d9bde75111d4c02@si-rdtest1:9090/job/CheckBuild/job/Auto_Check_merge/job/master/build?
```

```
curl -X post http://svc_cicd:110ab11e08fa74b0498ac8e22411b0a136@eudvl-jenum.cadence.com:8080/job/CheckBuild/job/main/job/Fidelity_All_In_One/buildWithParameters?token=8fbe0598-c71c-42f8-b396-dd48091f6fe7 -F username=yanfeiw
```

# Get jenkins file from git hub

![image-20231120154132621](C:\Users\yanfeiw\AppData\Roaming\Typora\typora-user-images\image-20231120154132621.png)
