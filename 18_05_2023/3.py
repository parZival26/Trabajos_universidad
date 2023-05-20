import csv, shutil, os # Se importan las librerias necesarias
from prettytable import PrettyTable


class Tarea: # Se crea la clase Tarea
    last_id = 0 # Se crea un atributo de clase para el id

    def __init__(self, nombre, fecha): # Se crea el constructor de la clase
        Tarea.last_id +=1 # Se le suma 1 al atributo de clase
        self.id = Tarea.last_id # Se le asigna el valor del atributo de clase al atributo de instancia
        self.nombre = nombre
        self.fecha = fecha
        self.completada = False

def continuar(texto="Desea continuar S/N: "): # Se crea una funcion por si el usuario desea continuar la cual se ejecuta de forma infinita hasta que el usuario elija una opcion valida
    while True:
        opcion = input(texto).lower()
        if opcion == 's':
            return True
        elif opcion == 'n':
            return False
        else:
            continue


def clean(): # Funcion para limpiar la terminal tanto en widows como en linux usado la libreria OS
    os.system('cls')
    os.system('clear')

def save_tareas(tarea): # Funcion para guardar las tareas en un archivo csv
    existe_archivo = os.path.isfile('tareas.csv') # Se analiza si existe el archivo csv
    ultimo_id = 0 # Se crea una variable para guardar el ultimo id

    if existe_archivo: # Si existe el archivo se analiza el ultimo id
        with open('tareas.csv', mode="r") as archivo_csv: # Se abre el archivo en modo lectura
            reader = csv.DictReader(archivo_csv) # Se crea un objeto reader
            for fila in reader: # Se recorre el objeto reader
                tarea_id = int(fila["ID"])# Se guarda el id de la fila
                ultimo_id = max(ultimo_id, tarea_id)# Se analiza cual es el ultimo id

    with open('tareas.csv', mode="a", newline="") as archivo_csv: # Se abre el archivo en modo append
        writer = csv.writer(archivo_csv) # Se crea un objeto writer

        if not existe_archivo: # Si no existe el archivo se crea el encabezado
            encabezados = ["ID", "Nombre", "Fecha", "Completada"] # Se crea una lista con los encabezados
            writer.writerow(encabezados) # Se escribe el encabezado en el archivo

        nuevo_id = ultimo_id + 1 # Se crea un nuevo id
        writer.writerow([nuevo_id, tarea.nombre, tarea.fecha, tarea.completada]) # Se escribe la tarea en el archivo



def show_tareas(): # Funcion para mostrar las tareas en una tabla
    with open('tareas.csv', mode="r") as archivo_csv: # Se abre el archivo en modo lectura
        reader = csv.reader(archivo_csv) # Se crea un objeto reader para leer el archivo
        encabezados = next(reader)  # Se guarda el encabezado en una variable
        tabla = PrettyTable(encabezados) # Se crea una tabla con los encabezados

        for fila in reader: # Se recorre el objeto reader
            tabla.add_row(fila) # Se agrega la fila a la tabla

        print(tabla)    # Se imprime la tabla


def delete_tarea(id_tarea): # Funcion para eliminar una tarea
    archivo_temporal = 'tareas.csv' + ".temp" # Se crea un archivo temporal para guardar los datos

    with open('tareas.csv', mode="r") as archivo_csv, open(archivo_temporal, mode="w", newline="") as temp_csv: # Se abre el archivo en modo lectura y el archivo temporal en modo escritura
        reader = csv.DictReader(archivo_csv) # Se crea un objeto reader
        encabezados = reader.fieldnames # Se guarda el encabezado en una variable
        writer = csv.DictWriter(temp_csv, fieldnames=encabezados) # Se crea un objeto writer con los encabezados
        writer.writeheader() # Se escribe el encabezado en el archivo

        for fila in reader: # Se recorre el objeto reader
            if fila["ID"] != str(id_tarea): # Si el id de la fila es diferente al id de la tarea a eliminar se escribe en el archivo temporal
                writer.writerow(fila) # Se escribe la fila en el archivo temporal

    shutil.move(archivo_temporal, 'tareas.csv') # Se mueve el archivo temporal al archivo original sobreescribiendolo y se usa la libreia shutil para mover el archivo

