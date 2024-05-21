class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"товар {item_name} был добавлен в {self.name}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"товар {item_name} был удален из {self.name}")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"цена {item_name} была обновлена в {self.name}")
        else:
            print(f"товар {item_name} не найден в {self.name}")

store1 = Store("магнит", "ул. Пушкина, 1")
store2 = Store("пятерочка", "ул. Пушкина, 2")
store3 = Store("табрис", "ул. Пушкина, 12")

store1.add_item("молоко", 100)
store1.add_item("курица", 200)
store1.add_item("селедка", 300)

store1.remove_item("молоко")

print(store1.get_price("курица"))

store1.update_price("селедка", 150)