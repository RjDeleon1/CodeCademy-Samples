class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "Menu name: " + self.name + ", " + " Times available: " + str(self.start_time) + " hrs " + " - " + str(self.end_time) + " hrs"

  def calculate_bill(self, purchased_items):
    total = 0
    for items in purchased_items:
      if items in self.items:
        total += self.items[items]
    return total


##Start of class
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return "Welcome to our restaurant, our address is: " + self.address

  def available_menus(self, time):
    available = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available.append(menu)
    return available
## End of class

## class start
class Business:
  def __init__(self, name, franchises):
    pass
## class end


brunch = Menu("brunch", {'pancakes': 7.50,'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)

early_bird = Menu("early bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}, 15, 18)

dinner = Menu("dinner",{'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}, 17, 23)

kids = Menu("kids",{'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)

arepas_menu = Menu("Arepas",{'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50 },10, 20)

print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise('1232 West End Road', menus)

new_installment = Franchise('12 East Mulberry Street', menus)

print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))

stores = [flagship_store, new_installment]

chain = Business("Basta Fazoolin' with my Heart", stores)

arepas_place = Franchise('189 Fitzgerald Avenue', arepas_menu)

arepas = Business("Take a' Arepa", arepas_place)

