import time,sympy as s

def generator(nu,pnl,pl):
    for n in pnl:
        while True:
            if nu%n==0:
                pl.append(n)
                nu/=n
            else:
                break    
    print("*"*3)    
    for t in pl:
        print(t)
    print("*"*3)

def main():
    domain=s.prime(pow(10,4))
    prime_nums_list=list(s.primerange(domain))
    prime_list=[]
    while True:
        num=int(input("Please enter a posetive number -> "))
        if 2<=num<=pow(10,9):
            process1=time.process_time()
            generator(num,prime_nums_list,prime_list)
            process2=time.process_time()
            print(f"The time for processing was -> {process2-process1:1.5f} seconds")
            break
        else:
            print("Please write a valid number fo input...")

if __name__=="__main__":
    main()


