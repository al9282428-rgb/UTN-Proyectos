#TADReserva.py (Uriel Sebastian Lallana)

#VALIDACIONES

#Se usa el bloque Try-except para que el programa no se rompa y aparezca un error en caso de que el usuario ingrese algo no relacionado con lo que se pide
#Valida que la entrada tenga formato ´HH:MM´ y que no ingresen un numero al azar
def validarHora(hora):
    try:
        h, m = hora.split(":")
        if 0 <= int(h) < 24 and 0 <= int(m) < 60:
            return True
        else:
            print("Error: Hora inválida. Debe estar entre 00:00 y 23:59.")
            return False
    except:
        print("Error: Formato de hora inválido. Use hora/minuto.")
        return False
#Valida el formato ´DD/MM/AAAA´ y asegura que los componentes sean convertidas a enteros
def validarFecha(fecha):
    try:
        d, m, a = fecha.split("/")
        if 1 <= int(d) <= 31 and 1 <= int(m) <= 12 and int(a) >= 2026:
            return True
        else:
            print("Error: Fecha inválida. Revise dia, mes y año.")
            return False
    except:
        print("Error: Formato de fecha inválido. Use dia/mes/año")
        return False


#CONSTRUCTOR
#Crea la reserva y verifica que no hayan ingresado un espacio vacio
def crearReserva(actividad, prioridad, fecha, hora):
    if not actividad.strip():
        print("Error: la actividad no puede estar vacía.")
        return None
    if not fecha.strip():
        print("Error: la fecha no puede estar vacía.")
        return None
    if not hora.strip():
        print("Error: la hora no puede estar vacía.")
        return None

    if not validarFecha(fecha) or not validarHora(hora):
        return None
#validacion de prioridad Normal, Tocio, Torneo, si el usuario ingresa la palabra sin mayuscula o con un espacio, se agrega automaticamente
    prio_validas = ["Normal", "Socio", "Torneo"]
    prio_mejor = prioridad.strip().capitalize()
#En el caso de que no se escriba una prioridad valida, se asigna automaticamente a Normal
    if prio_mejor not in prio_validas:
        print("Prioridad inválida, se asignó 'Normal'.")
        prio_final = "Normal"
    else:
        prio_final = prio_mejor

    return [actividad.strip(), prio_final, fecha.strip(), hora.strip()]


#Funciones de VER, en el caso de que no escriban nada, aparece el mensaje de error y se retorna

def verActividad(reserva):
    if reserva is None:
        print("Error: reserva inexistente.")
        return None
    return reserva[0]

def verPrioridad(reserva):
    if reserva is None:
        print("Error: reserva inexistente.")
        return None
    return reserva[1]

def verFecha(reserva):
    if reserva is None:
        print("Error: reserva inexistente.")
        return None
    return reserva[2]

def verHora(reserva):
    if reserva is None:
        print("Error: reserva inexistente.")
        return None
    return reserva[3]


#Funciones de MODIFICAR, en el caso de que no se escriba nada, aparece el mensaje de error, al igual de que si ponen una actividad incorrecta, prioridad, fecha y hora
#En el caso de fecha y hora, se valida para que este correcto, una vez hecho aparece un mensaje que se modifico correctamente 

def modActividad(reserva, nueva_act):
    if reserva is None:
        print("Error: reserva inexistente.")
        return
    if not nueva_act.strip():
        print("Error: actividad inválida.")
        return
    
    reserva[0] = nueva_act.strip()
    print("Actividad modificada correctamente.")

def modPrioridad(reserva, nueva_prio):
    if reserva is None:
        print("Error: reserva inexistente.")
        return

    prio_cambiada = nueva_prio.strip().capitalize()
    if prio_cambiada in ["Normal", "Socio", "Torneo"]:
        reserva[1] = prio_cambiada
        print("Prioridad modificada correctamente.")
    else:
        print("Error: prioridad inválida.")

def modFecha(reserva, nueva_fec):
    if reserva is None:
        print("Error: reserva inexistente.")
        return

    if validarFecha(nueva_fec):
        reserva[2] = nueva_fec.strip()
        print("Fecha modificada correctamente.")

def modHora(reserva, nueva_h):
    if reserva is None:
        print("Error: reserva inexistente.")
        return

    if validarHora(nueva_h):
        reserva[3] = nueva_h.strip()
        print("Hora modificada correctamente.")
