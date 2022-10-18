from dask.distributed import Client, SSHCluster
import time

if __name__ == '__main__':

    cluster = SSHCluster(
        ["10.134.138.81","10.134.176.64", "10.134.176.73"],
        remote_python = ["D:/Precheck_Local/regressiontest/bin/Python37/python","/data/users/yanfei/Files/Python3/Python-3.7.9/python","/data/yanfeiw/Python-3.7.9/python"]
        )
    client = Client(cluster)
    print(cluster.dashboard_link)

    cluster.get_logs()
    time.sleep(330)

    
import dask.dataframe as dd
dd.msg("test")
