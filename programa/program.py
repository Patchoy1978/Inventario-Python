from ProductosTotales.productos_almacen import Producto
from InventariosTotales.inventarios_productos import Inventario

class AgregarProductos(Inventario):
    
    def agregar_nuevos_productos(self):
    
        nombre = input("Ingrese el nombre del Producto: ").title()
        categoria = input("Ingrese la categoria a al que pertenece el Producto: ").title()
        
        while True:
        
            try:
                
                precio = float(input("Ingresa el precio del producto: "))
                cantidad = int(input("Ingresa la cantidad del producto: "))
            
                mi_producto = Producto(nombre, categoria, precio, cantidad)
            
                self._productos.append(mi_producto)

                print(f"El articulo {nombre} ha sido agregado al inventario con exito")
                
                break
            
            except ValueError as e:
                
                print(f"{e}")
    
class Menu:
    
    def __init__(self):
        
        print("\n\033[1mMenú de Manejo De Inventario\033[0m\n")
    
        self.menu = ['Agregar Productos','Actualizar un Producto', 'Eliminar Productos', 'Mostrar Inventario', 'Buscar Producto', 'Salir']
    
    def mostrar_menu(self):
        
        for index, elemento in enumerate(self.menu, start = 1):
            
            print(f"\033[1m{index}.\033[0m {elemento}")

class Main():
    
    def __init__(self):
    
        self.mi_menu = Menu()
        
        self.mi_menu.mostrar_menu()
        
        self.run()
        
    def run(self):
        
        mis_productos = AgregarProductos()
    
        while True:
            
            try:
                
                opcion = input("\nElige una opción del menú anterior:\033[1m \033[0m")
                
                if not opcion.isnumeric():
                    
                    raise ValueError("\nCaracter Invalido, Debe ser un Número")
                
                opcion = int(opcion)
                                
                match opcion:
                    
                    case 1:
                        
                        mis_productos.agregar_nuevos_productos()
                    
                    case 2:
                        
                        pass
                    
                    case 3:
                        
                        pass
                    
                    case 4:
                        
                        pass
                    
                    case 5:
                        
                        pass
                    
                    case 6:
                        
                        print("\nSaliendo del Sistema, Hasta Pronto!!" )
                        exit()
                        
                    case _:
                        
                        print("!Has Seleccionado un caracter invalido, Vuelve a intentar!!")
                        
            except ValueError as e:
                
                print(f"{e}")

if __name__ == '__main__':
    
    Main()