/*Ejecutar con Ctrl+shift+P -> Prolog:load document*/

/* Ejercicio 1 Tp : Sistema Experto para revision y mantenimiento de valvula de Gas*/

/* Axiomas (invariantes del dominio) */
/* Rama Izquierda*/
/*'Verificar si el espesor de la valvula de seguridad es menor al umbral requerido'*/
verificar(thinckness_of_the_safety_valve_body) :- 
    estado(thinckness_of_the_safety_valve_body, yes), 
    writeln('El estado del equipo debe ser reportado para una inspeccion tecnica de la unidad inmediatamente'),
    !;

    estado(thinckness_of_the_safety_valve_body, no),
    writeln('El estado del equipo es aceptable '),
    !;

    estado(thinckness_of_the_safety_valve_body, desconocido),
    verificar(safety_valve_body_has_deffect_of_dazzling_and_rusting).
               
/*¿El cuerpo de la válvula de seguridad, tiene defectos?*/
verificar(safety_valve_body_has_deffect_of_dazzling_and_rusting) :-
    estado(safety_valve_body_has_deffect_of_dazzling_and_rusting, yes),
    writeln('Se requiere coordinacion para renderizar y colorear el equipo'),
    !;

    estado(safety_valve_body_has_deffect_of_dazzling_and_rusting, no),
    writeln('Verificar si el espesor de la valvula de seguridad es menor al umbral requerido'),
    !;
                
    estado(safety_valve_body_has_deffect_of_dazzling_and_rusting, desconocido), 
    writeln('Verificar el cuerpo de la valvula de seguridad ').

/*  Rama Derecha    */
/* ¿la fuga se arregla con la llave? */
verificar(leakage_fixed_with_the_wrench) :- 
    estado(leakage_fixed_with_the_wrench, yes),
    writeln('Reportar que ha sido reparado'),
    !;

    estado(leakage_fixed_with_the_wrench, no),
    writeln('Enviar un reporte al departamento de reparaciones para arreglar la falla'),
    !;
   
    estado(leakage_fixed_with_the_wrench, desconocido),
    verificar(gas_leakage_at_joint).

/*¿Hay una fuga de gas en las juntas?*/
verificar(gas_leakage_at_joint) :- 
    estado(gas_leakage_at_joint, no), 
    writeln('La valvula no tiene perdidas de gas'),
    !;

    estado(gas_leakage_at_joint, yes),
    writeln('Verificar si la fuga puede repararse con la llave '),
    !;

    estado(gas_leakage_at_joint, desconocido), 
    writeln('Verificar si hay fuga de gas en las juntas ').

/*  Rama Central Izquierda   */
/*El piloto trabaja de forma apropiada*/
verificar(piloto) :- 
    estado(piloto, yes), 
    writeln('Colocar la valvula de seguridad de acuerdo con las instrucciones'),
    !;

    estado(piloto, no),
    writeln('Realizar un reparacion completa del piloto y reinstalarlo'),
    !;

    estado(piloto, desconocido),
    verificar(leakage_prevention_between_sit_and_orifice).

/*¿Existe una prevención de fugas adecuada?*/
verificar(leakage_prevention_between_sit_and_orifice) :- 
    estado(leakage_prevention_between_sit_and_orifice, yes),
    writeln('Verificar Pilot'),
    !;

    estado(leakage_prevention_between_sit_and_orifice, no),
    writeln('Reemplazar el asiento y el orificio, y colocar la valvula de seguridad'),
    !;

    estado(leakage_prevention_between_sit_and_orifice, desconocido), 
    verificar(safety_valve_spring).

/*Buen desempeño de la valvula de seguridad*/
verificar(safety_valve_spring) :- 
    estado(safety_valve_spring, yes),
    writeln('Verificar seguridad contra fugas'),
    !;

    estado(safety_valve_spring, no),
    writeln('Reparar o cambiar valvula de seguridad'),
    !;

    estado(safety_valve_spring, desconocido),
    verificar(control_valve_sensors_blocked).

/*Estan los sensores de control bloqueados*/
verificar(control_valve_sensors_blocked) :- 
    estado(control_valve_sensors_blocked, yes),
    writeln('Reparar o cambiar los sensores'),
    !;

    estado(control_valve_sensors_blocked, no),
    writeln('Verificar el estado de la valvula de seguridad'),
    !;

    estado(control_valve_sensors_blocked, desconocido),
    verificar(valve_status_closed).
                
