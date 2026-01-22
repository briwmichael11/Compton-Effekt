import math
from sympy import symbols, Eq, solve, diff, cos, simplify

me = 9.10938356e-31 #Elektronenmasse
c = 299792458 #Lichtgeschwindigkeit
print(me*c**2)
#Eg in keV
Eg120 = 215.81833368169308*(1.60218*10**(-16))
#E von Gammaquanten von Cs(137) in keV
E = 662*(1.60218*10**(-16))
#Fehler aus den Gaussfits
mEg120 = 0.45594219737303066 #Fehler bei 120 Grad in keV
mEg120= mEg120*(1.60218*10**(-16))
#Fehler von Energiefits
mE1 = 0.03202608265992502
mE2 = 0.12016544326951932
mE = ((mE1)**2 + (mE2)**2)**0.5 #Fehler der Eichgerade in keV
mE = mE*(1.60218*10**(-16))
print("mE=",mE)
print("Eg120=",Eg120)
print("E=",E)


#Berechnung Phi
phi120 = math.acos(-me*c**2*(1/Eg120-1/E)+1)
print("phi120=",phi120)
phi120grad = phi120*(180/math.pi)
print("phi120grad=",phi120grad)


#Berechnung Fehler bei 20°
#Ableitungen:
ablE= ((c**2)*me)/((1-((c**2)*me*((1/Eg120)-(1/E))-1)**2)**0.5*(E**2))
print("ablE=",ablE)
ablEg120= -(((c**2)*me)/((1-((c**2)*me*((1/Eg120)-(1/E))-1)**2)**0.5*(Eg120**2)))
print("ablEg120=",ablEg120)
#Fehlerfortpflanzung:
mEg120=((mE*ablE)**2+(mEg120*ablEg120)**2)**0.5
print("mEg120=",mEg120)
#in Grad umrechnen
mEg120grad = mEg120*(180/math.pi)
print("mEg120grad=",mEg120grad)
msyst= 6.6
mEg120tot = (mEg120grad**2 + msyst**2)**0.5
print("mEg10tot=",mEg120tot)