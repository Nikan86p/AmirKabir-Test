import time

def generator(num):
    found=False
    amount=0
    t={"1","0"}
    while not found:
        amount+=1
        for i in range(1,amount):
            mazrab=str(num*i)
            if set(mazrab).issubset(t):
                a="*"*10
                print(f"\n{a}\n{mazrab}\n{a}")
                found=True

def main():
    while True:
        k=int(input("Please write a natural number -> "))
        if 1<=k<=100:
            process1=time.process_time()
            generator(k)
            process2=time.process_time()
            print(f"The time for processing was -> {process2-process1:1.5f} seconds\n")
            break
        else:
            print("Please enter a valid number...")

if __name__=="__main__":
    main()
            



