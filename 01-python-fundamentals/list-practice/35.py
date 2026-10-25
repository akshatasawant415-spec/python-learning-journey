#35. Create a list and remove all even numbers.
num=[1,2,3,4,5]
res=[]
for i in num:
    if i%2==0:
        res.append(i)
print(res)