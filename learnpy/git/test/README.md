### Regression Client

The client is started by P4V, and communicate with Internal Server, but not connect to Jenkins Server directly.

### Installation

```
pip install colorama --target ./lib
pip install requests --target ./lib
pip install p4python --target ./lib
```



## Functionality

1. Parse user setting: project/change list/ username/ platform
2. Invoke multiple instances to start the network request
3. ...

## How to debug on Windows
1. change bridge server to local host in "Config.py": BridgeServerHost = "http://127.0.0.1:5000"
2. click Run --> Add Configuration -->select Python File
3. set python env in "settings.json"
4. set debug configuration in "launch.json" file, e.g. set program startup path and arguments as below:
```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: startup.py",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/start.py",
            "args": [
                "-c",
                "203290",
                "-u",
                "tianzuoz",
            ]
        }
    ]
}
```
5. Press F5 and start debug.