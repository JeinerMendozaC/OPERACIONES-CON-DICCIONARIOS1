print("OPERACIONES CON DICCIONARIOS ")
print("1. CREACION DE DICCIONARIOS")
print("#1.1.-PRIMER EJERCICIO:")

D=dict()#diccionario vacio
print(D)

print("#1.2.-SEGUNDO EJERCICIO:")

DICC={}
print(DICC)

print("#1.3.-TERCER EJERCICIO:")

DIC=dict(X=2)
print(DIC)

print("#1.4.-CUARTO EJERCICIO:")

D={1:10,2:20}
print(D)

print("#1.5.-QUINTO EJERCICIO:")

DC={"A":"a","B":"b","C":"c","D":5}
print(DC)

print("#1.6.-SEXTO EJERCICIO:")

DS=dict({1:"a",2:"e",3:"o"})
print(DS)

print("#1.7.-SETIMO EJERCICIO:")

P=[12,13,14,19,19]
Q=["PEDRO","LUIS","ANGELA","EDUARDO","JUAN"]
DCS=dict(zip(P,Q))
print(DCS)

print("#1.8.-OCTAVO EJERCICIO:")
DICC={"LIMA":{"FRUTA","CIUDAD","HERRAMIENTA"},"e":{"VOCAL","N° epsilom"}}
print(DICC)

print("#1.9.-NOVENO EJERCICIO:")

DCSS=dict({0:"PORTAL ENTRE NUMEROS NEGATIVOS Y POSITIVOS"})
print(DCSS)

print("#1.10.-DECIMO EJERCICIO")

dicc={"HOLA":"SALUDO","RESPETO":"VALOR","UVA":"FRUTA"}
print(dicc)


print("2. PERTENENCIA DE CLAVE EN UN DICCIONARIOS")
print("#2.1.-PRIMER EJERCICIO:")

D={}
print( 1 in D)

print("#2.2.-SEGUNDO EJERCICIO:")
S={1:2,3:4,5:6}
print(1 in S)

print("#2.3.-TERCER EJERCICIO:")

S={"A":1,"E":2,"I":3,"O":4,"U":5}
print("A"in S)
print("U" in S)

print("#2.4.-CUARTO EJERCICIO:")

DC=dict({"X":"VARIABLE"})
print("Y" not in DC)

print("#2.5.-QUINTO EJERCICIO:")

DA={1:2,3:3,4:4}
print(3 not in DA)

print("#2.6.-SEXTO EJERCICIO:")

G={"MANZANA":"FRUTA","ARROZ":"ABARROTE","ACE":"DETERGENTE"}
print("FRUTA" in G)

print("#2.7.-SETIMO EJERCICIO:")

SA=dict({"A":1,"E":2,"I":3})
print("A" in SA)

print("#2.8.-OCTAVO EJERCICIO:")

A={1:2}
print(2 not in A)

print("#2.9.-NOVENO EJERCICIO:")

B=dict()
print(1 not in B)

print("#2.10.-DECIMO EJERCICIO")

A={1:1,2:2,3:3}
print(1 in A)


print("3. COMPARACION DE DICCIONARIOS")
print("#3.1.-PRIMER EJERCICIO:")

D={1:2,2:3,3:4,4:5}
D1={2:1,3:2,4:3,5:4}
print(D==D1)

print("#3.2.-SEGUNDO EJERCICIO:")
D={1:2,2:3,3:4,4:5}
D1={2:1,3:2,4:3,5:4}
print(D!=D1)


print("#3.3.-TERCER EJERCICIO:")

A={}
B=dict()
print(A==B)

print("#3.4.-CUARTO EJERCICIO:")

S={1:1,2:2,3:3}
Z={1:1,2:2,3:3}
print(S!=Z)

print("#3.5.-QUINTO EJERCICIO:")

Q={"A":"a","B":"b","C":"c"}
P={"A":"a","B":"b","C":"c"}
print(P==Q)

print("#3.6.-SEXTO EJERCICIO:")

Z={}
AS=dict({1:1})
print(Z==AS)

print("#3.7.-SETIMO EJERCICIO:")

X={1:"A",2:"E",3:"I",4:"O",5:"U"}
Y={"A":1,"E":2,"I":3,"O":4,"U":5}
print(X==Y)

