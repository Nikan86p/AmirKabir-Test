import time ,sympy as s

def is_prime(n):
    if s.isprime(n):
        return 1
    else:
        return 0

def is_smith(num):
    l=[]
    sum_of_prime_number_nums_of_input_number=0
    sum_of_num_of_input_number=0

    for r in str(num):
        sum_of_num_of_input_number+=int(r)

    prime_list=list(s.primerange(s.prime(pow(10,3))))
    found=is_prime(num)

    if  found==0 :

        for i in prime_list:
            while True:
                if num%i==0:
                    l.append(i)
                    num/=i  
                else:
                    break

        for t in l:
            #print(t)
            for e in str(t):
                sum_of_prime_number_nums_of_input_number+=int(e)

        #print(o)
        #print(f)
        
        if sum_of_prime_number_nums_of_input_number==sum_of_num_of_input_number:
            print("This is a smith num")
            return 3
        else:
            print("It isn't smith number!!")


    else:
        print("It isn't smith number!!")

def main():
    while True:
        smith_list=[]
        x=int(input("Please write a posetive number -> "))
        process1=time.process_time()
        if 1<=x<=10000:
            for r in range(1,x+1):
                if is_smith(r)==3:
                    smith_list.append(r)
                else:
                    None
            g="*"*6
            print(f"\n{g}")
            for i in smith_list:
                print(i)
            print(f"{g}")
            process2=time.process_time()
            print(f"The time for processing was -> {process2-process1:1.5f} seconds\n")

            break
        else:
            print("Please write a valid number...")



if __name__=="__main__":
    main()