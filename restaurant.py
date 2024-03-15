class Order():
    def __init__(self) -> None:
        self.items = []
        self.total = None

    def calculate_price(self):
        self.total = sum([item.price * item.quantity for item in self.items])

    def calculate_discount(self, discount):
        self.total -= self.total * (discount / 100)

    def add_item(self, item):
        self.items.append(item)

    def print_bill(self):
        for item in self.items:
            print(f"{item.name} - {item.price} - {item.quantity}")
        print(f"Total: {self.total}")

class MenuItem():
    def __init__(self, price, name, quantity) -> None:
        self.price = price
        self.name = name
        self.quantity = quantity

class Beverage(MenuItem):
    def __init__(self, price, size, name, quantity) -> None:
        super().__init__(price, name, quantity)
        self.size = size

class Appetizer(MenuItem):
    def __init__(self, price, customers, name, quantity) -> None:
        super().__init__(price, name, quantity)
        self.customers = customers

class MainCourse(MenuItem):
    def __init__(self, price, grammage, name, quantity) -> None:
        super().__init__(price, name, quantity)
        self.grammage = grammage


order = Order()
running = True

while running:
    selection = input("¿Desea ordenar un plato principal? (s/n): ")
    if selection == "s":
        print("""Platos principales:
        1. Hamburguesa sencilla
        2. Hamburguesa doble
        3. Hamburguesa ranchera
        4. Hamburguesa todo terreno
        """)
        main_course = int(input("Seleccione una opción: "))
        if main_course == 1:
            print("Hamburguesa sencilla seleccionada")
            order.add_item(MainCourse(12000, 150, "Hamburguesa sencilla", int(input("Cantidad: "))))
        elif main_course == 2:
            print("Hamburguesa doble seleccionado")
            order.add_item(MainCourse(16000, 300, "Hamburguesa doble", int(input("Cantidad: "))))
        elif main_course == 3:
            print("Hamburguesa ranchera seleccionada")
            order.add_item(MainCourse(20000, 200, "Hamburguesa ranchera", int(input("Cantidad: "))))
        elif main_course == 4:
            print("Hamburguesa todo terreno seleccionada")
            order.add_item(MainCourse(23000, 250, "Hamburguesa todo terreno", int(input("Cantidad: "))))            


    selection = input("¿Desea ordenar una entrada? (s/n): ")
    if selection == "s":
        print("""Entradas:
        1. Canasta de pan (3 personas)
        2. Sopa (1 persona)
        3. Papas fritas (5 personas)
        """)
        appetizer = int(input("Seleccione una opción: "))
        if appetizer == 1:
            print("Canasta de pan seleccionada")
            order.add_item(Appetizer(4000, 3, "Canasta de pan", int(input("Cantidad: "))))
        elif appetizer == 2:
            print("Sopa seleccionada")
            order.add_item(Appetizer(6000, 1, "Sopa seleccionada", int(input("Cantidad: "))))
        elif appetizer == 3:
            print("Papas fritas seleccionadas")
            order.add_item(Appetizer(8000, 5, "Papas fritas seleccionadas", int(input("Cantidad: "))))


    selection = input("¿Desea ordenar una bebida? (s/n): ")
    if selection == "s":
        print("""Bebidas:
        1. Agua
        2. Refresco
        3. Jugo
        """)
        beverage = int(input("Seleccione una opción: "))
        if beverage == 1:
            print("Agua seleccionada")
            order.add_item(Beverage(2000, 500, "Agua seleccionada", int(input("Cantidad: "))))
        elif beverage == 2:
            print("Refresco seleccionado")
            order.add_item(Beverage(3000, 500, "Refresco seleccionado", int(input("Cantidad: "))))
        elif beverage == 3:
            print("Jugo seleccionado")
            order.add_item(Beverage(5000, 600, "Jugo seleccionado", int(input("Cantidad: "))))

    selection = input("¿Desea ordenar algo más? (s/n)")
    if selection == 'n':
        running = False


order.calculate_price()

selection = input("¿Posee un cupón de descuento? (s/n): ")
if selection == "s":
    discount = int(input("Ingrese el valor porcentual descuento: "))
    order.calculate_discount(discount)

order.print_bill()