print("#3.8.-OCTAVO EJERCICIO:")

A=dict()
B=dict()
print(A!=B)

print("#3.9.-NOVENO EJERCICIO:")

P={}
Q={}
print(P==Q)

print("#3.10.-DECIMO EJERCICIO")

A={1:2}
Z={2:1}
print(A==Z)


print("4. INDEXACION DE DICCIONARIOS")
print("#4.1.-PRIMER EJERCICIO:")

A={"REDONDO":"CIRULO","RECTANGULO":"CUADRADO"}
print(A["REDONDO"])

print("#4.2.-SEGUNDO EJERCICIO:")

D={1:2,2:3,3:4,4:5}
print(D[1])

print("#4.3.-TERCER EJERCICIO:")

SA=dict({"A":1,"E":2,"I":3})
print(SA["A"])

print("#4.4.-CUARTO EJERCICIO:")

Z=dict({10:1000})
print(Z[10])

print("#4.5.-QUINTO EJERCICIO:")

D={1:"NUMERO","S":"CONSONANTE","A":"VOCAL"}
print(D["S"])

print("#4.6.-SEXTO EJERCICIO:")

SD=dict({1:"a",5:"u"})
print(SD[5])

print("#4.7.-SETIMO EJERCICIO:")

D={1:2,2:3,3:4,4:5}
print(D[2])

print("#4.8.-OCTAVO EJERCICIO:")

Z={1:{"HOLA","MUNDO"},2:"ESTOY",4:"ACA"}
print(Z[1])

print("#4.9.-NOVENO EJERCICIO:")

SA=dict({"A":1,"E":2,"I":3})
print(SA["I"])

print("#4.10.-DECIMO EJERCICIO")

A={1:2}
print(A[1])


print("5. LONGITUD DE DICCIONARIOS")
print("#5.1.-PRIMER EJERCICIO:")

A={1:2}
print(len(A))

print("#5.2.-SEGUNDO EJERCICIO:")

Z={1:{"HOLA","MUNDO"},2:"ESTOY",4:"ACA"}
print(len(Z))

print("#5.3.-TERCER EJERCICIO:")

A=dict()
print(len(A))

print("#5.4.-CUARTO EJERCICIO:")

Q={1:1,2:2,3:3}
print(len(Q))

print("#5.5.-QUINTO EJERCICIO:")

P=[12,13,14,19,19]
Q=["PEDRO","LUIS","ANGELA","EDUARDO","JUAN"]
DCS=dict(zip(P,Q))
print(len(DCS))

print("#5.6.-SEXTO EJERCICIO:")

X={1:3}
S=len(X)
print(S)

print("#5.7.-SETIMO EJERCICIO:")

Q={"PEDRO":12,"LUIS":13,"ANGELA":14,"EDUARDO":19,"JUAN":20}
print(len(Q))

print("#5.8.-OCTAVO EJERCICIO:")

Z={1:1,2:2,3:3}
print(len(Z))

print("#5.9.-NOVENO EJERCICIO:")

Z1={1:1,2:2,3:3,4:3,5:3}
print(len(Z1))

print("#5.10.-DECIMO EJERCICIO")

S=dict({1:1})
print(len(S))


print("6. ITERACION DE DICCIONARIOS ")
print("#6.1.-PRIMER EJERCICIO:")

Z={1:1,2:2,3:3}
for k in Z:
    print(k)

print("#6.2.-SEGUNDO EJERCICIO:")

Q={"PEDRO":12,"LUIS":13,"ANGELA":14,"EDUARDO":19,"JUAN":20}
for k in Q:
    print(k)

print("#6.3.-TERCER EJERCICIO:")

A={1:2,"A":2,"B":1,"S":1}
for k in A:
    print(k)

print("#6.4.-CUARTO EJERCICIO:")

Z=dict({1:"W"})
for k in Z:
    print(k)

print("#6.5.-QUINTO EJERCICIO:")

D={"HOLA":"MUNDO","BB":"HHH","JJJ":"LLLL","MMMM":"NNNN"}
for k in D:
    print(k)

print("#6.6.-SEXTO EJERCICIO:")

A={1:2,2:3,3:4,4:5,5:6,7:8}
for k,v in zip(A.keys(),A.values()):
    print(k,v)

