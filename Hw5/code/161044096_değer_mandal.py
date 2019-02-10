d = int(input('d='))
sayaç=-1
m=int(d)
mult=1
while (m !=0):
        m=int(m)/10
        sayaç=sayaç+1
print("sayaç=",sayaç)

if(sayaç==0):
       mult=mult*0
       print("no integer to multiply")

a=int(d)
for i in range(0, sayaç):
        H=int(a)%10
        a=int(a)/10
        #print H
        if (H !=0):
            mult=H*mult
print (mult)
