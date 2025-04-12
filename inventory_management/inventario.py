
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._cantidad = cantidad
    
    def get_nombre(self):
        return self._nombre

    def get_categoria(self):
        return self._categoria

    def get_precio(self):
        return self._precio

    def get_cantidad(self):
        return self._cantidad    
    
    def set_nombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self._nombre = nombre

    def set_categoria(self, categoria):
        if isinstance(categoria, str) and categoria.strip():
            self._categoria = categoria

    def set_precio(self, precio):
        if isinstance(precio, (int, float)) and precio > 0:
            self._precio = precio

    def set_cantidad(self, cantidad):
        if isinstance(cantidad, (int, float)) and cantidad >= 0:
            self._cantidad = cantidad
       
    def mostrar_info(self):
        print(f"\nProducto: {self._nombre}\n"
            f"Categoria: {self._categoria}\n"
            f"Precio: {self._precio}\n"
            f"Cantidad: {self._cantidad}\n")
        
class Inventario:
    def __init__(self):
        self._inventario = [] 
        
    def agregar_producto(self, producto): 
        if not self.producto_existente(producto.get_nombre()):
            self._inventario.append(producto)
            return True 
        return False 
        
    def producto_existente(self, nombre_producto): 
        for producto in self._inventario:
            if producto.get_nombre().lower() == nombre_producto.lower():
                return True
        return False    

    def mostrar_inventario(self):  
        if not self._inventario:
            return None
        else:
            return self._inventario  
                
    def actualizar_producto(self, nombre_producto, nuevo_precio=None, nueva_cantidad=None): 
        for producto in self._inventario:
            if producto.get_nombre().lower() == nombre_producto.lower():
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                return producto
        return None

    def eliminar_producto(self, nombre_producto): 
        for producto in self._inventario:
            if producto.get_nombre().lower() == nombre_producto.lower():
                self._inventario.remove(producto)
                return True
        return False
    
    def buscar_producto(self, nombre_producto):  
        for producto in self._inventario:
            if producto.nombre == nombre_producto:
                return producto 
        return None 
