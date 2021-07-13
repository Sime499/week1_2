
Shopping_lists=[]


class ShoppingList:
    def _init_(self,store,address):
      self.title=title
      self.address=address
      self.item=[]


    def add_item(self, item): 
       self.items.append(item)

class Item: 
  def __init__(self, price, quantity): 
    self.price = price 
    self.quantity = quantity 


while True:
  
    print("Enter 1.add store information:")
    print("Enter 3.display all shopping_list information:")
    print("Enter q to quit:")

    user_choice  =input("please enter your selection:")

  
    if user_choice== "q":
      break

    if user_choice== "1":
      store=input("Enter the name of the store name:")
      address=input("Enter {street_no} {city}{state}:")
      shopping_list=ShoppingList(store,address)
      shopping_list.append(shopping_list)
      print(shopping_list)

    if user_choice== "2":
        for i in range(0,shopping_lists)):
          print(f"{shopping_lists[i].store}")
          store=shopping
          print(store)

    store_location=int(input(" select which  store  "))
    title=input("Item you would like to add to shopping cart:")
    price=input("cost of and an item  ")
    shopping_list=shopping_list[store_location-1]
    shopping_list.item.append[Item]
