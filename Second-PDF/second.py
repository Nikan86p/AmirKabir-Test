import time

def count_divisor(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    #print(l)
    return len(l)

def is_highly_composite(q):
    t=[]
    r=count_divisor(q)
    error=[]
    for i in range(1,q):
        t.append(count_divisor(i))
    for h in t:
        if h>=r:
            error.append(h)
    #print(t)
    #print(r)
    if len(error)==0:
        #print("soo morak")
        return 1
    else:
        #print("nooo")
        return 0

def main():
    while True:
        morak_list=[]
        N=int(input("pleae write a posetive number -> "))
        process1=time.process_time()

        if 1<=N<=1000:
            for s in range(1,N+1):
                if is_highly_composite(s)==1:
                    morak_list.append(s)

            g="*"*6
            print(f"\n{g}")

            for x in morak_list:
                print(x)

            g="*"*6
            print(f"{g}")
            process2=time.process_time()
            print(f"The time for processing was -> {process2-process1:1.5f} seconds\n")
            break
        else:
            print("Please enter a valid number...")
    

if __name__=="__main__":
    main()