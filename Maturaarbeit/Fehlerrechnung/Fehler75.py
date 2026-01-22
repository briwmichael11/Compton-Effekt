import math
from sympy import symbols, Eq, solve, diff, cos, simplify

me = 9.10938356e-31 #Elektronenmasse
c = 299792458 #Lichtgeschwindigkeit
print(me*c**2)
#Eg in keV
Eg75 = 336.326562618549*(1.60218*10**(-16))
#E von Gammaquanten von Cs(137) in keV
E = 662*(1.60218*10**(-16))
#Fehler aus den Gaussfits
mEg75 = 0.18005838722783296 #Fehler bei 75 Grad in keV
mEg75= mEg75*(1.60218*10**(-16))
#Fehler von Energiefits
mE1 = 0.03202608265992502
mE2 = 0.12016544326951932
mE = ((mE1)**2 + (mE2)**2)**0.5 #Fehler der Eichgerade in keV
mE = mE*(1.60218*10**(-16))
print("mE=",mE)
print("Eg75=",Eg75)
print("E=",E)


#Berechnung Phi
phi75 = math.acos(-me*c**2*(1/Eg75-1/E)+1)
print("phi75=",phi75)
phi75grad = phi75*(180/math.pi)
print("phi75grad=",phi75grad)


#Berechnung Fehler bei 75°
#Ableitungen:
ablE= ((c**2)*me)/((1-((c**2)*me*((1/Eg75)-(1/E))-1)**2)**0.5*(E**2))
print("ablE=",ablE)
ablEg75= -(((c**2)*me)/((1-((c**2)*me*((1/Eg75)-(1/E))-1)**2)**0.5*(Eg75**2)))
print("ablEg75=",ablEg75)
#Fehlerfortpflanzung:
mEg75=((mE*ablE)**2+(mEg75*ablEg75)**2)**0.5
print("mEg75=",mEg75)
#in Grad umrechnen
mEg75grad = mEg75*(180/math.pi)
print("mEg75grad=",mEg75grad)
msyst= 0.37
mEg75tot = (mEg75grad**2 + msyst**2)**0.5
print("mEg10tot=",mEg75tot)