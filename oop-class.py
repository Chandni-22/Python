'''OOP: Object-oriented programming (OOP) is like organizing your code by thinking about things as objects. Imagine your code is like a toy box, called "class", and each toy is an object. OOP helps you keep your toys (or objects) organized and easy to play with.'''

# class student:
# #student is a class.
#     # __init__ works as initial.
#     def __init__(self, name, last, age, phone):
#         self.name=name
#         self.last=last
#         self.age=age
#         self.phone=phone
#         #self is an object in student.

#     def fullName(self):
#         return (self.name+" "+self.last)
    
#     def back4(self):
#         return (self.age-4)
    
#     def deffi(self):
#         a=f"{self.name} s full name is {self.name} {self.last} and her age is {str(self.age)}."
#         return a
    
# #student_1 is an instance of class student.   
# student_1=student("Chandni", "Vishwakarma", 20, 9873193222)

# print(student_1.fullName())
# print(student.back4(student_1))
# print(student_1.deffi()) 

# #__dict__ will return the dictionary contains the information of instance.
# print(student_1.__dict__)

# # Gives the info.
# print(help(student))

# The super() function is used to give access to methods and properties of a parent or sibling class.

'''The isinstance() function will tell us if an Object is an instance of a class.'''
# isinstance(object, type)

'''The issubclass() function will tell us if a subclass of another.'''
# issubclass(object,subclass)

'''__repr__ method returns a string that represents the object in a way that it can be recreated.'''
#  def __repr__(self):

'''__str__ method returns the user readable string form of an object that can be understood by the end users.'''
# def __str__(self):

'''__add__ method is called when the addition operator ( + ) is used with instances of your custom class.'''
# __add__
# print(int.__add__(1,2))
# print(str.__add__("A","B"))

'''__len__() method is a built-in Python method that returns the length of an object.'''
# __len__

'''Decorators allows you to modify or extend the behavior of functions or methods without changing their actual code. '''
# @property
# Accessing a method as an attribute.

'''setter allows you to customize how a property is modified. Imagine you're working on a data science project where you're dealing with temperature data. Using setters, you can automatically convert any temperature data to Fahrenheit when it's set.'''
# @Method_name.setter

'''deleter will delete the attribute, we call it with "del".'''
# @Method_name.setter
# def Method_name(self):
#     print("Delete Name")
#     self.first=None
#     self.last=None



'''Q-1.) Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details. Sample Employee Data:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"

1) Use the 'assign_department' method to change the department of an employee.
2) Use the 'print_employee_details' method to print the details of an employee.
3) The 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:

overtime = hours_worked - 50
Overtime amount = (overtime * (salary / 50))'''

# class Employee:
#     def __init__(self, emp_name, emp_id, emp_salary, emp_department):
#         self.emp_name=emp_name
#         self.emp_id=emp_id
#         self.emp_salary=emp_salary
#         self.emp_department=emp_department

#     def calculate_emp_salary(self, hours_worked):
#         if hours_worked>50:
#             overtime=(hours_worked)-50
#             overtime_amount=(overtime*(self.emp_salary/50))
#             total_salary=(self.emp_salary)+(overtime_amount)
#         else:
#             total_salary=self.emp_salary
#         return total_salary

#     def assign_department(self, new_department):
#         self.emp_department = new_department

#     def print_employee_details(self):
#         print(f"Employee's Name:{self.emp_name}")
#         print(f"Employee's ID:{self.emp_id}")
#         print(f"Employee's Salary:{self.emp_salary}")
#         print(f"Employee's Department:{self.emp_department}")

# employee_data = [
#     ["ADAMS","E7876",50000,"ACCOUNTING"],
#     ["JONES","E7499",45000,"RESEARCH"],
#     ["MARTIN","E7900",50000,"SALES"],
#     ["SMITH","E7698",55000,"OPERATIONS"]
# ]

# employees = []
# for data in employee_data:
#     emp = Employee(*data)
#     employees.append(emp)

# for emp in employees:
#     emp.print_employee_details()
#     print()

# employee = employees[0]
# employee.assign_department("HR")
# print("After changing department:")
# employee.print_employee_details()

# print()
# print(f"Calculating salary for employee {employee.emp_name}:")
# hours_worked = 55
# total_salary = employee.calculate_emp_salary(hours_worked)
# print(f"Total salary for {employee.emp_name} with {hours_worked} hours worked:{total_salary}.")


'''Q-2.) Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
Perform the following tasks now:
  1) Now add items to the menu.
  2) Make table reservations.
  3) Take customer orders.
  4) Print the menu.
  5) Print table reservations.
  6) Print customer orders.
Note: Use dictionaries and lists to store the data.'''

# class Restaurant:
#     def __init__(self):
#         self.menu_items={}
#         self.booked_tables={}
#         self.customer_orders=[]

