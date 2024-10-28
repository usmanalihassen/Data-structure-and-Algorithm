array=[7,3,8,2,7,9,1,25]
minval=array[0]

for i in array:
     if minval > i:
        minval=i
print(minval)
#finding maximum value and minimum value 
array1=[1,3,4,7,54,7,0,4,3,2,45,53,66,75,33,26,87.4]
max=array1[0]
for i in array1:
    if max < i:
        max=i
print(max)
min=array1[0]
maxx=array1[0]
for i in array1:
    if min > i:
        min=i
    elif maxx < i:
        maxx=i
print(min)
print(maxx)