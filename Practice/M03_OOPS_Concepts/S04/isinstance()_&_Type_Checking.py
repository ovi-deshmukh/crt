'''
Type Checking --> it mainly used to check the obj/value is belogns to particular class/datatype

syntax:
isinstance(obj,type)


a = 10
b = 15.5
c =  "Ram"
d = [1,2,3,4,5,6]
e = (1,2,3,10,45,6)
f = {1,2,3,4,5,6}
g = {"name":"Kalyani"}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

'''

a = 10
b = 15.5
c =  "Ram"
d = [1,2,3,4,5,6]
e = (1,2,3,10,45,6)
f = {1,2,3,4,5,6}
g = {"name":"Kalyani"}
print(isinstance(a,int))
print(isinstance(b,float))
print(isinstance(c,str))
print(isinstance(d,list))
print(isinstance(e,list))
print(isinstance(f,set))
print(isinstance(g,dict))

#checking with multiple data types:
x = 'Ram'
if isinstance(x,(int,float)):
    print("X is a number")
else:
    print("X is a String")

#Chceking of Object's Class:
class A:
    pass
class B(A):
    pass
b = B()
print(isinstance(b,A))
print(isinstance(b,B))

#Example:
def process(data):
    if isinstance(data, int):
        return data * 2
    elif isinstance(data, str):
        return data.upper()
    elif isinstance(data,list):
        return len(data)
print(process(10))
print(process('kalyani'))
print(process([1,2,3,5,6,7,8]))


#How they ask in interviews:
class A:
    pass
class B(A):
    pass
obj = B()

print(type(obj) == B)
print(type(obj) == A)
print(isinstance(obj,B))
print(isinstance(obj,A))