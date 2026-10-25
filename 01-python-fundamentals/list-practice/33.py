#33. Create a list and find the second-largest number
num=[1,2,3,4,5,6,7,8]
uni=list(set(num))
uni.sort()
if len(uni)>=2:
    print("Second largest :",uni[-2])
else:
    print("Second-largest number does not exist")