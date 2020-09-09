#sublist in  list

def s(x,y):
   common=0
   for value in x:
      if value in y:
         common=1
   if(not common):
      print ("its gone")
   else:
       print ("match")
s([1,1,2,3,4,5,6],[1,1,5])

#CAPTALIZE
p=["hi whatsapp"]
q=map(lambda x:x.title(),p)
r=list(q)
print(r)


#PRIME
def prime(n):
    count=0
    for i in range(2,n):
        if(n%i==0):
            count+=1
    if (count==2):
        print("prime")
    else:
        print("not prime")

l=list(range(1,2501))
print(l)

q=filter(prime,l)
print(list(q))
