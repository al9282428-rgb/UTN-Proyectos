# Import de los módulos (TADs)
from TADreserva import *
from TADcola import *
from TADprocesos import *
from TADagenda import *

# ==========================================
# FUNCIONES DE INTERFAZ Y VALIDACIÓN
# ==========================================

# Esta función pide un número al usuario que se usa en el menú.
# Usa un bloque try-except para evitar que el programa se rompa si el usuario ingresa algo que no es un número entero.
# Se repite en bucle hasta que el número ingresado esté dentro del rango permitido (minimo, maximo).

def leerEntero(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Error: Por favor ingrese un número entre {minimo} {maximo}.")
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un número entero.")


# Esta es una funcion simple para mostrar el menú principal del programa, se llama cada vez que se necesita mostrar las opciones al usuario.

def mostrarMenu():
    print("\n" + "="*40)
    print("  GESTIÓN DE COMPLEJO DEPORTIVO")
    print("="*40)
    print("1. Alta de Reserva")
    print("2. Modificación de Reserva")
    print("3. Cancelación de Reserva")
    print("4. Listado General de Reservas")
    print("5. Reorganización y Depuración (Mantenimiento)")
    print("6. Generación de Hoja de Ruta (Maestranza)")
    print("0. Salir del Sistema")
    print("="*40)

# ==========================================
# BUCLE PRINCIPAL DEL PROGRAMA
# ==========================================

def main():
    # Se inicializa la estructura de la agenda utilizando el constructor del TAD Agenda.
    # Este objeto 'mi_agenda' funciona como el contenedor principal donde se guardan todas las reservas.
    mi_agenda = crearAgenda()
    
    opcion = -1
    
    while opcion != 0:
        mostrarMenu()
        opcion = leerEntero("Seleccione una opción: ", 0, 6)
        
        if opcion == 1:
            # Opcion 1: Registro de nuevos turnos en el sistema.
            print("\n--- ALTA DE RESERVA ---")
            act = input("Ingrese Actividad (Ej: fútbol 5, tenis, cumpleaños, etc): ")
            prio = input("Ingrese Prioridad (Normal/Socio/Torneo): ")
            fec = input("Ingrese Fecha (DD/MM/AAAA): ")
            hor = input("Ingrese Hora de Inicio (HH:MM): ")
            
            # El TAD reservas empaqueta los datos en una estructura de reserva.
            nueva_reserva = crearReserva(act, prio, fec, hor)
            
            if nueva_reserva is not None:
                # Se utiliza la función del TAD Agenda para insertar la reserva en la agenda.
                # El TAD Agenda valida internamente que no se repitan la fecha y la hora.
                if agregarReserva(mi_agenda, nueva_reserva):
                    print("¡Reserva guardada con éxito!")
                
        elif opcion == 2:
            # Opcion 2: Actualización de datos de un turno que ya existe en la agenda.
            print("\n--- MODIFICACIÓN DE RESERVA ---")
            fec_orig = input("Ingrese Fecha del turno a modificar: ")
            hor_orig = input("Ingrese Hora del turno a modificar: ")
            
            # Se busca si el turno existe en la agenda antes de pedir los nuevos datos.
            res_encontrada = buscarReserva(mi_agenda, fec_orig, hor_orig)
            
            if res_encontrada:
                print("Turno encontrado. Deje en blanco lo que NO desee cambiar.")
                n_act = input("Nueva Actividad: ") or None
                n_prio = input("Nueva Prioridad: ") or None
                n_fec = input("Nueva Fecha: ") or None
                n_hor = input("Nueva Hora: ") or None
                
                # Se llama a la función del TAD Agenda para aplicar los cambios sobre la reserva encontrada.
                # Si se cambia fecha u hora, el sistema verifica que el nuevo horario no esté ocupado.
                if modificarReserva(mi_agenda, fec_orig, hor_orig, n_act, n_prio, n_fec, n_hor):
                    print("Cambios aplicados correctamente.")
            else:
                print("No se encontró ninguna reserva en ese horario.")

        elif opcion == 3:
            # Opcion 3: Eliminación definitiva de un turno específico del sistema.
            print("\n--- CANCELACIÓN DE RESERVA ---")
            fec_baja = input("Fecha del turno a cancelar (DD/MM/AAAA): ")
            hor_baja = input("Hora del turno a cancelar (HH:MM): ")
            
            # Se solicita al TAD Agenda que elimine la entrada que coincida con la fecha y hora.
            if cancelarReserva(mi_agenda, fec_baja, hor_baja):
                print("La reserva ha sido eliminada del sistema.")
            else:
                print("Error: No se pudo realizar la baja (verifique los datos ingresados).")

        elif opcion == 4:
            # Opcion 4: Visualización de todos los turnos almacenados en la lista de la agenda.
            print("\n--- LISTADO GENERAL DE RESERVAS ---")
            # Se usa la función del TAD Agenda para saber cuántos elementos hay que recorrer.
            cant = tamanioAgenda(mi_agenda)
            
            if cant == 0:
                print("La agenda está vacía actualmente.")
            else:
                # Se itera la agenda recuperando cada reserva por su índice de posición.
                for i in range(1, cant + 1):
                    res = recuperarReserva(mi_agenda, i)
                    # Se muestran los datos usando las funciones 'ver' del TAD de Uriel.
                    print(f"{i}. [{verPrioridad(res)}] {verActividad(res)} - {verFecha(res)} {verHora(res)}")

        elif opcion == 5:
            # Opcion 5: Submenú para procesos masivos (mover fechas por lluvia o borrar días enteros)
            print("\n--- MANTENIMIENTO ---")
            print("1. Traslado por lluvia")
            print("2. Limpiar un día completo")
            sub_op = leerEntero("Elija una opción: ", 1, 2)   
            # Aca arriba uso de nuevo la funcion segura para leer la opcion del sub-menu sin que rompa el programa
            
            if sub_op == 1:
                fec_orig = input("Fecha a trasladar (DD/MM/AAAA): ")
                fec_dest = input("Nueva fecha de destino (DD/MM/AAAA): ")
                
                # Se ejecuta el proceso masivo del TAD agenda sobre la propia agenda.
                trasladarPorLluvia(mi_agenda, fec_orig, fec_dest)
            elif sub_op == 2:
                fec_limpia = input("Fecha a limpiar completamente (DD/MM/AAAA): ")
                # Se eliminan todas las reservas que coincidan con la fecha indicada.
                limpiarCalendario(mi_agenda, fec_limpia)

        elif opcion == 6:
            # Opcion 6: Creación de una Cola de trabajo para el personal de mantenimiento.
            print("\n--- GENERAR HOJA DE RUTA ---")
            fec_ruta = input("Ingrese la fecha para maestranza: ")
            
            # Se genera la estructura de Cola filtrando por la fecha elegida.
            cola_ruta = generarHojaDeRuta(mi_agenda, fec_ruta)
            
            if cola_ruta and not esVacia(cola_ruta):
                print(f"\nTAREAS PROGRAMADAS PARA EL DÍA {fec_ruta}:")
                # Se procesa la Cola mostrando las tareas en el orden en que fueron cargadas (FIFO).
                while not esVacia(cola_ruta):
                    tarea = desencolar(cola_ruta) 
                    print(f"-> Preparar {tarea[0]} (Prioridad: {tarea[1]})")

    print("Saliendo del sistema...")

if __name__ == "__main__":
    main()
