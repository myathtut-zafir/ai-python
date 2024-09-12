my_st="testing"
print(len(my_st))
# name=input("dd")
# print(name)

name="hello mgmg"
print(name in "hello mgmg")
print(name not in "hello mgmg")

# string slicing
x="Hello_World"
y=[0,1,2,3,4,5,6,7,8,9,10]
print(x[0])
print(x[:])
print(x[:5]) # slice start 0, last number 5 word does not include
print(x[2:]) # slice start from 0
print(x[2:5]) # slice start from 2 last number 5 word does not include
print(y[2:10:2])
print(x[::-1]) # revise string
print(x[-11:-2])

print(x.find("o"))
print(x.rfind("o"))


