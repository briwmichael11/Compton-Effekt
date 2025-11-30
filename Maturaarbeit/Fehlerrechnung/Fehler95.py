import math
from sympy import symbols, Eq, solve, diff, cos, simplify

me = 9.10938356e-31 #Elektronenmasse
c = 299792458 #Lichtgeschwindigkeit
print(me*c**2)
#Eg in keV
Eg95 = 267.70264298212334*(1.60218*10**(-16))
#E von Gammaquanten von Cs(137) in keV
E = 662*(1.60218*10**(-16))
#Fehler aus den Gaussfits
mEg95 = 0.22132642618453247 #Fehler bei 95 Grad in keV
mEg95= mEg95*(1.60218*10**(-16))
#Fehler von Energiefits
mE1 = 0.03202608265992502
mE2 = 0.12016544326951932
mE = ((mE1)**2 + (mE2)**2)**0.5 #Fehler der Eichgerade in keV
mE = mE*(1.60218*10**(-16))
print("mE=",mE)
print("Eg95=",Eg95)
print("E=",E)


#Berechnung Phi
phi95 = math.acos(-me*c**2*(1/Eg95-1/E)+1)
print("phi95=",phi95)
phi95grad = phi95*(180/math.pi)
print("phi95grad=",phi95grad)


#Berechnung Fehler bei 20°
#Ableitungen:
ablE= ((c**2)*me)/((1-((c**2)*me*((1/Eg95)-(1/E))-1)**2)**0.5*(E**2))
print("ablE=",ablE)
ablEg95= -(((c**2)*me)/((1-((c**2)*me*((1/Eg95)-(1/E))-1)**2)**0.5*(Eg95**2)))
print("ablEg95=",ablEg95)
#Fehlerfortpflanzung:
mEg95=((mE*ablE)**2+(mEg95*ablEg95)**2)**0.5
print("mEg45=",mEg95)
#in Grad umrechnen
mEg95grad = mEg95*(180/math.pi)
print("mEg95grad=",mEg95grad)
msyst= 7.9
mEg95tot = (mEg95grad**2 + msyst**2)**0.5
print("mEg10tot=",mEg95tot)