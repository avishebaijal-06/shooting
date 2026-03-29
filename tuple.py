a=()
b=tuple()
c=[1,2,3,4,5,6,7,8,9,0]
c=tuple(c)
print (a,b,c)
if 2 in c:
    print ("Yes!")
for i in c:
    print (i)   
# packing
data="Avishe",14,"French",[7.8,9,8.9],{"Home":"Lucknow","School":"La Martiniere Girls' College"}
data[3][0]=6 
data[3].append(9)
data[4]["xyz"]="abc"

# unpacking
name,age,subject,marks,addr=data 
print (data)
print(name,age,subject,marks,addr)      


print(c)
print (c[:])
print (c[0:])
print (c[:10])
print (c[0:10])
print(c[2:7])
print(c[0:-1:2])
print(c[0:-1:3])
c=list(c)
print (c)
group_name=[]
size=[]
date=[]
venue=[]
medal=[]
for i in range (5):
    group_name.append (input("Enter the group name."))
    size.append(input ("Enter the size of the group."))
    date.append (input("Enter the date"))
    venue.append (input("enter the venue"))
    medal.append (input("enter the type of medal")) 

group_tuple=(group_name,size,date,venue,medal)
print (group_tuple) 

