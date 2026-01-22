import math
from sympy import symbols, Eq, solve, diff, cos, simplify
z0=795.8771895423947
z10=769.8135156663086
z20=724.5840631076989
z45=575.0232349443609
z75=412.8516259108621
z95=335.9184649517497
z120=277.7518090712597

#Konstanten
me = 9.10938356e-31 #Elektronenmasse
c = 299792458 #Lichtgeschwindigkeit
E=662*(1.60218*10**(-16))

#Energien in keV umwandeln
lin0=0.898328*z0 -43.320829
lin10=0.898328*z10 -43.320829
lin20=0.898328*z20 -43.320829
lin45=0.898328*z45 -43.320829
lin75=0.898328*z75 -43.320829
lin95=0.898328*z95 -43.320829
lin120=0.898328*z120 -43.320829
print("lin0=",lin0)
print("lin10=",lin10)
print("lin20=",lin20)
print("lin45=",lin45)
print("lin75=",lin75)
print("lin95=",lin95)
print("lin120=",lin120)

#Energien von keV in Joule umwandeln
lin0j=lin0*(1.60218*10**(-16))
lin10j=lin10*(1.60218*10**(-16))
lin20j=lin20*(1.60218*10**(-16))
lin45j=lin45*(1.60218*10**(-16))
lin75j=lin75*(1.60218*10**(-16))
lin95j=lin95*(1.60218*10**(-16))
lin120j=lin120*(1.60218*10**(-16))

#Winkel berechen
#10°
phi10lin = math.acos(-me*c**2*(1/lin10j-1/E)+1)
phi10gradlin = phi10lin*(180/math.pi)
print("phi10grad_lin=",phi10gradlin)
#20°
phi20lin = math.acos(-me*c**2*(1/lin20j-1/E)+1)
phi20gradlin = phi20lin*(180/math.pi)
print("phi20grad_lin=",phi20gradlin)
#45°
phi45lin = math.acos(-me*c**2*(1/lin45j-1/E)+1)
phi45gradlin = phi45lin*(180/math.pi)
print("phi45grad_lin=",phi45gradlin)
#75°
phi75lin = math.acos(-me*c**2*(1/lin75j-1/E)+1)
phi75gradlin = phi75lin*(180/math.pi)
print("phi75grad_lin=",phi75gradlin)
#95°
phi95lin = math.acos(-me*c**2*(1/lin95j-1/E)+1)
phi95gradlin = phi95lin*(180/math.pi)
print("phi95grad_lin=",phi95gradlin)
#120°
phi120lin = math.acos(-me*c**2*(1/lin120j-1/E)+1)
phi120gradlin = phi120lin*(180/math.pi)
print("phi120grad_lin=",phi120gradlin)