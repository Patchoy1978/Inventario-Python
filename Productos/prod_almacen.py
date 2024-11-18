# Clase que representa un producto almacenado en el inventario.
class ProductosAlmacenados():
    
    """
        Constructor de la clase ProductosAlmacenados.
        
        Parámetros:
            nombre (str): Nombre del producto.
            categoria (str): Categoría del producto.
            precio (float): Precio del producto. Debe ser mayor o igual a 0.
            cantidad (int): Cantidad de unidades del producto. Debe ser mayor o igual a 0.
        
        Reglas:
        - Si el precio o la cantidad son menores a 0, se lanza una excepción.
        """
    def __init__(self, nombre, categoria, precio, cantidad):
        
        # Inicializa los atributos privados.
        self.__nombre = nombre # Nombre del producto.
        self.__categoria = categoria # Categoría del producto.
        
        # Valida que el precio sea mayor o igual a 0.
        if precio >= 0:
            
            self.__precio = precio
            
        else:
            
            raise ValueError("El Precio debe ser mayor que 0")
        
        # Valida que la cantidad sea mayor o igual a 0.
        if cantidad >= 0:
            
            self.__cantidad = cantidad
            
        else:
            
            raise ValueError("La cantidad debe ser mayor que 0")
    
    # Métodos getters: permiten acceder a los atributos privados.    
    
    def get_nombre(self):
        
        """
        Retorna el nombre del producto, con la primera letra de cada palabra en mayúscula.
        """
        return self.__nombre.title()
    
    def get_categoria(self):
        
        """
        Retorna la categoría del producto, con la primera letra de cada palabra en mayúscula.
        """
        return self.__categoria.title()
    
    def get_precio(self):
        
        """
        Retorna el precio del producto.
        """
        return self.__precio
    
    def get_cantidad(self):
        
        """
        Retorna la cantidad de unidades del producto en el inventario.
        """
        return self.__cantidad
        
    # Métodos setters: permiten modificar los atributos privados con validaciones.
    
    def set_precio(self, precio):
        
        """
        Establece un nuevo precio para el producto.
        
        Parámetros:
            precio (float): Nuevo precio del producto. Debe ser diferente al precio actual.
        
        Reglas:
        - Si el nuevo precio es igual al precio actual, se lanza una excepción.
        - Si se lanza una excepción, solicita al usuario ingresar un precio nuevo.
        """
        while True:
        
            try:
                
                if self.__precio != precio:
                    
                    self.__precio = precio # Actualiza el precio.
                    
                    break
            
                else:
                    
                    # Si el precio es igual al anterior, lanza una excepción.
                    raise ValueError("\nEl precio es igual al anterior")
                
                    
            except ValueError as e:
                
                print(f"{e}")
                
                # Solicita al usuario que ingrese un nuevo precio.
                precio = float(input("\nIngresa un precio nuevo para el producto: "))
            
    def set_cantidad(self, cantidad):
        
        """
        Establece una nueva cantidad para el producto.
        
        Parámetros:
            cantidad (int): Nueva cantidad de unidades. Debe ser mayor o igual a 0.
        
        Reglas:
        - Si la cantidad es menor a 0, se lanza una excepción.
        """
        while True:
            
            try:
                
                if cantidad <= 0:
                    
                    raise ValueError("\nLa cantidad debe ser mayor que 0.")
                    
                if cantidad == self.__cantidad:
                    
                    raise ValueError("\nLa cantidad es igual a la que está en el inventario. No se realiza ningún cambio.")
                    
                self.__cantidad = cantidad # Actualiza la cantidad.
                    
                break
                    
            except ValueError as e:
                
                # Maneja la excepción y muestra el mensaje de error.
                print(f"{e}")
                
                # Solicita al usuario que ingrese una nueva cantidad.
                cantidad = int(input("\nIngresa una nueva cantidada para el producto: "))

    def set_categoria(self, categoria):
        
        """
        Establece una nueva categoría para el producto.
        
        Parámetros:
            categoria (str): Nueva categoría. Debe ser diferente a la categoría actual.
        
        Reglas:
        - Si la nueva categoría es igual a la actual, se lanza una excepción.
        - Si se lanza una excepción, solicita al usuario ingresar una categoría nueva.
        """
        while True:
        
            try:
                
                if self.__categoria != categoria:
                
                    self.__categoria = categoria # Actualiza la categoría.
                    
                    break
                
                else:
                    
                    # Si la categoria es igual a la anterior, lanza una excepción.
                    raise ValueError("\nLa categoria es igual a la anterior")
            
            except ValueError as e:
                
                print(f"{e}")
                
                # Solicita al usuario que ingrese una categoría diferente.
                categoria = input("\nIngresa una categoria diferente: ").title()
            
    def set_nombre(self, nombre):
        
        """
        Establece un nuevo nombre para el producto.
        
        Parámetros:
            nombre (str): Nuevo nombre del producto. Debe ser diferente al nombre actual.
        
        Reglas:
        - Si el nuevo nombre es igual al nombre actual, se lanza una excepción.
        - Si se lanza una excepción, solicita al usuario ingresar un nombre nuevo.
        """
        while True:
        
            try:
                
                if self.__nombre != nombre:
                
                    self.__nombre = nombre # Actualiza el nombre.
                    
                    break
                
                else:
                    
                    # Si el nombre es igual al anterior, lanza una excepción.
                    raise ValueError("\nEl nuevo nombre no puede ser igual al nombre anterior")
            
            except ValueError as e:
                
                print(f"{e}")
                
                # Solicita al usuario que ingrese un nombre diferente.
                nombre = input("\nIngresa un nombre diferente: ").title()