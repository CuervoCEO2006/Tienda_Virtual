from app.model import Tienda



def main():
    tienda: Tienda = Tienda("Tienda APOO")
    ui = TiendaUI = TiendaUI(tienda)
    ui.ejecutar()


if __name__ == "__main__":
    main()

