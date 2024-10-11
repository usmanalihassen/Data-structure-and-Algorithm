x=int(input("please enter an integer: "))
if x<0:
    x=0
    print("negative changed to zero")
elif x==0:
    print("zero")
elif x==1:
    print("single")
else:
    print("more") 
#for statements
words=("cat","window","defenestrate")
for w in words:
    print(w,len(w))
#range
for i in range(10):
    print(i)
print(sum(range(5)))