class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.name=name
    self.items=items
    self.start_time=start_time
    self.end_time=end_time
  def __repr__(self):
    self.menu_string="{Menu} menu is avaibable from {start_time} to {end_time}".format(Menu=self.name,start_time=self.start_time,end_time=self.end_time)
    return self.menu_string
  def calculate_bill(self,purchased_items):
    total=0
    for items in purchased_items:
      if items in self.items:
        total+=self.items[items]
    return total

brunch_items={
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch=Menu("Brunch",brunch_items, 1100,1600)

early_bird_items={
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird=Menu("Early Bird",early_bird_items, 1500,1800)

dinner={
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner_menu=Menu("Dinner",dinner,1700,2300)

kids={
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_menu=Menu("Kids",kids,1100,2100)



print(brunch)


print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))


print(early_bird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))


class Franchise:
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address
  def available_menus(self, time):
    available_menus=[]
    for menus in self.menus:
      if time>=menus.start_time and time <= menus.end_time:
        available_menus.append(menus)
    return available_menus

flagship_store=Franchise("1232 West End Road",[brunch,early_bird,dinner_menu,kids_menu])

new_installment=Franchise("12 East Mulberry Street",[brunch,early_bird,dinner_menu,kids_menu])

print(flagship_store.available_menus(1700))


class Business:
  def __init__(self,name,franchises):
    self.name = name
    self.franchises = franchises

arepas_items={
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu=Menu("Arepas Menu",arepas_items,1000,2000)

arepas_place=Franchise("189 Fitzgerald Avenue",arepas_menu)

arepas_business=Business("Take a' Arepa",arepas_place)
