(define (problem carga2)
  	(:domain aviones)
    (:objects
     	AA01
     	AA02
     	AA03
		AA04
		AA05
		LA01
		LA02
		LA03
		LA04
		LA05
		AEP
		EZE
		RSA
		LUQ
     	PSS
     	MDZ
     	BRC
     	VINO
     	YERBA
		FERTILIZANTE
		SEMILLAS
		SOJA
     	CHOCOLATES
    )
	(:init
     	(avion AA01)
     	(avion AA02)
     	(avion AA03)
		(avion AA04)
		(avion AA05)
		(avion LA01)
		(avion LA02)
		(avion LA03)
		(avion LA04)
		(avion LA05)
     	(carga VINO)
     	(carga YERBA)
     	(carga CHOCOLATES)
		(carga FERTILIZANTE)
		(carga SEMILLAS)
		(carga SOJA)
		(aeropuerto AEP)
		(aeropuerto EZE)
		(aeropuerto LUQ)
		(aeropuerto RSA)
     	(aeropuerto PSS)
     	(aeropuerto MDZ)
     	(aeropuerto BRC)
     	(en CHOCOLATES BRC )
     	(en VINO MDZ)
     	(en YERBA PSS)
		(en SEMILLAS EZE)
		(en SOJA RSA)
		(en FERTILIZANTE AEP)
     	(en AA01 PSS)
     	(en AA02 MDZ)
     	(en AA03 BRC)
		(en AA04 AEP)
		(en AA05 EZE)
		(en LA01 AEP)
		(en LA02 EZE)
		(en LA03 RSA)
		(en LA04 BRC)
		(en LA05 MDZ)
     )
  	(:goal
     	(and
     		(en YERBA BRC)
     		(en CHOCOLATES MDZ)
     		(en VINO PSS)
			(en SEMILLAS RSA)
			(en SOJA AEP)
			(en FERTILIZANTE RSA)
         )
    )
)

