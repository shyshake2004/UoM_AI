def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True    

def main():
    s=0
    k=2
    while s<10001:
        if isprime(k)==True:
            s=s+1
        k=k+1
    print(k-1)

main()