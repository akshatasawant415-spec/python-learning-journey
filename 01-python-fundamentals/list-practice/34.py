#34. Create two lists and find their common elements
ls1=[12,13,14,15,22]
ls2=[12,21,22,23,24]
comm=[]
for i in ls1:
    if i in ls2 and i not in comm:
        comm.append(i)
print("Common elements :",comm)