print("#6.7.-SETIMO EJERCICIO:")

v={"NOMBRE":"JOSE","APELLIDO":"SALAZAR","DNI":567890}
for k, v in zip(v.keys(), v.values()):
    print(k, v)

print("#6.8.-OCTAVO EJERCICIO:")

A={"LUIS":16,"JUAN":17,"MARLOM":17,"PERCY":19}
for k, v in zip(A.keys(), A.values()):
    print(k, v)

print("#6.9.-NOVENO EJERCICIO:")

q = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 7: 8}
for k, v in zip(q.keys(), q.values()):
    print(k, v)

print("#6.10.-DECIMO EJERCICIO")

R={1:"HOLA",2:"COMO",3:"ESTAS",4:"AMIGO"}
for k, v in zip(R.keys(), R.values()):
    print(k, v)

print(" 7. BUSQUEDA EN DICCIONARIOS ")
print("#7.1.-PRIMER EJERCICIO:")

A={1:2}
print(A.get(1))

print("#7.2.-SEGUNDO EJERCICIO:")

D={"MANZANA":"FRUTA"}
print(D.get("MANZANA"))

print("#7.3.-TERCER EJERCICIO:")

A=dict({1:2,2:2,3:3})
print(A.get(2))

print("#7.4.-CUARTO EJERCICIO:")

S={"W":"Y","Z":"W","A":"1"}
print(S.get("W"))

print("#7.5.-QUINTO EJERCICIO:")

X={"!":"#","$>":"F"}
print(X.get("!"))

print("#7.6.-SEXTO EJERCICIO:")

Z={1:{1,2,3,4},2:8}
print(Z.get(1))

print("#7.7.-SETIMO EJERCICIO:")

CANDIDATOS={10:"LUIS ESPERANZA",20:"JOSE BARATA",30:"MARCO OCRAM"}
print(CANDIDATOS.get(10))


print("#7.8.-OCTAVO EJERCICIO:")

CANDIDATOS={10:"LUIS ESPERANZA",20:"JOSE BARATA",30:"MARCO OCRAM"}
print(CANDIDATOS.get(20))

print("#7.9.-NOVENO EJERCICIO:")

C={1:2,2:3}
print(C.get(2))

print("#7.10.-DECIMO EJERCICIO")

S=dict({1:"HOLA",2:"COMO",3:"ESTAS"})
print(S.get(1))
print(S.get(2))
print(S.get(3))

print(" 8. ELIMINACION DE DICCIONARIOS ")
print("#8.1.-PRIMER EJERCICIO:")

P={1:2,3:4,5:5}
del P[1]
print(P)

print("#8.2.-SEGUNDO EJERCICIO:")

Q={"A":"a","E":"e","I":"i","O":"o","U":"u"}
del Q["A"]
print(Q)

print("#8.3.-TERCER EJERCICIO:")

A={1:2,3:4,5:6}
del A[5]
print(A)

print("#8.4.-CUARTO EJERCICIO:")

P={1:2,3:4,5:5}
del P[3]
print(P)

print("#8.5.-QUINTO EJERCICIO:")

S={"HOLA":1,"MUNDO":2}
del S["MUNDO"]
print(S)

print("#8.6.-SEXTO EJERCICIO:")

P={10:20,30:4,5:50}
del P[10]
print(P)

print("#8.7.-SETIMO EJERCICIO:")

A=dict({1:"!"})
del A[1]
print(A)

print("#8.8.-OCTAVO EJERCICIO:")

X={1:2,2:3,4:5,6:3}
del X

print("#8.9.-NOVENO EJERCICIO:")

X={1:2,2:3,4:5,6:3}
del X[4]
print(X)

print("#8.10.-DECIMO EJERCICIO")

Y={6:3}
del Y[6]
print(Y)



print(" 9. REMPLAZO EN DICCIONARIOS ")
print("#9.1.-PRIMER EJERCICIO:")

Y={6:3}
Y[6]=12
print(Y)

print("#9.2.-SEGUNDO EJERCICIO:")

Z={1:2,3:5,4:9,0:1}
Z[1]=9
print(Z)

print("#9.3.-TERCER EJERCICIO:")

