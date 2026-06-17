import time

def genarator(t):
    number=0
    found=False
    while not found:
        number+=1
        divisor_count=0
        for i in range(1,number+1):
            if number%i==0:
                divisor_count+=1
        if divisor_count==t:
                print(f"\nThe smallest number with this amount of divisors is -> {number}")
                found=True
        else:
             continue
    
def main():
    while True:
        x=int(input("Please write the amont divisor that you want -> "))
        process1=time.process_time()
        #print(process1)
        if 1<=x<=1000:
            genarator(x)
            process2=time.process_time()
            #print(process2)
            print(f"\nThe time for processing was -> {process2-process1:1.5f} seconds")
            break
        else:
            print("write a posetive number under the 1000")

if __name__=="__main__":
    main()