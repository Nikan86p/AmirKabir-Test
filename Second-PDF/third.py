import time 

def find_missing_elements(il):
    r=il[-1]
    output_list=[]

    for q in range(1,r+1):
        output_list.append(q)

    z= [i for i in output_list if (i in output_list) > (i in il)]

    return z




def sort_list(il):
    n=len(il)
    for i in range(n-1):
        for j in range(n-i-1):
            if il[j]>il[j+1]:
                il[j],il[j+1]=il[j+1],il[j]
    
    return il



def main():
    x=0
    input_list=[]
    while x!=-1 :
        x=int(input("Please enter a valid number for adding to list -> "))
        if 1<=x<=1000:
            input_list.append(x)
        elif x==-1:
            print("\nNice job; we will processing the list that you give us...")
        else:
            print("Please enter a valid number...")
    
    
    process1=time.process_time()
    t=sort_list(input_list)
    g=find_missing_elements(t)
    
    a="*"*5
    print(f"\n{a}")

    for i in g:
        print(i)
    
    print(f"{a}")
    process2=time.process_time()
    print(f"The time for processing was -> {process2-process1:1.5f} seconds\n")



if __name__=="__main__":
    main()