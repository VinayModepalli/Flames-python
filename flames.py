a=str(input("Enter Your Name: "))
b=str(input("Enter Your Crush's Name: "))
c=len(a)
d=len(b)
for i in a:
    for j in b:
        if i==j:
            a=a.replace(i,"",1)
            b=b.replace(j,"",1)
            break        
s=a+b
#print(a)
#print(b)
#print(s)
count=len(s)
c2=count%6
#print("letters:" , count)
w="FLAMES"
for i in range(5):
    if i!=0:
        c2=count%(6-i)
    w=w[c2:]+w[0:c2]
    w=w.replace(w[-1],"")
    #print(w)
#print(w)

res = { 'F':'Friend','L':'Lover','A':'Attraction','M':'Marriage','E':'Enemy','S':'Sister'}
print("-->",res[w],"<--")
print('\n')