I={"A":1,"E":2,"I":3}
I["A"]=10
print(I)

print("#9.4.-CUARTO EJERCICIO:")

W=dict({1:"Q"})
W[1]="A"
print(W)

print("#9.5.-QUINTO EJERCICIO:")

SA={12:1,7:0}
SA[7]=13
print(SA)

print("#9.6.-SEXTO EJERCICIO:")

X={1:2,3:5,4:9,0:1}
X[0]="A"
print(X)

print("#9.7.-SETIMO EJERCICIO:")

OP={1:0,0:1}
OP[0]=9
print(OP)

print("#9.8.-OCTAVO EJERCICIO:")

A=dict({"W":"Q","O":"P"})
A["W"]="K"
print(A)

print("#9.9.-NOVENO EJERCICIO:")

W=dict({1:2})
W[1]="A"
print(W)

print("#9.10.-DECIMO EJERCICIO")

F={1:"O",2:"U"}
F[1]="I"
print(F)


print(" 10. AGREGADO EN DICCIONARIO ")
print("#10.1.-PRIMER EJERCICIO:")

D={}
A="EDUARDO"
T="TRACY"
D.setdefault(A,T)
print(D)

print("#10.2.-SEGUNDO EJERCICIO:")

A=dict()
Y="HOLA"
Z=["SALUDO","ESENCIAL"]
A.setdefault(Y,Z)
print(A)

print("#10.3.-TERCER EJERCICIO:")

A={1:2}
A.setdefault(0,8)
print(A)

print("#10.4.-CUARTO EJERCICIO:")

S=dict({2:4})
S.setdefault(1,0)
print(S)

print("#10.5.-QUINTO EJERCICIO:")

W=dict()
A="HOLA"
B="MUNDO"
W.setdefault(A,B)
W.setdefault(1,3)
print(W)

print("#10.6.-SEXTO EJERCICIO:")

SA={}
SA.setdefault(1,0)
SA.setdefault(2,9)
SA.setdefault(5,6)
SA.setdefault(3,9)
print(SA)

print("#10.7.-SETIMO EJERCICIO:")

D=dict()
D.setdefault("a","b")
D.setdefault("c","d")
D.setdefault("e","f")
D.setdefault("g","h")
D.setdefault("i","e")
print(D)

print("#10.8.-OCTAVO EJERCICIO:")

X={1:0,2:9}
X.setdefault(8,0)
X.setdefault(100,19)
print(X)

print("#10.9.-NOVENO EJERCICIO:")

SA=dict({1:9})
SA.setdefault(3,0)
SA.setdefault("W","E")
SA.setdefault("#","%")
SA.setdefault(11,12)
print(SA)

print("#10.10.-DECIMO EJERCICIO")

O={1:10}
O.setdefault(100,120)
print(O)


print(" 11. CREACION DE DICCIONARIOS")
print("#11.1.-PRIMER EJERCICIO:")

A={1:2,2:0,3:0,11:9}
A.clear()
print(A)

print("#11.2.-SEGUNDO EJERCICIO:")

D=dict({1:9})
D.clear()
print(D)

print("#11.3.-TERCER EJERCICIO:")

D1={}
D1.clear()
print(D1)

print("#11.4.-CUARTO EJERCICIO:")

A1={1:2,2:0,3:0,11:9}
A1.clear()
print(A1)

print("#11.5.-QUINTO EJERCICIO:")

SA=dict()
SA.clear()
print(SA)

print("#11.6.-SEXTO EJERCICIO:")

Z=dict({1:9})
Z.clear()
print(Z)

print("#11.7.-SETIMO EJERCICIO:")

XZ={1:9,"W":"K","G":"J"}
XZ.clear()
print(XZ)

print("#11.8.-OCTAVO EJERCICIO:")

A={"S":2}
A.clear()
print(A)

print("#11.9.-NOVENO EJERCICIO:")

C={"AA":"HOLA","BB":"AYUDA","CC":"ESTOY ACA"}
C.clear()
print(C)

print("#11.10.-DECIMO EJERCICIO")

Z=dict({"W":"X"})
Z.clear()
print(Z)


print(" 12 CLONADO")
print("#12.1.-PRIMER EJERCICIO:")

