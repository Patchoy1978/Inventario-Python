class ProductosAlmacenados():
    
    def __init__(self, nombre, categoria, precio, cantidad):
        
        self.__nombre = nombre
        self.__categoria = categoria
        
        if precio >= 0:
            
            self.__precio = precio
            
        else:
            
            raise ValueError("El Precio debe ser mayor que 0")
        
        if cantidad >= 0:
            
            self.__cantidad = cantidad
            
        else:
            
            raise ValueError("La cantidad debe ser mayor que 0")
        
    # getters
    
    def get_nombre(self):
        
        return self.__nombre.title()
    
    def get_categoria(self):
        
        return self.__categoria.title()
    
    def get_precio(self):
        
        return self.__precio
    
    def get_cantidad(self):
        
        return self.__cantidad
        
    # setters
    
    def set_precio(self, precio):
        
        while True:
        
            try:
                
                if self.__precio != precio:
                    
                    self.__precio = precio
                    
                    break
            
                else:
                    
                    raise ValueError("\nEl precio es igual al anterior")
                
                    
            except ValueError as e:
                
                print(f"{e}")
                
                precio = int(input("\nIngresa un precio nuevo para el producto: "))
            
    def set_cantidad(self, cantidad):
        
        try:
            
            if cantidad >= 0:
                
                self.__cantidad = cantidad
                
            else:
                
                raise ValueError("La cantidad debe ser mayor que 0")
                
        except ValueError as e:
            
            print(f"{e}")  

    def set_categoria(self, categoria):
        
        while True:
        
            try:
                
                if self.__categoria != categoria:
                
                    self.__categoria = categoria
                    
                    break
                
                else:
                    
                    raise ValueError("\nLa categoria es igual a la anterior")
            
            except ValueError as e:
                
                print(f"{e}")
                
                categoria = input("\nIngresa una categoria diferente: ").title()
            
    def set_nombre(self, nombre):
        
        while True:
        
            try:
                
                if self.__nombre != nombre:
                
                    self.__nombre = nombre
                    
                    break
                
                else:
                    
                    raise ValueError("\nEl nuevo nombre no puede ser igual al nombre anterior")
            
            except ValueError as e:
                
                print(f"{e}")
                
                nombre = input("\nIngresa un nombre diferente: ").title()
                