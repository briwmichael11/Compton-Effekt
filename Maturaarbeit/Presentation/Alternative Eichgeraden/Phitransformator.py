import math
from sympy import symbols, Eq, solve, diff, cos, simplify

#Konstanten
me = 9.10938356e-31 #Elektronenmasse
c = 299792458 #Lichtgeschwindigkeit
E=662*(1.60218*10**(-16))
#Umwandeln von keV in Joule
original_0= 677.9830754884214*(1.60218*10**(-16))
v1_0= 682.9830754884214*(1.60218*10**(-16))
v2_0= 672.9830754884214*(1.60218*10**(-16))
v3_0= 675.1687178377463*(1.60218*10**(-16))
v4_0= 680.7974331390964*(1.60218*10**(-16))
original_10= 654.7344342106618*(1.60218*10**(-16))
v1_10= 659.7344342106618*(1.60218*10**(-16))
v2_10= 649.7344342106618*(1.60218*10**(-16))
v3_10= 651.6157749725814*(1.60218*10**(-16))
v4_10= 657.8530934487421*(1.60218*10**(-16))
original_20= 614.3900329292541*(1.60218*10**(-16))
v1_20= 619.3900329292541*(1.60218*10**(-16))
v2_20= 609.3900329292541*(1.60218*10**(-16))
v3_20= 610.7433056115741*(1.60218*10**(-16))
v4_20= 618.0367602469339*(1.60218*10**(-16))
original_45= 480.9826683456919*(1.60218*10**(-16))
v1_45= 485.9826683456919*(1.60218*10**(-16))
v2_45= 475.9826683456919*(1.60218*10**(-16))
v3_45= 475.5897713345099*(1.60218*10**(-16))
v4_45= 486.3755653568739*(1.60218*10**(-16))
original_75= 336.326562618549*(1.60218*10**(-16))
v1_75= 341.326562618549*(1.60218*10**(-16))
v2_75= 331.326562618549*(1.60218*10**(-16))
v3_75= 329.0402610821426*(1.60218*10**(-16))
v4_75= 343.6128641549554*(1.60218*10**(-16))
original_95= 267.70264298212334*(1.60218*10**(-16))
v1_95= 272.70264298212334*(1.60218*10**(-16))
v2_95= 262.70264298212334*(1.60218*10**(-16))
v3_95= 259.5181226023082*(1.60218*10**(-16))
v4_95= 275.8871633619384*(1.60218*10**(-16))
original_120= 215.81833368169308*(1.60218*10**(-16))
v1_120= 220.81833368169308*(1.60218*10**(-16))
v2_120= 210.81833368169308*(1.60218*10**(-16))
v3_120= 206.95469930579904*(1.60218*10**(-16))
v4_120= 224.6819680575871*(1.60218*10**(-16))

#Grad
#0°

#10°
#original
phi10original = math.acos(-me*c**2*(1/original_10-1/E)+1)
phi10gradoriginal = phi10original*(180/math.pi)
print("phi10grad_original=",phi10gradoriginal)
#v1
phi10v1 = math.acos(-me*c**2*(1/v1_10-1/E)+1)
phi10gradv1 = phi10v1*(180/math.pi)
print("phi10grad_v1=",phi10gradv1)
#v2
phi10v2 = math.acos(-me*c**2*(1/v2_10-1/E)+1)
phi10gradv2 = phi10v2*(180/math.pi)
print("phi10grad_v2=",phi10gradv2)
#v3
phi10v3 = math.acos(-me*c**2*(1/v3_10-1/E)+1)
phi10gradv3 = phi10v3*(180/math.pi)
print("phi10grad_v3=",phi10gradv3)
#v4
phi10v4 = math.acos(-me*c**2*(1/v4_10-1/E)+1)
phi10gradv4 = phi10v4*(180/math.pi)
print("phi10grad_v4=",phi10gradv4)

#20°
#original
phi20original = math.acos(-me*c**2*(1/original_20-1/E)+1)
phi20gradoriginal = phi20original*(180/math.pi)
print("phi20grad_original=",phi20gradoriginal)
#v1
phi20v1 = math.acos(-me*c**2*(1/v1_20-1/E)+1)
phi20gradv1 = phi20v1*(180/math.pi)
print("phi20grad_v1=",phi20gradv1)
#v2
phi20v2 = math.acos(-me*c**2*(1/v2_20-1/E)+1)
phi20gradv2 = phi20v2*(180/math.pi)
print("phi20grad_v2=",phi20gradv2)
#v3
phi20v3 = math.acos(-me*c**2*(1/v3_20-1/E)+1)
phi20gradv3 = phi20v3*(180/math.pi)
print("phi20grad_v3=",phi20gradv3)
#v4
phi20v4 = math.acos(-me*c**2*(1/v4_20-1/E)+1)
phi20gradv4 = phi20v4*(180/math.pi)
print("phi20grad_v4=",phi20gradv4)

