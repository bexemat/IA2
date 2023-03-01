from funciones import *
#borrosificacion---------------->pasamos del mundo nitido al mundo borroso
# Universo de discurso para el angulo de inclinacion
thetamax = 90
theta = np.arange(-thetamax, thetamax, dt)
# Funciones de pertenencia para el angulo de inclinacion
ANG = trapmf(theta, [-thetamax, -thetamax, -thetamax/2, -thetamax/4])
ANP = trimf(theta, [-thetamax/2, -thetamax/4, 0])
AC = trimf(theta, [-thetamax/4, 0, thetamax/4])
APP = trimf(theta, [0, thetamax/4, thetamax/2])
APG = trapmf(theta, [thetamax/4, thetamax/2, thetamax, thetamax])
A=[ANG,ANP,AC,APP,APG]
A=np.array(A)
# Universo de discurso para la velocidad angular
wmax = 100
vel = np.arange(-wmax, wmax, dt)
# Funciones de pertenencia para la velocidad angular
WNG = trapmf(vel, [-wmax, -wmax, -wmax/2, -wmax/4])
WNP = trimf(vel, [-wmax/2, -wmax/4, 0])
WC = trimf(vel, [-wmax/4, 0, wmax/4])
WPP = trimf(vel, [0, wmax/4, wmax/2])
WPG = trapmf(vel, [wmax/4, wmax/2, wmax, wmax])
W=[WNG,WNP,WC,WPP,WPG]
W=np.array(W)
# Universo de discurso para la Fuerza
fmax = 300
f = np.arange(-fmax, fmax, dt)
# Funciones de pertenencia para la Fuerza
FNG = trapmf(f, [-fmax, -fmax, -fmax/2, -fmax/4])
FNP = trimf(f, [-fmax/2, -fmax/4, 0])
FC = trimf(f, [-fmax/4, 0, fmax/4])
FPP = trimf(f, [0, fmax/4, fmax/2])
FPG = trapmf(f, [fmax/4, fmax/2, fmax, fmax])
F=[FNG,FNP,FC,FPP,FPG]
F=np.array(F)

fza = 0        
thet =pos0
v = vel0
a = acel0
# Simular
y = []
x = np.arange(0, t_final, dt)
for t in x:
  a = calcula_aceleracion(thet, v, fza)
  v = v + a * dt
  
  thet = thet + v * dt + a * np.power(dt, 2) / 2  
  #print(np.round((thet*180)/np.pi,decimals=2))
  y.append(thet)  
  fuzzT=fuzzificar(A,theta,np.round((thet*180)/np.pi,decimals=2))
  fuzzW=fuzzificar(W,vel,np.round(v,decimals=2))
    #Reglas de inferencia
  R1=min(fuzzT[0],fuzzW[0]) #regla 1 theta es NG Y w es NG entonces F es NG
  R2=min(fuzzT[1],fuzzW[0]) #regla 2 theta es NP Y w es NG entonces F es NG
  R3=min(fuzzT[2],fuzzW[0]) #regla 3 theta es Z Y w es NG entonces F es NG
  R4=min(fuzzT[0],fuzzW[1]) #regla 4 theta es NG Y w es NP entonces F es NG
  R5=min(fuzzT[1],fuzzW[1]) #regla 5 theta es NP Y w es NP entonces F es NG
  R6=min(fuzzT[0],fuzzW[2]) #regla 6 theta es NG Y w es Z entonces F es NG

  R7=min(fuzzT[3],fuzzW[0]) #regla 7 theta es PP Y w es NG entonces F es NP
  R8=min(fuzzT[2],fuzzW[1]) #regla 8 theta es Z Y w es NP entonces F es NP
  R9=min(fuzzT[1],fuzzW[2]) #regla 9 theta es NP Y w es Z entonces F es NP
  R10=min(fuzzT[0],fuzzW[3]) #regla 10 theta es NG Y w es PP entonces F es NP

  R11=min(fuzzT[4],fuzzW[0]) #regla 11 theta es PG Y w es NG entonces F es Z
  R12=min(fuzzT[3],fuzzW[1]) #regla 12 theta es PP Y w es NP entonces F es Z
  R13=min(fuzzT[2],fuzzW[2]) #regla 13 theta es Z Y w es Z entonces F es Z
  R14=min(fuzzT[1],fuzzW[3]) #regla 14 theta es NP Y w es PP entonces F es Z
  R15=min(fuzzT[0],fuzzW[4]) #regla 15 theta es NG Y w es PG entonces F es Z

  R16=min(fuzzT[4],fuzzW[1]) #regla 16 theta es PG Y w es NP entonces F es PP
  R17=min(fuzzT[3],fuzzW[2]) #regla 17 theta es PP Y w es Z entonces F es PP
  R18=min(fuzzT[2],fuzzW[3]) #regla 18 theta es Z Y w es PP entonces F es PP
  R19=min(fuzzT[1],fuzzW[4]) #regla 19 theta es NP Y w es PG entonces F es PP

  R20=min(fuzzT[4],fuzzW[2]) #regla 20 theta es PG Y w es Z entonces F es PG
  R21=min(fuzzT[4],fuzzW[3]) #regla 21 theta es PG Y w es PP entonces F es PG
  R22=min(fuzzT[4],fuzzW[4]) #regla 22 theta es PG Y w es PG entonces F es PG
  R23=min(fuzzT[3],fuzzW[3]) #regla 23 theta es PP Y w es PP entonces F es PG
  R24=min(fuzzT[3],fuzzW[4]) #regla 14 theta es PP Y w es PG entonces F es PG
  R25=min(fuzzT[2],fuzzW[4]) #regla 14 theta es Z Y w es PG entonces F es PG

  F1=cortarF(R1,FNG)
  F2=cortarF(R2,FNG)
  F3=cortarF(R3,FNG)
  F4=cortarF(R4,FNG)
  F5=cortarF(R5,FNG)
  F6=cortarF(R6,FNG)
  F7=cortarF(R7,FNP)
  F8=cortarF(R8,FNP)
  F9=cortarF(R9,FNP)
  F10=cortarF(R10,FNP)
  F11=cortarF(R11,FC)
  F12=cortarF(R12,FC)
  F13=cortarF(R13,FC)
  F14=cortarF(R14,FC)
  F15=cortarF(R15,FC)
  F16=cortarF(R16,FPP)
  F17=cortarF(R17,FPP)
  F18=cortarF(R18,FPP)
  F19=cortarF(R19,FPP)

  F20=cortarF(R20,FPG)
  F21=cortarF(R21,FPG)
  F22=cortarF(R22,FPG)
  F23=cortarF(R23,FPG)
  F24=cortarF(R24,FPG)
  F25=cortarF(R25,FPG)
    #Salida Borrosa
  Fr=union([F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,F13,F14,F15,F16,F17,F18,F19,F20,F21,F22,F23,F24,F25])
    #Desborrosificacion------>pasamos del mundo borroso al mundo nitido
  fza=defuzz(f,Fr,'bisector')
  #print(fza)
grafica(x,y,dt,r'$\theta$[rad]','posicion')