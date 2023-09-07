import math
xini=1
xfin=2.5
h=xfin-xini
aprox=0
cont=1
sw = True
for i in range(0,4,1):
    Ri=((1/cont)*(pow(h,cont)))
    aprox+=pow(-1,i)*Ri    
    cont+=1
print("la aproximacion es ",aprox)
errorPorcentual=abs((math.log(2.5))-aprox)/(math.log(2.5))*100
print("el error porcentual es",errorPorcentual)
