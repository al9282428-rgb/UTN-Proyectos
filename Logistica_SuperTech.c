/*
El centro de distribución “SuperTech” en Berazategui realiza envío de accesorios gamer a pequeños negocios en CABA y en La Plata. Estos equipos son: Auriculares, mouse y teclado. Los pedidos son embalados, etiquetados y apilados en el galpón, el día anterior, con la siguiente información:
•	Dni del cliente
•	Zona de entrega (La Plata o CABA)
•	Código del producto que contiene (1- Teclado, 2-Mouse, 3-Auricular)
Por la mañana llegan 2 camionetas y el encargado debe desarmar esa pila que le dejaron y acomodar en cada vehículo según la zona de entrega.
El programa debe ofrecer el siguiente menú:
1-Registrar caja en el galpón (apilar con los datos mencionados)
2-Cargar camionetas (sacar caja de la pila y cargarla en la camioneta considerando la zona de entrega. Tener en cuenta estructuras para llevar la info de cada camioneta)
3-Mostrar cantidad de pedidos cargados por zona de entrega (indicar cuántas cajas fueron cargadas en cada camioneta hasta el momento)
4-Total por tipo de producto: Calcular y mostrar de forma recursiva el total de pedidos que se cargaron por tipo de producto (Teclado, Mouse y Auricular)
5-Salir
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
   int dni;
   char zona[50];
   int codigo;
}caja;

typedef struct NodoPila {
   caja dato;
   struct NodoPila* sig;
} NodoPila;

typedef struct {
    NodoPila* p;
} Pila;

void inicializarPila(Pila* pila){
    pila->p = NULL;
}

typedef struct Camion{
    caja dato;
    struct Camion* sig;
}Camion;

void apilar(NodoPila** pila, caja dato){
    NodoPila* nuevo = malloc(sizeof(NodoPila));
    nuevo->dato = dato;
    nuevo->sig = *pila;
    *pila = nuevo;
}

void desapilar(NodoPila** pila, caja* dato){
    NodoPila* aux = *pila;
    *dato = aux->dato;
    *pila = aux->sig;
    free(aux);
}

void insAlPio(Camion** camion, caja dato){
    Camion* nuevo = malloc(sizeof(Camion));
    nuevo->dato = dato;
    nuevo->sig = *camion;
    *camion = nuevo;
}

void registrarCaja(NodoPila** pila){
    printf("Carga de datos \n");
    
    caja dato;

    printf("Ingresar DNI: \n");
    scanf("%d", &dato.dni);

    do{
    printf("Ingresar zona de entrega l(la plata) o c(CABA): \n");
    scanf("%s", dato.zona);
    }while(strcmp(dato.zona, "l") != 0 && strcmp(dato.zona, "c") != 0);

    do{
    printf("Ingresar contenido del paquete(1-teclado, 2-mouse, 3-auricular): \n");
    scanf("%d", &dato.codigo);
    }while(dato.codigo < 1 || dato.codigo > 3);

    apilar(pila, dato);
}

void cargarCaja(NodoPila** pila, Camion** camionLP, Camion** camionCB, int* cantLP, int* cantCB){
    if(*pila == NULL){
        printf("no hay cajas para cargar");
        return;
    }

    caja dato;
    desapilar(pila, &dato);

    if(strcmp(dato.zona, "l") == 0){
        insAlPio(camionLP, dato);
        (*cantLP)++;
    }else{
        insAlPio(camionCB, dato);
        (*cantCB)++;
    }

}

void acumularRecu(Camion* camion, int* acumTeclado, int* acumMouse, int* acumAuris){
    if(camion != NULL){
        switch(camion->dato.codigo){
            case 1: (*acumTeclado)++; break;
            case 2: (*acumMouse)++; break;
            case 3: (*acumAuris)++; break;
        }
        acumularRecu(camion->sig, acumTeclado, acumMouse, acumAuris);
    }
}

int main(){
    Camion* camionLP = NULL;
    Camion* camionCB = NULL;
    Pila pila;

    inicializarPila(&pila);
    int cantidadLP = 0, cantidadCB = 0;
    int acumuladorT, acumuladorM, acumuladorA;
    int opcion;

    do{
       printf("---MENU---\n\n");

       printf("1-Registrar caja \n");
       printf("2-Cargar caja en los camiones \n");
       printf("3-Cajas cargadas hasta el momento \n");
       printf("4-Cantidad de productos cargados por tipo \n");
       printf("5-Salir.\n\n");

       printf("Ingresar opcion: ");
       scanf("%d", &opcion);

       switch(opcion){
        case 1: registrarCaja(&(pila.p)); break;
        case 2: cargarCaja(&(pila.p), &camionLP, &camionCB, &cantidadLP, &cantidadCB); break;
        case 3: printf("Cajas cargadas en el camion de La Plata: %d \n", cantidadLP);
                printf("Cajas cargadas en el camion de CABA: %d \n", cantidadCB);
                break;
        case 4: acumuladorT = 0, acumuladorM = 0, acumuladorA = 0;
                acumularRecu(camionLP, &acumuladorT, &acumuladorM, &acumuladorA);
                acumularRecu(camionCB, &acumuladorT, &acumuladorM, &acumuladorA);
                printf("Cantidad de productos cargados: \n");
                printf("Teclados: %d, Mouse: %d, Auriculares: %d\n",acumuladorT, acumuladorM, acumuladorA);
                break;
        case 5: printf("saliendo...\n"); break;
        default: printf("opcion incorrecta, intente nuevamente\n");
       }
       
    }while(opcion != 5);
    return 0;
}