XZ={1:9,"W":"K","G":"J"}
x=XZ.copy()
print(x)

print("#12.2.-SEGUNDO EJERCICIO:")

X={}
Z=X.copy()
print(Z)

print("#12.3.-TERCER EJERCICIO:")

A=dict()
F=A.copy()
print(F)

print("#12.4.-CUARTO EJERCICIO:")

CX={1:2,3:0,4:0}
B=CX.copy()
print(B)

print("#12.5.-QUINTO EJERCICIO:")

Z={1:0}
C=Z.copy()
print(C)

print("#12.6.-SEXTO EJERCICIO:")

SA=dict({1:9,5:0,3:2,12:90})
D=SA.copy()
print(D)

print("#12.7.-SETIMO EJERCICIO:")

XZ={1:9,10:0,2:6,"G":"g"}
x=XZ.copy()
print(x)

print("#12.8.-OCTAVO EJERCICIO:")

I={"NUMER0":12,"DNI":1234567,"NOMBRE":"ALEX"}
S=I.copy()
print(S)

print("#12.9.-NOVENO EJERCICIO:")

XZO=dict({1:9,"A":"W",1:4})
R=XZO.copy()
print(R)

print("#12.10.-DECIMO EJERCICIO")

X={"F":"E","W":"K","G":"J"}
x=X.copy()
print(x)

print(" 13 INSERCION")
print("#13.1.-PRIMER EJERCICIO:")

XZ={1:9,"W":"K","G":"J"}
XZ[1]=90
print(XZ)

print("#13.2.-SEGUNDO EJERCICIO:")

A={1:8}
A[1]=9
print(A)

print("#13.3.-TERCER EJERCICIO:")

B=dict({2:9,4:0})
B[4]=78
print(B)

print("#13.4.-CUARTO EJERCICIO:")

S={1:9,4:0,12:0,11:0}
S[11]=908
print(S)

print("#13.5.-QUINTO EJERCICIO:")

SA=dict({1:9,2:0,3:12})
SA[2]=1234
print(SA)

print("#13.6.-SEXTO EJERCICIO:")

XZ={1:9,"W":"K","G":"J"}
XZ["K"]=90
print(XZ)

print("#13.7.-SETIMO EJERCICIO:")

AD={1:0,2:0,8:9}
AD[8]=56
print(AD)

print("#13.8.-OCTAVO EJERCICIO:")

X1={"Q":"D","J":"A","AS":"AD"}
X1["J"]="WR"
print(X1)

print("#13.9.-NOVENO EJERCICIO:")

SZ=dict({1:0})
SZ[1]="SA"
print(SZ)

print("#13.10.-DECIMO EJERCICIO")

ZX={1:"O",2:"U",3:"I"}
ZX[1]="III"
print(ZX)


print("14 EXTRACCION")
print("#14.1.-PRIMER EJERCICIO:")

A={1:2,3:0,4:0}
Z=A.pop(1)
print(Z)

print("#14.2.-SEGUNDO EJERCICIO:")

S={1:0}
ZZ=S.pop(1)
print(ZZ)

print("#14.3.-TERCER EJERCICIO:")

SA=dict({0:1,3:9})
S=SA.pop(3)
print(S)

print("#14.4.-CUARTO EJERCICIO:")

CX={"A":"E","I":"O","U":"W"}
C=CX.pop("I")
print(C)

print("#14.5.-QUINTO EJERCICIO:")

WA={1:"W",2:"QW",3:"AS"}
V=WA.pop(3)
print(V)

print("#14.6.-SEXTO EJERCICIO:")

D={"A":1,"B":2,"C":8}
SA=D.pop("A")
print(SA)

print("#14.7.-SETIMO EJERCICIO:")

D1={2:3,"A":22,"J":29}
S=D1.pop("A")
print(S)

print("#14.8.-OCTAVO EJERCICIO:")

S=dict({"Q":"A"})
DS=S.pop("Q")
print(DS)

print("#14.9.-NOVENO EJERCICIO:")

CX={"A":"E","I":"O","U":"W"}
C=CX.pop("I")
X=CX.pop("A")
print(X)
print(C)

print("#14.10.-DECIMO EJERCICIO")

X={1:0,2:9}
A=X.pop(1)
A1=X.pop(2)
print(A)
print(A1)



