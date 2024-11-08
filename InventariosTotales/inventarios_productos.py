from ProductosTotales.prod_almacen import ProductosAlmacenados

class Inventario():
    
    def __init__(self):
        
        self._inventarioProd = []
        
    def agregar_productos_Inventario(self, producto):
            
        for prod in self._inventarioProd:
            
            if prod.get_nombre() == producto.get_nombre():
                
                raise ValueError ("\nEl producto ya esta en el inventario")
            
            break
                
        self._inventarioProd.append(producto)
                                    
    def eliminar_producto(self, nombre):
        
        try:
        
            for prod in self._inventarioProd:
                
                if prod.get_nombre().title() == nombre.title():
                    
                    producto_encontrado = prod
                    
                    if producto_encontrado:

                        while True:
                            
                            opcion = input("\nSeguro que quieres eliminar el prducto (S/N): ").upper()
                            
                            if opcion == 'S':
                                
                                self._inventarioProd.remove(producto_encontrado)
                                
                                print(f"\nEl producto {nombre} ha sido eliminado correctamente")
                                return
                            
                            print("\nOperacion Cancelada")
                            return
                    
            raise ValueError(f"\nEl producto {nombre} no esta en el inventario")
            
        except ValueError as e:
            
            print(f"{e}")
            
    def mostrar_Inventario(self):
        
        try:
            
            if not self._inventarioProd:
                
                raise ValueError("\nNo hay productos en el inventario para mostrar\n")
            
            print("\n\033[1mEl Inventario Contiene Estos Articulos\033[0m\n")
            print(f"{'-'*70}")
            print(f"{'CATEGORIA':<20} {'NOMBRE ARTICULO':<30} {'CANTIDAD':<10} {'PRECIO':<10}")
            print(f"{'-'*70}")
        
            for prod in self._inventarioProd:
                
                print(f"{prod.get_categoria():<20} {prod.get_nombre():<30} {prod.get_cantidad():<10} {prod.get_precio():<10.2f}")
                
        except ValueError as e:
            
            print(f"{e}")
    
    def buscar_producto(self, nombre, categoria):

        if not self._inventarioProd:
            
            raise ValueError("\nNo hay productos en el inventario para realizar una busqueda\n")     
            
        productoEncontrado = False
    
        for prod in self._inventarioProd:
        
            if prod.get_nombre() == nombre or prod.get_categoria() == categoria:
                
                if not productoEncontrado:
                
                    print("\n\033[1mHas Encontrado Estos Articulos en el Inventario\033[0m\n")
                    print(f"{'-'*70}")
                    print(f"{'CATEGORIA':<20} {'NOMBRE ARTICULO':<30} {'CANTIDAD':<10} {'PRECIO':<10}")
                    print(f"{'-'*70}")
                    
                productoEncontrado = True
                
                print(f"{prod.get_categoria():<20} {prod.get_nombre():<30} {prod.get_cantidad():<10} {prod.get_precio():<10.2f}")
            
                return prod
            
        if not productoEncontrado:
            
            if nombre:
                    
                raise ValueError(f"\nEl producto '{nombre}' no está en el inventario.\n")
            
            if categoria:
                
                raise ValueError(f"\nLa categoria {categoria} no esta en el inventario actual\n")
        
    def modficar_nombres_inventario(self, nombre):
        
        try:
            
            if not self._inventarioProd:
                
                raise ValueError("\nEL inventario esta vacio")
            
            prod_encontrado = self.buscar_producto(nombre, None)
            
            if prod_encontrado:
                
                nuevo_nombre = input("\nIngrese el nuevo nombre del producto: ").title()
                
                prod_encontrado.set_nombre(nuevo_nombre)
                
                return f"\nEl nombre {nombre} se ha modificado correctamente por {nuevo_nombre}!!"

            return f"\nEl nombre {nombre} no se ha modificado correctamente!!"
        
        except ValueError as e:
            
            print(f"{e}")
    
    def modficar_categorias_inventario(self, categoria):
        
        try:
            
            if not self._inventarioProd:
                
                raise ValueError("\nEL inventario esta vacio")
            
            prod_encontrado = self.buscar_producto(None, categoria)
            
            if prod_encontrado:
                
                nueva_categoria = input("\nIngrese la nueva categoria del producto: ").title()
                
                prod_encontrado.set_categoria(nueva_categoria)
                
                return f"\nLa categoria {categoria} se ha modificado correctamente por {nueva_categoria}!!"

            return f"\nLa categoria {categoria} no se ha modificado correctamente!!"
        
        except ValueError as e:
            
            print(f"{e}")
            
    def modificar_precio_producto(self, nombre):
        
        try:
        
            if not self._inventarioProd:
                
                raise ValueError("\nEl Producto no esta en el inventario")
            
            producto_encontrado = self.buscar_producto(nombre, None)
            
            if producto_encontrado:
                
                nuevo_precio = float(input("\nIngrese el nuevo precio para el producto: "))
                
                producto_encontrado.set_precio(nuevo_precio)
                
                return f"\nEl precio de {nombre} se ha modificado correctamente por {nuevo_precio}!!"

            return f"\nEl precio de {nombre} no se ha modificado correctamente!!"
            
        except ValueError as e:
            
            print(f"{e}")
            
    def modificar_cantidad_producto(self, nombre):
        
        try:
        
            if not self._inventarioProd:
                
                raise ValueError("\nEl inventario está vacio")
            
            producto_encontrado = self.buscar_producto(nombre, None)
            
            if producto_encontrado:
                
                nueva_cantidad = int(input("\nIngrese la nueva cantidad para el producto seleccionado: "))
                
                producto_encontrado.set_cantidad(nueva_cantidad)
                
                return f"\nEl producto {nombre}, se ha modificado correctamente por {nueva_cantidad} unidades en el inventario!!"
                
            return f"\nEl producto {nombre} no se ha modificado!!"
                
        except ValueError as e:
            
            print(f"{e}") 