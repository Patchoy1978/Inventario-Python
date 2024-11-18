# Importación de la clase 'ProductosAlmacenados' desde el módulo 'prod_almacen' dentro del paquete 'Productos'.
from Productos.prod_almacen import ProductosAlmacenados

# Importación de la clase 'Inventario' desde el módulo 'manejo_inventario' dentro del paquete 'Inventario'.
from Inventario.manejo_inventario import Inventario

# Importación del módulo 'platform' que proporciona una interfaz para interactuar con el sistema operativo.
import platform

# Importación del módulo 'os', que permite interactuar con el sistema operativo, como ejecutar comandos del sistema.
import os

# Clase para limpiar la pantalla de la consola según el sistema operativo
class LimpiarPantalla():
    
    def __init__(self):
        
        # Llama automáticamente al método de limpiar pantalla al instanciar la clase
        self.limpiarpantalla()
        
    def limpiarpantalla(self):
        
        # Detecta el sistema operativo en el que se está ejecutando el programa
        sisop = platform.system()
        
        if sisop == "Windows":
            
            # Comando para limpiar la consola en Windows
            os.system("cls")
        
        else:
            
            # Comando para limpiar la consola en sistemas Unix/Linux/Mac
            os.system("clear")

# Clase que gestiona las operaciones relacionadas con productos heredando de la clase Inventario
class ManejoProductos(Inventario):

    # Método para agregar un nuevo producto al inventario
    def agregar_productos_nuevos(self):
        
        # Solicita al usuario el nombre del producto, ajustando a formato título
        nombre = input("\nIngrese el nombre del Producto: ").title()
        # Solicita al usuario la categoría del producto, ajustando a formato título
        categoria = input("\nIngrese el nombre de la Categoria: ").title()
        
        while True:
        
            try:
                
                # Solicita y convierte a float el precio del producto
                precio = float(input("\nIngrese el Precio del Producto: "))

                # Solicita y convierte a int la cantidad del producto
                cantidad = int(input("\nIngrese La Cantidad del Producto: "))

                # Crea un objeto de tipo ProductosAlmacenados con los datos ingresados
                producto =  ProductosAlmacenados(nombre, categoria, precio, cantidad)
                
                # Llama al método heredado para agregar el producto al inventario
                self.agregar_productos_Inventario(producto)
                
                # Limpia la pantalla después de agregar el producto
                LimpiarPantalla()
                
                # Muestra un mensaje confirmando que el producto fue agregado exitosamente
                print(f"\nEl producto \033[1m{nombre}\033[0m se ha agregado correctamente")
                
                break
                
            except ValueError as e:
                
                print(f"{e}")
                
                return # Sale del bucle si no hubo errores
        
    # Método para actualizar el nombre de un producto en el inventario
    def actualizar_nombre(self):
        
        # Solicita el nombre actual del producto que se desea modificar
        nombre = input("\nIngrese el nombre del producto a modificar: ").title()
        
        # Llama al método heredado para modificar el nombre del producto
        resultado = self.modficar_nombres_inventario(nombre)
        
        if resultado:
            
            # Muestra el resultado si el producto fue encontrado y modificado
            print(f"\n{resultado}")
        
    # Método para actualizar la categoría de un producto
    def actualizar_categoria(self):
        
        # Solicita la categoría del producto a modificar
        categoria = input("\nIngrese la categoria a modificar: ").title()
        
        # Llama al método heredado para modificar la categoría
        resultado = self.modficar_categorias_inventario(categoria)
        
        if resultado:
            
            # Muestra el resultado de la operación
            print(f"\n{resultado}")
            
    # Método para actualizar el precio de un producto
    def actualizar_precio_producto(self):
        
        # Solicita el nombre del producto cuyo precio será actualizado
        nombre = input("\nIngrese el nombre del producto al que va a modificar el precio: ").title()
        
        # Llama al método heredado para modificar el precio
        resultado = self.modificar_precio_producto(nombre)
        
        if resultado:
            
            # Muestra el resultado de la operación
            print(f"{resultado}")
            
    # Método para actualizar la cantidad de un producto en el inventario
    def actualizar_cantidad_producto(self):
         
        # Solicita el nombre del producto cuya cantidad será actualizada   
        nombre = input("\nIngrese el nombre del producto al que desea cambiar la cantidad en el inventario: ").title()
        
        # Llama al método heredado para modificar la cantidad
        resultado = self.modificar_cantidad_producto(nombre)
        
        if resultado:
            
            # Muestra el resultado de la operación
            print(f"{resultado}")
          
    # Método para eliminar un producto del inventario
    def eliminar_producto_inventario(self):
        
        # Solicita el nombre del producto a eliminar
        nombre = input("\nIngresa el nombre del Producto: ").title()
        
        # Llama al método heredado para eliminar el producto
        self.eliminar_producto(nombre)
     
    # Método para buscar un producto específico en la lista del inventario
    def buscar_producto_lista(self):
        
        while True:
            
            # Solicita el nombre del producto a buscar
            prod = input("\nIngrese el nombre del producto a buscar: ").title()
            
            try:
                
                # Llama al método heredado para buscar el producto
                self.buscar_producto(prod, None)
            
                break # Sale del bucle si el producto se encuentra
            
            except ValueError as e:
                
                # Captura y muestra el error si el producto no existe
                print(f"{e}")
                
                return # Finaliza la operación en caso de error
                    
