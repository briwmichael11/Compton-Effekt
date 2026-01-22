import math
from sympy import symbols, Eq, solve, diff, cos, simplify

me = 9.10938356e-31 #Elektronenmasse
c = 299792458 #Lichtgeschwindigkeit
print(me*c**2)
#Eg in J
Eg10 = 654.7344342106618*(1.60218*10**(-16))
#E von Gammaquanten von Cs(137) in keV
E = 662*(1.60218*10**(-16))
#Fehler aus den Gaussfits
#Muss mit Eichgerade in keV und dann in J umgerechnet werden
#Eichgerade: 0.8919940215753929*x-31.934619491620538
mEg10 = 0.26451461601653214  #Fehler bei 10 Grad in keV
mEg10= mEg10*(1.60218*10**(-16))
#Fehler von Energiefits
#Muss mit Eichgerade in keV und dann in J umgerechnet werden
#Eichgerade: 0.8919940215753929*x-31.934619491620538
mE1 = 0.03202608265992502
mE2 = 0.12016544326951932
mE = ((mE1)**2 + (mE2)**2)**0.5 #Fehler der Eichgerade in keV
mE = mE*(1.60218*10**(-16))
print("mE=",mE)
print("Eg10=",Eg10)
print("E=",E)


#Berechnung Phi
phi10 = math.acos(-me*c**2*(1/Eg10-1/E)+1)
print("phi10=",phi10)
phi10grad = phi10*(180/math.pi)
print("phi10grad=",phi10grad)


#Berechnung Fehler bei 10°
#Ableitungen:
ablE= ((c**2)*me)/((1-((c**2)*me*((1/Eg10)-(1/E))-1)**2)**0.5*(E**2))
print("ablE=",ablE)
ablEg10= -(((c**2)*me)/((1-((c**2)*me*((1/Eg10)-(1/E))-1)**2)**0.5*(Eg10**2)))
print("ablEg10=",ablEg10)
#Fehlerfortpflanzung:
mEg10=((mE*ablE)**2+(mEg10*ablEg10)**2)**0.5
print("mEg10=",mEg10)
#in Grad umrechnen
mEg10grad = mEg10*(180/math.pi)
print("mEg10grad=",mEg10grad)
msyst = 2.5
mEg10tot = (mEg10grad**2 + msyst**2)**0.5
print("mEg10tot=",mEg10tot)