#45°
#original
phi45original = math.acos(-me*c**2*(1/original_45-1/E)+1)
phi45gradoriginal = phi45original*(180/math.pi)
print("phi45grad_original=",phi45gradoriginal)
#v1
phi45v1 = math.acos(-me*c**2*(1/v1_45-1/E)+1)
phi45gradv1 = phi45v1*(180/math.pi)
print("phi45grad_v1=",phi45gradv1)
#v2
phi45v2 = math.acos(-me*c**2*(1/v2_45-1/E)+1)
phi45gradv2 = phi45v2*(180/math.pi)
print("phi45grad_v2=",phi45gradv2)
#v3
phi45v3 = math.acos(-me*c**2*(1/v3_45-1/E)+1)
phi45gradv3 = phi45v3*(180/math.pi)
print("phi45grad_v3=",phi45gradv3)
#v4
phi45v4 = math.acos(-me*c**2*(1/v4_45-1/E)+1)
phi45gradv4 = phi45v4*(180/math.pi)
print("phi45grad_v4=",phi45gradv4)

#75°
#original
phi75original = math.acos(-me*c**2*(1/original_75-1/E)+1)
phi75gradoriginal = phi75original*(180/math.pi)
print("phi75grad_original=",phi75gradoriginal)
#v1
phi75v1 = math.acos(-me*c**2*(1/v1_75-1/E)+1)
phi75gradv1 = phi75v1*(180/math.pi)
print("phi75grad_v1=",phi75gradv1)
#v2
phi75v2 = math.acos(-me*c**2*(1/v2_75-1/E)+1)
phi75gradv2 = phi75v2*(180/math.pi)
print("phi75grad_v2=",phi75gradv2)
#v3
phi75v3 = math.acos(-me*c**2*(1/v3_75-1/E)+1)
phi75gradv3 = phi75v3*(180/math.pi)
print("phi75grad_v3=",phi75gradv3)
#v4
phi75v4 = math.acos(-me*c**2*(1/v4_75-1/E)+1)
phi75gradv4 = phi75v4*(180/math.pi)
print("phi75grad_v4=",phi75gradv4)

#95°
#original
phi95original = math.acos(-me*c**2*(1/original_95-1/E)+1)
phi95gradoriginal = phi95original*(180/math.pi)
print("phi95grad_original=",phi95gradoriginal)
#v1
phi95v1 = math.acos(-me*c**2*(1/v1_95-1/E)+1)
phi95gradv1 = phi95v1*(180/math.pi)
print("phi95grad_v1=",phi95gradv1)
#v2
phi95v2 = math.acos(-me*c**2*(1/v2_95-1/E)+1)
phi95gradv2 = phi95v2*(180/math.pi)
print("phi95grad_v2=",phi95gradv2)
#v3
phi95v3 = math.acos(-me*c**2*(1/v3_95-1/E)+1)
phi95gradv3 = phi95v3*(180/math.pi)
print("phi95grad_v3=",phi95gradv3)
#v4
phi95v4 = math.acos(-me*c**2*(1/v4_95-1/E)+1)
phi95gradv4 = phi95v4*(180/math.pi)
print("phi95grad_v4=",phi95gradv4)

#120°
#original
phi120original = math.acos(-me*c**2*(1/original_120-1/E)+1)
phi120gradoriginal = phi120original*(180/math.pi)
print("phi120grad_original=",phi120gradoriginal)
#v1
phi120v1 = math.acos(-me*c**2*(1/v1_120-1/E)+1)
phi120gradv1 = phi120v1*(180/math.pi)
print("phi120grad_v1=",phi120gradv1)
#v2
phi120v2 = math.acos(-me*c**2*(1/v2_120-1/E)+1)
phi120gradv2 = phi120v2*(180/math.pi)
print("phi120grad_v2=",phi120gradv2)
#v3
phi120v3 = math.acos(-me*c**2*(1/v3_120-1/E)+1)
phi120gradv3 = phi120v3*(180/math.pi)
print("phi120grad_v3=",phi120gradv3)
#v4
phi120v4 = math.acos(-me*c**2*(1/v4_120-1/E)+1)
phi120gradv4 = phi120v4*(180/math.pi)
print("phi120grad_v4=",phi120gradv4)
