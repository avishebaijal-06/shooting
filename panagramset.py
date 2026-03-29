import string, random
a=set()
print (type(a))
sentence= input("enter a sentence").lower()
b=[]
for i in sentence:
    if i.isalpha():
        a.add(i)
print (a)
if len(a)==26:
    print ("its a panagram")
else:
    print ("its not a panagram")   

for i in sentence:
    if i.isalpha():
        if i not in b:
            b.append(i)
print (b)
if len(b)==26:
    print ("its a panagram")
else:
    print ("its not a panagram")   