def update_tarea(id_tarea, nuevos_datos): # Funcion para actualizar una tarea
    archivo_temporal = 'tareas.csv' + ".temp" # Se crea un archivo temporal para guardar los datos
 
    with open('tareas.csv', mode="r") as archivo_csv, open(archivo_temporal, mode="w", newline="") as temp_csv: # Se abre el archivo en modo lectura y el archivo temporal en modo escritura
        reader = csv.DictReader(archivo_csv) # Se crea un objeto reader
        encabezados = reader.fieldnames # Se guarda el encabezado en una variable
        writer = csv.DictWriter(temp_csv, fieldnames=encabezados) # Se crea un objeto writer con los encabezados
        writer.writeheader() # Se escribe el encabezado en el archivo

        for fila in reader: # Se recorre el objeto reader
            if fila["ID"] == str(id_tarea): # Si el id de la fila es igual al id de la tarea a modificar se actualiza la fila
                fila.update(nuevos_datos) # Se actualiza la fila
            writer.writerow(fila) # Se escribe la fila en el archivo temporal

    shutil.move(archivo_temporal, 'tareas.csv')  # Se mueve el archivo temporal al archivo original sobreescribiendolo y se usa la libreia shutil para mover el archivo


if __name__ == '__main__':
    while True: # Se crea un ciclo infinito para que el programa se ejecute hasta que el usuario lo desee
        clean() # Se limpia la terminal
        opcion = int(input("""
Bienvenido a tus tareas, por favor seleccione una opcion:
1. Ver tareas
2. Agregar tarea
3. Eliminar tarea
4. Editar tarea
5. Salir

: """)) # Se pide al usuario que ingrese una opcion
        if opcion == 1: # Se analiza la opcion
            clean()
            show_tareas() # Se muestran las tareas
            if continuar(): continue # si se desea continuar o terminar el programa
            else: break

        elif opcion == 2:
            clean() # Se limpia la terminal
            nombre = input("Ingrese el nombre de la tarea: ") # Se pide al usuario el nombre y la fecha de la tarea
            fecha = input("Ingrese la fecha de entrega: ")
            tarea = Tarea(nombre, fecha) # Se crea un objeto tarea
            save_tareas(tarea) # Se guarda la tarea en el archivo csv
            show_tareas() # Se muestran las tareas
            if continuar(): continue # si se desea continuar o terminar el programa
            else: break

        elif opcion == 3:
            clean()
            show_tareas() # Se muestran las tareas
            id_del = int(input("Ingresa el Id de la tarea a eliminar: ")) # Se pide al usuario el id de la tarea a eliminar
            if continuar(f"Esta seguro de eliminar la tarea {id_del}  S/N: "): # Se pide confirmacion para eliminar la tarea
                delete_tarea(id_del) # Se elimina la tarea
                clean()
                show_tareas() # Se muestran las tareas
                if continuar(): continue # si se desea continuar o terminar el programa
                else: break
            else: continue

        elif opcion == 4: # Se pide al usuario el id de la tarea a modificar y los nuevos datos
            clean()
            show_tareas() # Se muestran las tareas
            id_modif = int(input("Ingrese el ID de la tarea que desea modificar: ")) # Se pide al usuario el id de la tarea a modificar
            nuevos_datos = {
            "Nombre": input("Ingrese el nombre de la tarea: "),
            "Fecha": input("Ingrese la Fecha de la taera: "),
            "Completada": continuar("La tarea ya esta completada S/N: ")} # Se pide al usuario los nuevos datos
            update_tarea(id_modif, nuevos_datos) # Se actualiza la tarea
            show_tareas() # Se muestran las tareas
            if continuar(): continue # si se desea continuar o terminar el programa
            else: break

        elif opcion == 5: # Si la opcion es 5 se termina el programa
            break 