#     def add_item_to_menu(self, item_name,item_price):
#         self.menu_items[item_name]=item_price

#     def book_table(self,table_number,customer_name):
#         if table_number not in self.booked_tables:
#             self.booked_tables[table_number]=customer_name
#             print(f"Table {table_number} booked for {customer_name}.")
#         else:
#             print(f"Table {table_number} is already booked.")

#     def customer_order(self,customer_name,items_ordered):
#         order={"customer_name":customer_name,"items_ordered":items_ordered}
#         self.customer_orders.append(order)
#         print(f"Order placed for {customer_name}:{','.join(items_ordered)}")

#     def print_menu(self):
#         print("Menu:")
#         for item, price in self.menu_items.items():
#             print(f"{item}: ₹{price}")

#     def print_table_reservations(self):
#         print("Table Reservations:")
#         for table, customer in self.booked_tables.items():
#             print(f"Table {table}: {customer}")

#     def print_customer_orders(self):
#         print("Customer Orders:")
#         for order in self.customer_orders:
#             print(f"{order['customer_name']} ordered: {', '.join(order['items_ordered'])}")

# restaurant = Restaurant()

'''Adding items to the menu.'''
# restaurant.add_item_to_menu("Dosa",80)
# restaurant.add_item_to_menu("Biryani",250)
# restaurant.add_item_to_menu("Samosa",10)
# restaurant.add_item_to_menu("Chole Bhature",40)
# restaurant.add_item_to_menu("Chai",15)

'''Making table reservations.'''
# restaurant.book_table(1,"Sangeeta")
# restaurant.book_table(2,"Bhawna")
# restaurant.book_table(1,"Chandni")
# print()

'''Taking customer's orders.'''
# restaurant.customer_order("Sangeeta",["Chai","Dosa"])
# restaurant.customer_order("Bhawna",["Samosa","Dosa"])
# restaurant.customer_order("Chandni",["Samosa","Biryani"])
# restaurant.customer_order("Nisha",["Chole Bhature","Chai"])
# print()

'''Printing menu, table reservations, and customer orders.'''
# restaurant.print_menu()
# print()
# restaurant.print_table_reservations()
# print()
# restaurant.print_customer_orders()


'''Q-3.) Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.'''

# class BankAccount:
#     def __init__(self,account_number,balance,date_of_opening,customer_name):
#         self.account_number=account_number
#         self.balance=balance
#         self.date_of_opening=date_of_opening
#         self.customer_name=customer_name

#     def account_details(self):
#         print("Account details of user:")
#         print(f"Account Holder:{self.customer_name}")
#         print(f"Account Number:{self.account_number}")
#         print(f"Date Of Opening:{self.date_of_opening}")
#         print(f"Account Balance:{self.balance}")

#     def deposit(self,amount):
#         if amount>0:
#             self.balance+=amount
#             print(f"Deposite of ₹{amount} successful.")
#         else:
#             print("Enter valid amount.")  

#     def withdraw(self,amount):
#         if amount>0:
#             if (amount<=self.balance):
#                 self.balance-=amount
#                 print(f"Withdrawal of ₹{amount} successful.")
#             else:
#                 print("Insufficient balance")
#         else:
#             print("Enter valid amount.")

#     def check_balance(self):
#         print(f"Account Balance for {self.customer_name} (Account Number:{self.account_number}) is ₹{self.balance}.")

# account1 = BankAccount(200012343297986,12000,"30-03-2023","Bhawna")

# account1.account_details()
# print()

# account1.deposit(5000)
# account1.check_balance()
# print()

# account1.withdraw(200)
# account1.check_balance()


'''Q-4.) Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods like add_item, update_item, and check_item_details.
   Note: Use a dictionary to store the item details, where the key is the item_id and the value is a dictionary containing the item_name, stock_count, and price.'''

# class Inventory:
#     def __init__(self):
#       self.items={}

#     def add_item(self,item_id,item_name,stock_count,price):
#       if item_id not in self.items:
#         self.items[item_id]={'Item Name':item_name,'Stock Count':stock_count,'Price':price}
#         print("Item added successfully.")
#       else:
#         print("Item ID already exists, modify existing item to add again.")
        
#     def update_item(self,item_id=None,item_name=None,stock_count=None,price=None):
#       if item_id in self.items:
#         item_details=self.items[item_id]
#         if item_name:
#             item_details['Item Name']=item_name
#         if stock_count is not None:
#             item_details['Stock Count']=stock_count
#         if price is not None:
#             item_details['Price']=price
#         else:
#           print("Item details updated successfully.")
#       else:
#         print("Item ID does not exist. Use add_item() to add a new item.")   

#     def check_item_details(self, item_id):
#       if item_id in self.items:
#         print(f"Item ID:{item_id}")
#         print(f"Item Name:{self.items[item_id]['Item Name']}")
#         print(f"Stock Count:{self.items[item_id]['Stock Count']}")
#         print(f"Price:{self.items[item_id]['Price']}")
#       else:
#         print("Item ID does not exist.")

