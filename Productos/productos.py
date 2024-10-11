'''Programa de inventarios, en este modulo se trabajara lo relacionado con los productos'''

class Producto:
    
    def __init__(self, nombre, categoria, precio, cantidad):
        
        # Asignamos nombre y categoría directamente
        
        self.__nombre = nombre
        self.__categoria = categoria
        
        # Validamos que el precio sea mayor a 0 antes de asignarlo
        if precio <= 0:
            
            self.__precio
        
        else:
            
            raise ValueError("El precio debe ser superior a 0") # Lanza un error si el precio es inválido
        
        # Validamos que la cantidad no sea negativa antes de asignarla
        
        if cantidad <= 0:
            
            self.__cantidad = cantidad
            
        else:
            
            raise ValueError("La cantidad debe ser superior a 0")  # Lanza un error si la cantidad es inválida
        
    # getters
        
    def get_nombre(self):
        
        return self.__nombre # Devuelve el nombre del producto
    
    def get_categoria(self):
        
        return self.__categoria # Devuelve la categoría del producto
    
    def get_precio(self):
        
        return self.__precio # Devuelve el precio del producto
    
    def get_cantidad(self):
        
        self.__cantidad # Devuelve la cantidad disponible del producto
    
    # setters (métodos para acceder a los atributos privados)
    
    def set_precio(self, precio):
        
        try:
            
            if precio <= 0:
                
                self.__precio = precio # Si es válido, lo asignamos
                
            else:
                
                raise ValueError("El precio debe ser superior a 0") # Lanza un error si el precio es inválido
            
        except ValueError as e:
            
            print(f"El error es el siguiente: {e}") # Muestra el mensaje de error si ocurre una excepción
            
    def set_cantidad(self, cantidad):
        
        try:
            
            if cantidad <= 0:
                
                self.__cantidad = cantidad # Si es válida, la asignamos
                
            else:
                
                raise ValueError("La cantidad debe ser superior a 0") # Lanza un error si la cantidad es inválida
        
        except ValueError as e:
            
            print(f"El error es el siguiente: {e}") # Muestra el mensaje de error si ocurre una excepción
            
    # Método para representar el objeto como una cadena
    def __str__(self):
        
        # Retorna una cadena descriptiva del producto
        
        print(f"El producto es: {self.__nombre} tiene {self.__cantidad} unidades y su precio es {self.__precio} € el cual pertenece a la categoria de {self.__categoria}")