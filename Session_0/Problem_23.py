def d(n):
 s=1
 for i in range(2,int(n**0.5)+1):
  if n%i==0:s+=i;s+=n//i if i!=n//i else 0
 return s
L=28123
a=[i for i in range(12,L+1)if d(i)>i]
ab=set()
for i in range(len(a)):
 for j in range(i,len(a)):
  s=a[i]+a[j]
  if s<=L:ab.add(s)
  else:break
t=sum(i for i in range(1,L+1)if i not in ab)
print(f"Sum: {t}")
