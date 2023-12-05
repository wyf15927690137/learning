from dask.distributed import Client

if __name__ == '__main__':
    client = Client(n_workers=4)