# inventory = Inventory()

# inventory.add_item('201','Notebook',1000,20)
# inventory.add_item('300','Pen',5000, 10)

# print("Item details before update:")
# inventory.check_item_details('300')

# inventory.update_item('201',stock_count=200, price=30)
# print()

# print("Item details after update:")
# inventory.check_item_details('300')
# print()

# print("Item details for non-existing item:")
# inventory.check_item_details('103')


'''Q-4.) E-Commerce Website: 1.)Products already there
                     2.)Multiple functions 
                     3.)Add to cart
                     4.)Delete from cart
                     5.)Update quantity in cart
                     6.)Price for every item
                     7.)If total bill is more then or equal to Rs. 1000, give 5% discount on total bill
                     8.)Minimum order Rs 100
                     9.)Wishlist'''

# class Website:
#    def __init__(self):
#       self.products={} 
#       self.cart={} 
#       self.wishlist=[]

#    def add_product(self,name,price,quantity):
#       self.products[name]=(price,quantity)

#    def print_product(self):
#       print("Products:")
#       print()
#       for name,(price,quantity) in self.products.items():
#          print(f"{name}:₹{price}, Quantity:{quantity}")
#          print()   

#    def add_to_cart(self,name,quantity):
#       if name in self.products:
#          if self.products[name][1]>=quantity:
#             if name not in self.cart:
#               self.cart[name]=quantity
#               print(f"{name} added to the cart.")
#             else:
#                self.cart[name]+=quantity
#                print(self.cart[name])
#          else:
#             print(f"{name}'s quantity exceeds.")     
#       else:
#          print("Product not available.")

#    def remove_from_cart(self,name):
#       if name in self.cart:
#          del self.cart[name]
#          print(f"{name} removed from cart.")
#       else:
#          print("Product not in the cart.")

#    def update_quantity(self,name,quantity):
#       if name in self.cart:
#          self.cart[name]=quantity
#          print(f"Quantity of {name} updated to {quantity}.")
#       else:
#          print("Product not in the cart.") 

#    def calculate_bill(self):
#       total_bill=0
#       for name,quantity in self.cart.items():
#          price=self.products[name][0]
#          total_bill+=price*quantity 

#       if total_bill<100:
#          print("Minimum order amount not met.")
#       elif total_bill>=1000:
#          print(total_bill)
#          total_bill=total_bill-((5/100)*total_bill)
#          print(f"Total bill:{total_bill}")
#       else:
#          print(f"Total bill:{total_bill}") 
         
#    def add_to_wishlist(self,name):
#       if name not in self.wishlist:
#          self.wishlist.append(name)
#          print(f"{name} added to the wishlist.")
#       else:
#          print(f"{name} already in the wishlist.")

#    def remove_from_wishlist(self,name):
#       if name in self.wishlist:
#          self.wishlist.remove(name)
#          print(f"{name} removed from wishlist.")   
#       else:
#          print("Product not in wishlist.")

# ZoomBoomWebsite=Website()

# '''Add products.'''
# ZoomBoomWebsite.add_product("Cap",60,7)
# ZoomBoomWebsite.add_product("T-shirt",1500,100)
# ZoomBoomWebsite.add_product("Shoes",2000,50)
# ZoomBoomWebsite.add_product("Jeans",1000,100)
# ZoomBoomWebsite.add_product("Makeup",2000,1)
# ZoomBoomWebsite.add_product("Headphones",1000,1)
# ZoomBoomWebsite.add_product("Pen",20,1000)
# ZoomBoomWebsite.add_product("Notebook",100,100)

# '''Printing products.'''
# ZoomBoomWebsite.print_product()

# '''Add products to the cart.'''
# ZoomBoomWebsite.add_to_cart("Jeans",2)
# ZoomBoomWebsite.add_to_cart("Headphones",1)
# ZoomBoomWebsite.add_to_cart("Cap",1)
# ZoomBoomWebsite.add_to_cart("Notebook",5)
# print()

# '''Remove from the cart.'''
# ZoomBoomWebsite.remove_from_cart("Jeans")
# print()

# '''Update quantity in the cart.'''
# ZoomBoomWebsite.update_quantity("Notebook",3)
# print()

# '''Calculate the total bill.'''
# ZoomBoomWebsite.calculate_bill()
# print()

# '''Add products to wishlist.'''
# ZoomBoomWebsite.add_to_wishlist("Makeup")
# ZoomBoomWebsite.add_to_wishlist("Shoes")
# ZoomBoomWebsite.add_to_wishlist("Cap")
# print()

# '''Remove from wishlist.'''
# ZoomBoomWebsite.remove_from_wishlist("Cap")

# ZoomBoomWebsite.add_product("❤️",0,1)