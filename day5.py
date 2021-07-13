stores=[]

class ShoppingList:
    def __init__(self,title,address):
      self.title=title
      self.address=address
      self.item=[]


    def add_item(self, item): 
       self.items.append(item)

class Item: 
  def __init__(self, price, quantity): 
    self.price = price 
    self.quantity = quantity 

print("1 to add shopping list")
print("2 to view all Shopping List")
print("3 to add item into shopping list")
print("4 to delete item from shopping list")
print("q to quit")


while True:
    
    user_choice  =input("please enter your selection:")

  
    if user_choice== "q":
      break

    if user_choice== "1":
      store_name=input("Enter the name of the store name:")
      store_address=input("Enter {street_no} {city}{state}:")
      shopping_list=ShoppingList(store_name,store_address)
      stores.append(shopping_list)
      

    elif user_choice== "2":
      for store in stores:
          print(store.title)

    elif user_choice=="3":
        
        for i in range(0,len(stores)):
          store=stores[i]
          print(f"{i+1}. {store.title}")
    
        
        store_number = int(input("Enter Store Number: "))
        store = stores[store_number - 1]
        item_name = input("Enter item name: ")
        item_price = float(input("Enter item price: ")) 
        item = Item(item_name, item_price)
        store.item.append:[item]
    
    
    
    
    elif user_choice=="4":
      
      for i in range(0,len(stores)):
        
        print(f"{i+1}.{stores[i].title}")
      store_number = int(input("Enter Store Number to delete: "))
      del stores[store_number-1]

