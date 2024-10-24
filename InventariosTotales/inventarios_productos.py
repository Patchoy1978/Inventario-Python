from ProductosTotales.productos_almacen import Producto

class Inventario:

    def __init__(self):

        self._productos = []

    def agregar_productos(self, producto):
        
        try:
            
            for prod in self._productos:
                
                if prod.get_nombre().title() == producto.get_nombre().title():
                    
                    raise ValueError("El producto ya Existe En El Inventario")
            
            self._productos.append(producto)
                
        except ValueError as e:
            
            print(f"{e}")
            
    def actualizar_producto(self, nombre, nuevo_precio = None, nueva_cantidad = None):
        
        producto = self.buscar_producto(nombre)
        
        try:
            
            if producto:
                
                if nuevo_precio is not None:
                    
                    producto.set_precio(nuevo_precio)
                    
                if nueva_cantidad is not None:
                    
                    producto.set_cantidad(nueva_cantidad)
                
            else:
                
                raise ValueError ("El Producto no ha sido Encontrado")
            
        except ValueError as e:
            
            print(f"{e}")
            
    def eliminar_producto(self, nombre):
        
        producto = self.buscar_producto(nombre)
        
        if producto is None:
            
            raise ValueError("El Producto no Existe en el Inventario")
        
        try:
                
            self.__productos.remove(producto)
            
            print(f"El producto {producto.get_nombre()} ha sido eliminado del Inventario")
        
        except ValueError:
            
            print(f"El producto {nombre} no Existe en el Inventario")
            
    def mostrar_inventario(self):
        
        if not self.__productos:
            
            print("El inventario esta Vacio")
            
        else:
                  
            for prod in self.__productos:
                
                print(f"En el Inventario estan estos productos {prod}")
    
    def buscar_producto(self, nombre):
        
        pass