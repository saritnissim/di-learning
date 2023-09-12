# Exercise 3 : Restaurant Menu Manager
class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice level": "B", "gluten index": False},
            {"name": "Hamburger", "price": 15, "spice level": "A", "gluten index": True},
            {"name": "Salad", "price": 18, "spice level": "A", "gluten index": False},
            {"name": "French Fries", "price": 5, "spice level": "C", "gluten index": False},
            {"name": "Beef bourguignon", "price": 25, "spice level": "B", "gluten index": True}

        ]

    def add_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"] == name:
                print(f"{name} already exists in the menu.")
                return
        new_dish = {"name": name, "price": price, "spice": spice, "gluten": gluten}
        self.menu.append(new_dish)

    def update_item(self, name, price, spice, gluten):
        for item in self.menu:
            if item["name"] == name:
                self.menu.update( {"name": name, "price": price, "spice level": spice, "gluten index": gluten})
                return
        print(f"Manager, we don't have {name} on the menu")

    def remove_item(self, name):
        for item in self.menu:
            if item["name"] == name:
                self.menu.remove(item)
        return 
    

