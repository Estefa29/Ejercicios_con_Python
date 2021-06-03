tupla=['matricula','fecha maxima']
x,y=tupla
print (x)
print(y)

tupla=['matricula','fecha maxima']
x=tupla[0]
y=tupla[1]
print (x)
print(y)

tupla=['matricula','fecha maxima']
(x,y)=tupla
print (x)
print(y)

d={'gaseosa':4500,'torta':12600,'pasabocas':3459}
tupla=list(d.items())
print(tupla)
tupla.sort(reverse=True)