print("15 VER CLAVES")
print("#15.1.-PRIMER EJERCICIO:")

A={1:9,11:23}
print(A.keys())

print("#15.2.-SEGUNDO EJERCICIO:")

X={1:0,2:9}
print(X.keys())

print("#15.3.-TERCER EJERCICIO:")

D={1:7}
print(D.keys())

print("#15.4.-CUARTO EJERCICIO:")

AS={"W":"E","Y":0,2:9}
print(AS.keys())

print("#15.5.-QUINTO EJERCICIO:")

CX={"A":"E","I":"O","U":"W"}
print(CX.keys())

print("#15.6.-SEXTO EJERCICIO:")

XZ={1:9,"W":"K","G":"J"}
print(XZ.keys())

print("#15.7.-SETIMO EJERCICIO:")

A={1:0}
print(A.keys())

print("#15.8.-OCTAVO EJERCICIO:")

S=dict({1:9,"S":"s",3:3})
print(S.keys())

print("#15.9.-NOVENO EJERCICIO:")

I={"NUMER0":12,"DNI":1234567,"NOMBRE":"ALEX"}
print(I.keys())

print("#15.10.-DECIMO EJERCICIO")

S={"A":1,"E":2,"O":3}
print(S.keys())



print("16 VER VALORES")
print("#15.1.-PRIMER EJERCICIO:")

A={1:9,11:23}
print(A.values())

print("#15.2.-SEGUNDO EJERCICIO:")

X={1:0,2:9}
print(X.values())

print("#15.3.-TERCER EJERCICIO:")

D={1:7}
print(D.values())

print("#15.4.-CUARTO EJERCICIO:")

AS={"W":"E","Y":0,2:9}
print(AS.values())

print("#15.5.-QUINTO EJERCICIO:")

CX={"A":"E","I":"O","U":"W"}
print(CX.values())

print("#15.6.-SEXTO EJERCICIO:")

XZ={1:9,"W":"K","G":"J"}
print(XZ.values())

print("#15.7.-SETIMO EJERCICIO:")

A={1:0}
print(A.values())

print("#15.8.-OCTAVO EJERCICIO:")

S=dict({1:9,"S":"s",3:3})
print(S.values())

print("#15.9.-NOVENO EJERCICIO:")

I={"NUMER0":12,"DNI":1234567,"NOMBRE":"ALEX"}
print(I.values())

print("#15.10.-DECIMO EJERCICIO")

S={"A":1,"E":2,"O":3}
print(S.values())


print("17 CONVERSION ")
print("#17.1.-PRIMER EJERCICIO:")

A={1:2,3:4,9:0,10:33}
L=list(A)
print(L)

print("#17.2.-SEGUNDO EJERCICIO:")

A1={"A":"S","B":"b","C":"c","D":"d"}
T=tuple(A1)
print(T)

print("#17.3.-TERCER EJERCICIO:")

Z=dict({1:2,2:3,3:4,5:5})
S=set(Z)
print(Z)

print("#17.4.-CUARTO EJERCICIO:")

A={1:2,3:4,9:0,10:33}
L1=list(A.values())
print(L1)

print("#17.5.-QUINTO EJERCICIO:")

A1={"A":"S","B":"b","C":"c","D":"d"}
T1=tuple(A1.values())
print(T1)

print("#17.6.-SEXTO EJERCICIO:")

WA={1:"W",2:"QW",3:"AS"}
S1=set(WA.values())
print(S1)

print("#17.7.-SETIMO EJERCICIO:")

AS=dict({1:2,2:3})
LA=list(AS)
print(LA)

print("#17.8.-OCTAVO EJERCICIO:")

A={1:2,3:2,7:2,9:2,12:2}
S=set(A.values())
print(S)

print("#17.9.-NOVENO EJERCICIO:")

CX={"A":"E","I":"O","U":"W"}
Z=tuple(CX)
print(Z)

print("#17.10.-DECIMO EJERCICIO:")

AS=dict({"A":"a","E":"e","I":"i","O":"o","U":"u"})
D=tuple(AS.values())
print(D)
print("     ")

print("########### ---- FIN DE EJERCICIOS DE OPERACIONES CON LISTAS ----  #############")