/*la valvula esta cerrada*/
verificar(valve_status_closed) :- 
    estado(valve_status_closed, yes),
    writeln('Se debe abrir la valvula'),
    !;

    estado(valve_status_closed, no),
    writeln('Verificar si los sensores estan bloqueados'),
    !;

    estado(valve_status_closed, desconocido),
    verificar(relief_valve_ok_with_10_percent_more_pressure).
                
/*¿La válvula funciona correctamente con un aumento de presión del 10% más que la presión regular?*/
verificar(relief_valve_ok_with_10_percent_more_pressure) :- 
    estado(relief_valve_ok_with_10_percent_more_pressure, yes),
    writeln('La funcion de seguridad es apropiada'),
    !;

    estado(relief_valve_ok_with_10_percent_more_pressure, no),
    writeln('Verificar si la valvula esta cerrada'),
    !;

    estado(relief_valve_ok_with_10_percent_more_pressure, desconocido),
    verificar(safety_valve_has_continuous_evacuation).
            
/*Rama central derecha*/
/*Fuga prevenible entre asiento y orificio?*/
verificar(preventable_leakage) :- 
    estado(preventable_leakage, yes),
    writeln('Colocar la valvula de seguridad'),
    !;

    estado(preventable_leakage, no),
    writeln('Reemplazar el asiento y orificio, y poner la valvula'),
    !;

    estado(preventable_leakage, desconocido),
    verificar(safety_spring).

/*El resorte es eficiente?*/
verificar(safety_spring) :- 
    estado(safety_spring, yes),
    writeln('Verificar si hay una fuga prevenible entre el asiento y el orificio'),
    !;

    estado(safety_spring, no),
    writeln('Reemplazar el resorte de seguridad'),
    !;

    estado(safety_spring, desconocido),
    verificar(sensors_blocked).

/*Los sensores estan bloqueados?*/
verificar(sensors_blocked) :- 
    estado(sensors_blocked, yes),
    writeln('Limpiar y arreglar las fallas de los sensores'),
    !;

    estado(sensors_blocked, no),
    writeln('Verificar si el resorte de seguridad es efectivo'),
    !;

    estado(sensors_blocked, desconocido),
    verificar(line_pressure_appropriate).

/*La presion de linea es apropiada?*/
verificar(line_pressure_appropriate) :- 
    estado(line_pressure_appropriate, yes),
    writeln('Verificar controlador y sensores'),
    !;

    estado(line_pressure_appropriate, no),
    writeln('Ajustar el regulador'),
    !;

    estado(line_pressure_appropriate, desconocido),
    verificar(safety_valve_has_continuous_evacuation).

/*Interseccion de Rama central izquierda y derecha*/
/*La valvula tiene evacuacion de gas continua?*/
verificar(safety_valve_has_continuous_evacuation) :-
    estado(safety_valve_has_continuous_evacuation, yes),
    writeln('Verificar si la linea de gas tiene una presion apropiada'),
    !;

    estado(safety_valve_has_continuous_evacuation, no),
    writeln('Verificar si la valvula funciona bien al aumentar un 10% la presion'),
    !; 

    estado(safety_valve_has_continuous_evacuation, desconocido),
    writeln('Verificar si la valvula de seguridad tiene una evacuacion de gas continua').




/* Ground Facts de instancia variables (podrian resolverse mediante sensado o agregando la informacion interactivamente a la base de conocimientos) */
/* Rama Izquierda*/
estado(thinckness_of_the_safety_valve_body, desconocido).
estado(safety_valve_body_has_deffect_of_dazzling_and_rusting, desconocido).
/* Rama Derecha*/
estado(leakage_fixed_with_the_wrench,desconocido).
estado(gas_leakage_at_joint,desconocido).
/*  Rama Central Izquierda   */
estado(piloto, desconocido).
estado(leakage_prevention_between_sit_and_orifice, desconocido).
estado(safety_valve_spring, desconocido).
estado(control_valve_sensors_blocked, desconocido).
estado(valve_status_closed, desconocido).
estado(relief_valve_ok_with_10_percent_more_pressure, desconocido).
/*  Rama Central derecha*/
estado(preventable_leakage,desconocido).
estado(safety_spring,desconocido).
estado(sensors_blocked,desconocido).
estado(line_pressure_appropriate,desconocido).
/*Interseccion de ramas centrales*/
estado(safety_valve_has_continuous_evacuation, desconocido).