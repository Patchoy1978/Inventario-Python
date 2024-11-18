# Importa la clase ProductosAlmacenados desde el módulo correspondiente
from Productos.prod_almacen import ProductosAlmacenados

# Clase que maneja el inventario de productos
class Inventario():
    
    def __init__(self):
        
        """
        Inicializa una instancia de la clase Inventario.
        Se crea un atributo protegido _inventarioProd, que almacenará una lista de objetos
        de productos gestionados en el inventario.
        """
        self._inventarioProd = [] # Lista vacía para almacenar los productos.
        
    # Método para agregar productos al inventario
    def agregar_productos_Inventario(self, producto):
        
        """
        Agrega un producto al inventario.
        
        Parámetros:
            producto (ProductosAlmacenados): Objeto que representa un producto.
        
        Reglas:
        - Si un producto con el mismo nombre ya está en el inventario, lanza una excepción.
        """    
        for prod in self._inventarioProd:
            
            # Compara el nombre del producto a agregar con los nombres de productos existentes.
            if prod.get_nombre() == producto.get_nombre():
                
                # Si el producto ya está en el inventario, lanza una excepción
                raise ValueError ("\nEl producto ya esta en el inventario")
            
            break # Solo necesita verificar una vez si el producto ya está presente.
        
        # Agrega el nuevo producto a la lista del inventario        
        self._inventarioProd.append(producto)
                                    
    # Método para eliminar un producto del inventario por nombre
    def eliminar_producto(self, nombre):
        
        """
        Elimina un producto del inventario en base a su nombre.
        
        Parámetros:
            nombre (str): Nombre del producto a eliminar.
        
        Reglas:
        - Si el producto no existe, lanza una excepción.
        - Solicita confirmación al usuario antes de eliminar el producto.
        """
        try:
        
            for prod in self._inventarioProd:
                
                # Compara los nombres de los productos, ignorando mayúsculas y minúsculas
                if prod.get_nombre().title() == nombre.title():
                    
                    producto_encontrado = prod
                    
                    if producto_encontrado:
                        
                        # Si se encuentra, solicita confirmación antes de eliminar.
                        while True:
                            
                            opcion = input("\nSeguro que quieres eliminar el prducto (S/N): ").upper()
                            
                            if opcion == 'S': # Si el usuario confirma:
                                
                                self._inventarioProd.remove(producto_encontrado) # Elimina el producto.
                                
                                print(f"\nEl producto {nombre} ha sido eliminado correctamente")
                                return
                            
                            # Si el usuario cancela, muestra un mensaje.
                            print("\nOperacion Cancelada")
                            return
            
            # Si el producto no se encuentra, lanza una excepción        
            raise ValueError(f"\nEl producto {nombre} no esta en el inventario")
            
        except ValueError as e:
            
             # Captura y muestra errores relacionados con la operación.
            print(f"{e}")
            
    # Método para mostrar todos los productos en el inventario
    def mostrar_Inventario(self):
        
        """
        Muestra todos los productos en el inventario en formato de tabla.
        
        Reglas:
        - Si el inventario está vacío, lanza una excepción.
        """
        try:
            
            # Verifica si el inventario está vacío.
            if not self._inventarioProd:
                
                # Si el inventario está vacío, lanza una excepción
                raise ValueError("\nNo hay productos en el inventario para mostrar\n")
            
            # Imprime una tabla con los encabezados y los datos de los productos.
            print("\n\033[1mEl Inventario Contiene Estos Articulos\033[0m\n")
            print(f"{'-'*70}")
            print(f"{'CATEGORIA':<20} {'NOMBRE ARTICULO':<30} {'CANTIDAD':<10} {'PRECIO':<10}")
            print(f"{'-'*70}")
        
            # Recorre cada producto en el inventario y lo muestra en la tabla.
            for prod in self._inventarioProd:
                
                print(f"{prod.get_categoria():<20} {prod.get_nombre():<30} {prod.get_cantidad():<10} {prod.get_precio():<10.2f}")
                
        except ValueError as e:
            
            # Muestra un mensaje de error si el inventario está vacío.
            print(f"{e}")
    
    # Método para buscar productos en el inventario
    def buscar_producto(self, nombre, categoria):

        """
        Busca un producto en el inventario por nombre o categoría.
        
        Parámetros:
            nombre (str): Nombre del producto a buscar.
            categoria (str): Categoría del producto a buscar.
        
        Reglas:
        - Si el inventario está vacío, lanza una excepción.
        - Si no encuentra ningún producto, lanza una excepción.
        
        Retorno:
            Retorna el producto encontrado o lanza una excepción si no se encuentra.
        """
        if not self._inventarioProd:
            
            # Si el inventario está vacío, no es posible buscar productos.
            raise ValueError("\nNo hay productos en el inventario para realizar una busqueda\n")
            
        productoEncontrado = False # Variable para rastrear si se encuentra un producto.
    
        for prod in self._inventarioProd:
            
            # Verifica si el producto coincide por nombre o categoría.
            if prod.get_nombre() == nombre or prod.get_categoria() == categoria:
                
                if not productoEncontrado:
                
                    # Muestra encabezados solo la primera vez que encuentra un producto.
                    print("\n\033[1mHas Encontrado Estos Articulos en el Inventario\033[0m\n")
                    print(f"{'-'*70}")
                    print(f"{'CATEGORIA':<20} {'NOMBRE ARTICULO':<30} {'CANTIDAD':<10} {'PRECIO':<10}")
                    print(f"{'-'*70}")
                    
                productoEncontrado = True
                
                # Muestra los detalles del producto encontrado.
                print(f"{prod.get_categoria():<20} {prod.get_nombre():<30} {prod.get_cantidad():<10} {prod.get_precio():<10.2f}")
            
                return prod
        
        # Si no encuentra ningún producto, lanza una excepción.    
        if not productoEncontrado:
            
            if nombre:
                    
                raise ValueError(f"\nEl producto '{nombre}' no está en el inventario.\n")
            
            if categoria:
                
                raise ValueError(f"\nLa categoria {categoria} no esta en el inventario actual\n")
        
    # Métodos para modificar propiedades específicas de los productos (nombre, categoría, precio, cantidad).
    def modficar_nombres_inventario(self, nombre):
        
        """
        Modifica el nombre de un producto específico.
        
        Parámetros:
            nombre (str): Nombre actual del producto a modificar.
        
        Retorno:
            Mensaje de confirmación de la operación.
        """
        try:
            
             # Verifica que el inventario no esté vacío.
            if not self._inventarioProd:
                
                raise ValueError("\nEL inventario esta vacio")
            
            prod_encontrado = self.buscar_producto(nombre, None) # Busca el producto.
            
            if prod_encontrado:
                
                # Solicita el nuevo nombre al usuario.
                nuevo_nombre = input("\nIngrese el nuevo nombre del producto: ").title()
                
                prod_encontrado.set_nombre(nuevo_nombre) # Actualiza el nombre del producto.
                
                return f"\nEl nombre {nombre} se ha modificado correctamente por {nuevo_nombre}!!"

            return f"\nEl nombre {nombre} no se ha modificado correctamente!!"
        
        except ValueError as e:
            
            # Maneja excepciones durante la operación.
            print(f"{e}")
    
    def modficar_categorias_inventario(self, categoria):
        
        """
        Modifica la categoria de un producto específico.
        
        Parámetros:
            categoria (str): Categoria actual del producto a modificar.
        
        Retorno:
            Mensaje de confirmación de la operación.
        """
        try:
            
             # Verifica que el inventario no esté vacío.
            if not self._inventarioProd:
                
                raise ValueError("\nEL inventario esta vacio")
            
            prod_encontrado = self.buscar_producto(None, categoria) # Busca el producto.
            
            if prod_encontrado:
                
                # Solicita el nuevo nombre al usuario.
                nueva_categoria = input("\nIngrese la nueva categoria del producto: ").title()
                
                prod_encontrado.set_categoria(nueva_categoria) # Actualiza el nombre de la categoria.
                
                return f"\nLa categoria {categoria} se ha modificado correctamente por {nueva_categoria}!!"

            return f"\nLa categoria {categoria} no se ha modificado correctamente!!"
        
        except ValueError as e:
            
            # Maneja excepciones durante la operación.
            print(f"{e}")
            
    def modificar_precio_producto(self, nombre):
        
        """
        Modifica el precio de un producto específico.
        
        Parámetros:
            precio (float): Nombre actual del producto a modificar.
        
        Retorno:
            Mensaje de confirmación de la operación.
        """
        try:
            
            # Verifica que el inventario no esté vacío.
            if not self._inventarioProd:
                
                raise ValueError("\nEl Producto no esta en el inventario")
            
            producto_encontrado = self.buscar_producto(nombre, None) # Busca el producto.
            
            if producto_encontrado:
                
                # Solicita el nuevo precio al usuario.
                nuevo_precio = float(input("\nIngrese el nuevo precio para el producto: "))
                
                producto_encontrado.set_precio(nuevo_precio) # Actualiza el precio del producto.
                
                return f"\nEl precio de {nombre} se ha modificado correctamente por {nuevo_precio}!!"

            return f"\nEl precio de {nombre} no se ha modificado correctamente!!"
            
        except ValueError as e:
            
            # Maneja excepciones durante la operación.
            print(f"{e}")
            
    def modificar_cantidad_producto(self, nombre):
        
        """
        Modifica la cantidad de un producto específico.
        
        Parámetros:
            cantidad (int): Nombre actual del producto a modificar.
        
        Retorno:
            Mensaje de confirmación de la operación.
        """
        try:
            
            # Verifica que el inventario no esté vacío.
            if not self._inventarioProd:
                
                raise ValueError("\nEl inventario está vacio")
            
            producto_encontrado = self.buscar_producto(nombre, None) # Busca el producto.
            
            if producto_encontrado:
                
                while True:
                    
                    try:
                        nueva_cantidad = int(input("\nIngrese la nueva cantidad para el producto seleccionado: "))
                        # Llama a set_cantidad para actualizar la cantidad del producto
                        producto_encontrado.set_cantidad(nueva_cantidad)
                        return f"\nEl producto {nombre} ha sido modificado correctamente en el inventario."
                    except ValueError:
                        print("\nPor favor, ingresa una cantidad válida (un número entero).")
                
            else:
                
                return f"\nEl producto {nombre} no se ha encontrado en el inventario."
        
        except ValueError as e:
            
            # Maneja excepciones durante la operación.
            print(f"{e}") 