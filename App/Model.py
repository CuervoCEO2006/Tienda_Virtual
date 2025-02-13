class Producto:

    def __init__(self, nombre: str, precio: float): #Define los atributos y el parametro
        self.nombre : str = nombre
        self.precio : float = precio

    def mostrar_info(self) -> str:
        return f"{self.nombre} - {self.precio}"


p1: Producto = Producto("arroz" , 10000)
p2: Producto = Producto("Crema dental" , 5000)
print(p1.mostrar_info())
print(p2.mostrar_info())

class Cliente:

    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.carrito: list[Producto] = []
    def agregar_producto(self, producto: Producto):
        self.carrito.append(producto)
    def mostrar_carrito(self) -> str:
        productos_str: str = ""
        for producto in self.carrito:
            productos_str += producto.mostrar_info() + "\n"
        return productos_str

    def calcular_total(self) -> float:
        total = 0
        for producto in self.carrito:
            total += producto.precio
        return total

class Tienda:

    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.productos: list[Producto] = []

    def agregar_productos(self, producto: Producto):
        self.productos.append(producto)

    def mostrar_carrito(self, producto: Producto):
        productos_str: str = ""
        for producto in self.productos:
            productos_str += producto.mostrar_info() + "\n"
        return productos_str