# Clase para generar y mostrar el menú principal
class Menu:

    def __init__(self):
        
        # Muestra el encabezado del menú principal
        print("\n\033[1mMenú Para Manejo De Inventario\033[0m\n")
        
        # Define las opciones del menú
        self.menu = ["Agregar Producto", "Actualizar Producto", "Eliminar Producto", "Mostrar inventario", "Buscar Producto", "Salir del Sistema"]

    def mostrar_menu(self):
        
        # Itera y muestra cada opción con su índice correspondiente
        for i, elemento in enumerate(self.menu, start = 1):
            
            print(f"\033[1m{i}.\033[0m {elemento}")

# Clase para generar y mostrar el submenú de actualizaciones
class SubMenu:
    
    def __init__(self):
        
        # Muestra el encabezado del submenú
        print("\n\033[1mMenú Para Actualizar el Inventario\033[0m\n")
        
        # Define las opciones del submenú
        self.sub_menu = ["Actualizar Nombre", "Actualizar Categoria","Actualizar Precio","actualizar Cantidad","Regresar al Menú Anterior"]
        
    def mostrar_submenu(self):
    
        # Itera y muestra cada opción del submenú con su índice correspondiente
        for i,n in enumerate(self.sub_menu, start = 1):
            
            print(f"\033[1m{i}.\033[0m {n}")
            
# Clase principal para controlar la ejecución del programa
class Main(): 
      
    def __init__(self): 
        
        # Crea y muestra el menú principal
        self.mi_menu = Menu()    
        self.mi_menu.mostrar_menu()
        self.run() # Inicia el ciclo principal del programa
         
    def run(self):
        
        # Instancia ManejoProductos para operar sobre el inventario
        mis_productos = ManejoProductos()
        
        while True:  
              
            try:
                
                # Solicita al usuario una opción del menú principal        
                opcion = input("\nSeleccione una opción del menú anterior: ")
                    
                # Valida que la opción ingresada sea un número      
                if not opcion.isnumeric(): 
                                 
                    raise ValueError("\nDebes ingresar un número, la opción no es valida")
                            
                opcion = int(opcion)

                # Usa match-case para ejecutar la opción seleccionada
                match opcion: 
                                  
                    case 1:
                        
                        # Llama al método para agregar productos       
                        mis_productos.agregar_productos_nuevos()

                    case 2:
                        
                        # Limpia pantalla y muestra el submenú
                        LimpiarPantalla()
                        
                        self.misubmenu = SubMenu()
                        self.misubmenu.mostrar_submenu()
                        
                        # Aquí se maneja el submenú con sus respectivas opciones
                        while True:
                            
                            try:
                                          
                                opcion1 = input("\nSeleccione una opción del menú anterior: ")
                                
                                if not opcion1.isnumeric():
                                        
                                    raise ValueError("\nDebes ingresar un número, la opción no es valida")
                                
                                opcion1 = int(opcion1)
                                
                                match opcion1:
                                    
                                    case 1:
                                        
                                        mis_productos.actualizar_nombre()
                                        
                                    case 2:
                                        
                                        mis_productos.actualizar_categoria()
                                        
                                    case 3:
                                        
                                        mis_productos.actualizar_precio_producto()
                                        
                                    case 4:
                                        
                                        mis_productos.actualizar_cantidad_producto()
                                        
                                    case 5:
                                        
                                        # pregunta al usuario si se queda en el submenu o sale y convierte la respuesta en mayusculas
                                        continuar = input("\n¿Deseas continuar en el submenú? (S/N): ").upper()
                                        
                                        if continuar != "S":
                                            # Opción para regresar al menú principal
                                            print("\n!Saliendo del Submenú!!\n")
                                            
                                            # Limpia pantalla y sale
                                            LimpiarPantalla()
                                                
                                            break
                                    
                                    case _:
                                        
                                        # lanza una excepcion si no se ha elejido una opcion valida
                                        raise ValueError ("\nDebes elegir un número que este en el menú, intentalo de nuevo")
                                    
                            except ValueError as e:
                                
                                # Captura y muestra errores relacionados con la selección del submenú
                                print(f"{e}")
                                
                    case 3:                    
                        
                        # Llama al método para eliminar productos
                        mis_productos.eliminar_producto_inventario()
                    
                    case 4:
                        
                        # Limpia la pantalla y muestra el inventario completo
                        LimpiarPantalla()
                        
                        mis_productos.mostrar_Inventario()
                        
                    case 5:
                        
                        # Llama al método para buscar un producto
                        mis_productos.buscar_producto_lista()
                                       
                    case 6:
                        
                        # limpia la pantalla y Finaliza la ejecución del programa
                        LimpiarPantalla()
                                           
                        print("\n!Saliendo del Sistema, Hasta Pronto!!\n")
                                            
                        exit()
                                                            
                    case _:
                        
                        # lanza una excepcion si no se ha elejido una opcion valida
                        raise ValueError ("\nDebes elegir un número que este en el menú, intentalo de nuevo")
                                    
            except ValueError as e:
                
                # Captura y muestra errores relacionados con la selección del menú
                print(f"{e}")
            
            # Muestra el menú principal nuevamente después de cada acción
            print("\n\033[1mMenú Para Manejo De Inventario\033[0m\n")
                
            self.mi_menu.mostrar_menu()
                      
# Punto de entrada del programa
if __name__ == '__main__':
    
    Main()