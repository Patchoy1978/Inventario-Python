from ProductosTotales.prod_almacen import ProductosAlmacenados
from InventariosTotales.inventarios_productos import Inventario
import platform
import os

class LimpiarPantalla():
    
    def __init__(self):
        
        self.limpiarpantalla()
        
    def limpiarpantalla(self):
        
        sisop = platform.system()
        
        if sisop == "Windows":
            
            os.system("cls")
        
        else:
            
            os.system("clear")

class ManejoProductos(Inventario):

    def agregar_productos_nuevos(self):
        
        nombre = input("\nIngrese el nombre del Producto: ").title()
        categoria = input("\nIngrese el nombre de la Categoria: ").title()
        
        while True:
        
            try:
                
                precio = float(input("\nIngrese el Precio del Producto: "))
    
                cantidad = int(input("\nIngrese La Cantidad del Producto: "))
            
                producto =  ProductosAlmacenados(nombre, categoria, precio, cantidad)
                
                self.agregar_productos_Inventario(producto)
                
                LimpiarPantalla()
                
                print(f"\nEl producto \033[1m{nombre}\033[0m se ha agregado correctamente")
                
                break
                
            except ValueError as e:
                
                print(f"{e}")
                
                return
        
    def actualizar_nombre(self):
    
        nombre = input("\nIngrese el nombre del producto a modificar: ").title()
        
        resultado = self.modficar_nombres_inventario(nombre)
        
        if resultado:
            
            print(f"\n{resultado}")
        
    def actualizar_categoria(self):
        
        categoria = input("\nIngrese la categoria a modificar: ").title()
        
        resultado = self.modficar_categorias_inventario(categoria)
        
        if resultado:
            
            print(f"\n{resultado}")
            
    def actualizar_precio_producto(self):
        
        nombre = input("\nIngrese el nombre del producto al que va a modificar el precio: ").title()
        
        resultado = self.modificar_precio_producto(nombre)
        
        if resultado:
            
            print(f"{resultado}")
            
    def actualizar_cantidad_producto(self):
            
        nombre = input("\nIngrese el nombre del producto al que desea cambiar la cantidad en el inventario: ").title()
        
        resultado = self.modificar_cantidad_producto(nombre)
        
        if resultado:
            
            print(f"{resultado}")
          
    def eliminar_producto_inventario(self):
        
        nombre = input("\nIngresa el nombre del Producto: ").title()
        
        self.eliminar_producto(nombre)
     
    def buscar_producto_lista(self):
        
        while True:
        
            prod = input("\nIngrese el nombre del producto a buscar: ").title()
            
            try:
                
                self.buscar_producto(prod, None)
            
                break
            
            except ValueError as e:
                
                print(f"{e}")
                
                return
                    
class Menu:
    
    def __init__(self):
        
        print("\n\033[1mMenú Para Manejo De Inventario\033[0m\n")
        
        self.menu = ["Agregar Producto", "Actualizar Producto", "Eliminar Producto", "Mostrar inventario", "Buscar Producto", "Salir del Sistema"]
        
    def mostrar_menu(self):
        
        for i, elemento in enumerate(self.menu, start = 1):
            
            print(f"\033[1m{i}.\033[0m {elemento}")

class SubMenu:
    
    def __init__(self):
        
        print("\n\033[1mMenú Para Actualizar el Inventario\033[0m\n")
        
        self.sub_menu = ["Actualizar Nombre", "Actualizar Categoria","Actualizar Precio","actualizar Cantidad","Regresar al Menú Anterior"]
        
    def mostrar_submenu(self):
    
        for i,n in enumerate(self.sub_menu, start = 1):
            
            print(f"\033[1m{i}.\033[0m {n}")
            
class Main(): 
      
    def __init__(self): 
           
        self.mi_menu = Menu()    
        self.mi_menu.mostrar_menu()
        self.run()   
         
    def run(self):
        
        mis_productos = ManejoProductos()
        
        while True:  
              
            try:
                            
                opcion = input("\nSeleccione una opción del menú anterior: ")
                            
                if not opcion.isnumeric(): 
                                  
                    raise ValueError("\nDebes ingresar un número, la opción no es valida")
                            
                opcion = int(opcion)
         
                match opcion: 
                                  
                    case 1:
                                         
                        mis_productos.agregar_productos_nuevos()

                    case 2:
                        
                        LimpiarPantalla()
                        
                        self.misubmenu = SubMenu()
                        self.misubmenu.mostrar_submenu()
                        
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
                                        
                                        continuar = input("\n¿Deseas continuar en el submenú? (S/N): ").upper()
                                        
                                        if continuar != "S":
                                                                
                                            print("\n!Saliendo del Submenú!!\n")
                                            
                                            LimpiarPantalla()
                                                
                                            break
                                    
                                    case _:
                                        
                                        raise ValueError ("\nDebes elegir un número que este en el menú, intentalo de nuevo")
                                    
                            except ValueError as e:
                                
                                print(f"{e}")
                                
                    case 3:                    
                        
                        mis_productos.eliminar_producto_inventario()
                    
                    case 4:
                        
                        LimpiarPantalla()
                        
                        mis_productos.mostrar_Inventario()
                        
                    case 5:
                        
                        mis_productos.buscar_producto_lista()
                                       
                    case 6:
                        
                        LimpiarPantalla()
                                           
                        print("\n!Saliendo del Sistema, Hasta Pronto!!\n")
                                            
                        exit()
                                                            
                    case _:
                        
                        raise ValueError ("\nDebes elegir un número que este en el menú, intentalo de nuevo")
                                    
            except ValueError as e:
                     
                print(f"{e}")
                
            print("\n\033[1mMenú Para Manejo De Inventario\033[0m\n")
                
            self.mi_menu.mostrar_menu()
                      
if __name__ == '__main__':
    
    Main()