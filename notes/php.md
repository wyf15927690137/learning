how to start appach server:

```
cp D:\Files\varForApache\var D:\Files\varForApache\httpd-2.4.55-o111s-x64-vs17\Apache24
edit D:\Files\varForApache\httpd-2.4.55-o111s-x64-vs17\Apache24\conf\httpd.conf
	line39 : Define SRVROOT "D:\Files\varForApache\httpd-2.4.55-o111s-x64-vs17\Apache24\var\www"
	line256: DocumentRoot "${SRVROOT}"
			<Directory "${SRVROOT}">
	line289:
    		<IfModule dir_module>
		    	DirectoryIndex index.html
    		</IfModule>
start apache httpd:
	D:\Files\varForApache\httpd-2.4.55-o111s-x64-vs17\Apache24\bin>httpd.exe -D D:\Files\varForApache\httpd-2.4.55-o111s-x64-vs17\Apache24\var\www
	
edit D:\Files\varForApache\php-8.2.7-Win32-vs16-x86\php.ini
	line768:	
		extension_dir = "D:\Files\varForApache\php-8.2.7-Win32-vs16-x86\ext"
	line942:
		extension=openssl
start php
D:\Files\varForApache\php-8.2.7-Win32-vs16-x86\php.exe -S 127.0.0.1:80
```

