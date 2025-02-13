from rich import Console, box
from rich.prompt import Prompt
from rich.table import Table

from app.model import Tienda, Producto


class TiendaUI:

    def __init__(self, tienda: Tienda):
        self.Tienda: Tienda = Tienda
        self.consola: Console = Console()

    def mostrar_menu(self):
        self.consola.print("\n[bold green]Tienda Virtual[/bold green]")

        self.consola.print("agregar producto a tienda")
        self.consola.print("Mostrar productos de la tienda")
        self.consola.print("Agregar producto al carrito")
        self.consola.print("Mostrar carrito de compras")
        self.consola.print("Calcular total de compra")
        self.consola.print("salir")

        opcion = Prompt.ask("\nSeleccione una opción", choices=["1","2","3","4","5",])
        return opcion



    def ejecutar(self):
        while True:
            opcion = self.mostrar_menu()
            match opcion:

                case "1":
                    self.agregar_producto_a_tienda()

                case "2":
                    self.Mostrar_productos_de_la_tienda()

                case "3":
                    pass

                case "4":
                    pass

                case "5":
                    pass

                case "6":
                    self.consola.print("hasta luego!", style="bold red")
                    break


    def agregar_producto_a_tienda(self):
        nombre: str = Prompt.ask("Nombre del producto")
        precio: float = float(Prompt.ask("precio del producto"))
        producto: Producto = Producto(nombre, precio)
        #TERMINAR

    def mostrar_productos_tienda(self):
        if len(self.tienda.productos) == 0:
            self.consola.print("[red]No ay productos disponibles[/red]")
            return

        tabla: Table = Table(title="lista de productos", box=box.SQUARE_DOUBLE_HEAD)
        tabla.add_column("#", style="cyan")
        tabla.add_column("nombre", style="magenta")
        tabla.add_column("precio", style="blue")

        for i in range(len(self.tienda.productos)):
            tabla.add_row(str(i+1), self.tienda.productos[i].nombre,










