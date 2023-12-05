import traceback
try:
    file1 = "../learncpp/tes01.txt"
    f1 = open(file1)
    for line in f1:
        print(line)
except Exception:
    # print(traceback.format_exc())

print("tset line")