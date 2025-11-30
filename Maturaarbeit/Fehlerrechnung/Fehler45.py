import math
from sympy import symbols, Eq, solve, diff, cos, simplify

me = 9.10938356e-31 #Elektronenmasse
c = 299792458 #Lichtgeschwindigkeit
print(me*c**2)
#Eg in keV
Eg45 = 480.9826683456918*(1.60218*10**(-16))
#E von Gammaquanten von Cs(137) in keV
E = 662*(1.60218*10**(-16))
#Fehler aus den Gaussfits
mEg45 = 0.5873537798522647 #Fehler bei 45 Grad in keV
mEg45= mEg45*(1.60218*10**(-16))
#Fehler von Energiefits
mE1 = 0.03202608265992502
mE2 = 0.12016544326951932
mE = ((mE1)**2 + (mE2)**2)**0.5 #Fehler der Eichgerade in keV
mE = mE*(1.60218*10**(-16))
print("mE=",mE)
print("Eg45=",Eg45)
print("E=",E)


#Berechnung Phi
phi45 = math.acos(-me*c**2*(1/Eg45-1/E)+1)
print("phi45=",phi45)
phi45grad = phi45*(180/math.pi)
print("phi45grad=",phi45grad)


#Berechnung Fehler bei 45°
#Ableitungen:
ablE= ((c**2)*me)/((1-((c**2)*me*((1/Eg45)-(1/E))-1)**2)**0.5*(E**2))
print("ablE=",ablE)
ablEg45= -(((c**2)*me)/((1-((c**2)*me*((1/Eg45)-(1/E))-1)**2)**0.5*(Eg45**2)))
print("ablEg45=",ablEg45)
#Fehlerfortpflanzung:
mEg45=((mE*ablE)**2+(mEg45*ablEg45)**2)**0.5
print("mEg45=",mEg45)
#in Grad umrechnen
mEg45grad = mEg45*(180/math.pi)
print("mEg45grad=",mEg45grad)
msyst= 0.2
mEg45tot = (mEg45grad**2 + msyst**2)**0.5
print("mEg10tot=",mEg45tot)
