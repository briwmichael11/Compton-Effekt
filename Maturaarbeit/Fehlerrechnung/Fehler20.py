import math
from sympy import symbols, Eq, solve, diff, cos, simplify

me = 9.10938356e-31 #Elektronenmasse
c = 299792458 #Lichtgeschwindigkeit
print(me*c**2)
#Eg in J
Eg20 = 614.3900329292541*(1.60218*10**(-16))
#E von Gammaquanten von Cs(137) in keV
E = 662*(1.60218*10**(-16))
#Fehler aus den Gaussfits
mEg20 = 0.5379094798851779  #Fehler bei 20 Grad in keV
mEg20 = mEg20*(1.60218*10**(-16))
#Fehler von Energiefits
mE1 = 0.03202608265992502
mE2 = 0.12016544326951932
mE = ((mE1)**2 + (mE2)**2)**0.5 #Fehler der Eichgerade in keV
mE = mE*(1.60218*10**(-16))
print("mE=",mE)
print("Eg20=",Eg20)
print("E=",E)


#Berechnung Phi
phi20 = math.acos(-me*c**2*(1/Eg20-1/E)+1)
print("phi10=",phi20)
phi20grad = phi20*(180/math.pi)
print("phi20grad=",phi20grad)


#Berechnung Fehler bei 20°
#Ableitungen:
ablE= ((c**2)*me)/((1-((c**2)*me*((1/Eg20)-(1/E))-1)**2)**0.5*(E**2))
print("ablE=",ablE)
ablEg20= -(((c**2)*me)/((1-((c**2)*me*((1/Eg20)-(1/E))-1)**2)**0.5*(Eg20**2)))
print("ablEg20=",ablEg20)
#Fehlerfortpflanzung:
mEg20=((mE*ablE)**2+(mEg20*ablEg20)**2)**0.5
print("mEg20=",mEg20)
#in Grad umrechnen
mEg20grad = mEg20*(180/math.pi)
print("mEg20grad=",mEg20grad)
msyst=0.1
mEg20tot = (mEg20grad**2 + msyst**2)**0.5
print("mEg20tot=",mEg20tot)