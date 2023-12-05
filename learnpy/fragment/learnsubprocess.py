import subprocess
test = ["python.exe", "test.py"]
subprocess.Popen(test,shell=True)
print("subsub")
exit(1)