# sub dir
# start python.exe sub.py
import subprocess

cmd = ["python.exe", "cp.py"]
subprocess.Popen(cmd,shell=True)
print("success")
