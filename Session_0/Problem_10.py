def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True    
    
def main():
    sum=0
    for k in range(2000000):
        if isprime(k)==True:
            sum=sum+k
    print(sum)
    
main()