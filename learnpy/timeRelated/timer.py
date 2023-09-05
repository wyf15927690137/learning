from threading import Timer

def test():
    print("this is a test line")
    Timer(5,test).start()
Timer(5,test).start()