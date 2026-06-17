import time

def generator(num):
    while len(str(num))!=1:
        q=0
        for i in str(num):
            q+=int(i)
        num=q
    t="*"*4
    print(f"\n{t}\n{num}\n{t}")

def main():
    while True:
        a=int(input("Please write a non-negetive number -> "))
        if 0<=a<=pow(10,9):
            process1=time.process_time()
            generator(a)
            process2=time.process_time()
            print(f"The time for processing was -> {process2-process1:1.5f} seconds\n")
            break
        else:
            print("Please write a valid number fo input...")


if __name__=="__main__":
    main()
