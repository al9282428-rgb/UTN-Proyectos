from TADreserva import*
from TADcola import*

def trasladarPorLluvia(agenda, fecha_origen, fecha_destino):
    #Traslada todas las reservas de una fecha a otra

    #Valida que la nueva fecha tenga un formato correcto
    if not validarFecha(fecha_destino):
        print("Error: La fecha de destino no es válida. Proceso cancelado.")
        return 0

    modificados = 0
    #Recorre la agenda buscando las reservas que coincidan con la fecha de origen
    for reserva in agenda:
        if verFecha(reserva) == fecha_origen:
            modFecha(reserva, fecha_destino)
            modificados += 1
            
    print(f"Traslado completado. Se movieron {modificados} reservas del {fecha_origen} al {fecha_destino}.")
    return modificados


def limpiarCalendario(agenda, fecha_a_limpiar):
    #Elimina todas las reservas correspondientes a un día específico
    
    eliminados = 0
    i = 0
    
    while i < len(agenda):
        reserva = agenda[i]
        
        #Si la fecha coincide, se borra
        if verFecha(reserva) == fecha_a_limpiar:
            del agenda[i]
            eliminados += 1
        else:
            # Si no se borra, pasa a revisar la siguiente posición
            i += 1 
            
    if eliminados > 0:
        print(f"Limpieza completada. Se eliminaron {eliminados} reservas del día {fecha_a_limpiar}.")
    else:
        print(f"No se encontraron reservas para el día {fecha_a_limpiar}.")
        
    return eliminados

def generarHojaDeRuta(agenda, fecha_objetivo):
    #Crea y retorna una nueva Cola que contiene el Nombre de la Actividad y su Nivel de Prioridad de un día específico
    hoja_ruta = crearCola()
    encontrados = 0
    
    for reserva in agenda:
        if verFecha(reserva) == fecha_objetivo:
            
            actividad = verActividad(reserva)
            prioridad = verPrioridad(reserva)
            
            #Agrupa los dos datos en una lista para encolarlos juntos en la hoja de ruta
            datos_turno = [actividad, prioridad]
            encolar(hoja_ruta, datos_turno)
            encontrados += 1
            
    if encontrados == 0:
        print(f"No hay actividades programadas para la hoja de ruta del {fecha_objetivo}.")
    else:
        print(f"Hoja de ruta generada con {encontrados} actividades para el {fecha_objetivo}.")
        
    return hoja_ruta