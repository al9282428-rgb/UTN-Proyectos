from TADreserva import *


# CREACION

def crearAgenda():
    # Crea la agenda vacia
    agenda = []
    return agenda


def AgendaVacia(agenda):
    # Retorna True si la agenda está vacía
    return len(agenda) == 0


def tamanioAgenda(agenda):
    # Retorna la cantidad de reservas guardadas
    return len(agenda)

def agregarReserva(agenda, reserva):
    # Agrega una reserva si no existe otra con la misma fecha y hora
    if reserva is None:
        print("Error: la reserva es inválida.")
        return False

    fecha = verFecha(reserva)
    hora = verHora(reserva)

    if buscarReserva(agenda, fecha, hora) != None:
        print("Error: ya existe una reserva para esa fecha y hora.")
        return False

    agenda.append(reserva)
    return True


# BUSQUEDA / RECUPERACION

def buscarReserva(agenda, fecha, hora):
    # Busca una reserva por fecha y hora
    # Retorna la reserva si la encuentra, o None si no existe
    for reserva in agenda:
        if verFecha(reserva) == fecha and verHora(reserva) == hora:
            return reserva
    return None


def recuperarReserva(agenda, i):
    # Retorna la reserva ubicada en la posición que pida el usuario (se usa i-1)

    pos = i - 1

    if pos < 0 or pos >= len(agenda):
        print("Error: posición inválida.")
        return None

    return agenda[pos]



# ELIMINACION


def cancelarReserva(agenda, fecha, hora):
    # Elimina una reserva específica por fecha y hora
    i = 0
    while i < len(agenda):
        reserva = agenda[i]
        if verFecha(reserva) == fecha and verHora(reserva) == hora:
            del agenda[i]
            return True
        i += 1

    print("Error: no se encontró una reserva con esa fecha y hora.")
    return False


# MODIFICACION


def modificarReserva(agenda, fecha, hora,
                     nueva_actividad,
                     nueva_prioridad,
                     nueva_fecha,
                     nueva_hora):
    # Busca una reserva por fecha y hora y permite modificar uno o varios campos

    reserva = buscarReserva(agenda, fecha, hora)

    if reserva is None:
        print("Error: no se encontró la reserva a modificar.")
        return False

    # Si cambia fecha y/o hora, verificar que no choque con otra reserva
    fecha_final = verFecha(reserva) if nueva_fecha is None else nueva_fecha
    hora_final = verHora(reserva) if nueva_hora is None else nueva_hora

    if fecha_final != fecha or hora_final != hora:
        otra = buscarReserva(agenda, fecha_final, hora_final)
        if otra != None:
            print("Error: ya existe otra reserva con la nueva fecha y hora.")
            return False

    if nueva_actividad is not None:
        modActividad(reserva, nueva_actividad)

    if nueva_prioridad is not None:
        modPrioridad(reserva, nueva_prioridad)

    if nueva_fecha is not None:
        modFecha(reserva, nueva_fecha)

    if nueva_hora is not None:
        modHora(reserva, nueva_hora)

    return True


# LISTADO DE LAS RESERVAS

def listarReservas(agenda):
    # Muestra todas las reservas de la agenda
    if AgendaVacia(agenda):
        print("La agenda está vacía.")
        return

    i = 1
    for reserva in agenda:
        print(f"Reserva {i}:")
        print(f"  Actividad: {verActividad(reserva)}")
        print(f"  Prioridad: {verPrioridad(reserva)}")
        print(f"  Fecha: {verFecha(reserva)}")
        print(f"  Hora: {verHora(reserva)}")
        i += 1
    