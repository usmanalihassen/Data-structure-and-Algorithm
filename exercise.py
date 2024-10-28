F=1
k=0
for i in range(10):
    sum=F+k
    print(sum)
    k=F
    F=sum
    def f(n):
        if n <=1:
            return n
        else:
            return f(n-1)+f(n-2)
print(f(19))
            
