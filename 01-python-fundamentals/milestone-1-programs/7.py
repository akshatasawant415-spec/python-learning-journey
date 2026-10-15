#collection list tuple set dic
list=["Conjuring","Evil Dead","Heredity","Insidious","Annablle"]
print(list[0])
print(list[4])
list.append("It")
list.remove("Evil Dead")
print(list)
for i in list:
    print(i)
tuple=(12.34,45.67)
print(tuple[0])
print(tuple[1])
#set={}
set={1,1,2,3,4,5,6,6}
print(set)
dict={"name":"akshata",
      "age":20,
      "city":"Sangli",
      "favorite language":"Marathi"
    }
print(dict["age"])
print(dict["name"])
print(dict["city"])
print(dict["favorite language"])

Name=input("Enter a name :")
Age=int(input("Enter a age :"))
Marks=int(input("Enter your marks :"))
dict_1={
    "name":Name,
    "age":Age,
    "marks":Marks
}
print(dict_1)
