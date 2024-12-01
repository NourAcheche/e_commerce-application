import datetime#https://realpython.com/https://realpython.com/python-datetime/#:~:text=%3E%3E%3E%20date_string%20%3D%20%2201%2D31%2D2020%2014%3A45%3A37%22%0A%202%3E%3E%3E%20format_string%20%3D%20%22%25m%2D%25d%2D%25Y%20%25H%3A%25M%3A%25S%22
print("****Welcome to medipol Online Market****")
basket={}
products = [{"name": "Asparagus", "stock_Amount": 10, "price": 5},
            {"name": "Broccoli", "stock_Amount": 15, "price": 6},
            {"name": "carrots", "stock_Amount": 18, "price": 7},
            {"name": "apples", "stock_Amount": 20, "price": 5},
            {"name": "Banana", "stock_Amount": 10, "price": 8},
            {"name": "Berries", "stock_Amount": 30, "price": 3},
            {"name": "Eggs", "stock_Amount": 50, "price": 2},
            {"name": "Mixed fruit juice", "stock_Amount": 0, "price": 8},
            {"name": "fish stiks", "stock_Amount": 25, "price": 12},
            {"name": "ice cream", "stock_Amount": 32, "price": 6},
            {"name": "Apple juice", "stock_Amount": 40, "price": 7},
            {"name": "Orange juice", "stock_Amount": 30, "price": 8},
            {"name": "Grape juice", "stock_Amount": 10, "price": 9}]


class point:#because there is multiple user we use the class
    def _init_(self, user, password):
        self.user = user
        self.password = password


print("please log in by providing your user credentials:")
users = {"ahmet": "1234",#dictionary of the multiple users
         "zeynep": "4444",
         "admin": "qwerty"}
x = users.keys()#to get the keys of the dictionary such as ["ahmet","zeynep","admin"]


def search():#this function search for the product that the user enter in the list_dict products
    product_given = input("what are you searching for?")
    thelist = []#to keepe the information here
    for product in products:#condition to make sure that the given product is indeed in the dictionary list
        if product_given in product['name'] and product['stock_Amount'] > 0:#the stock_amount of the product has to be !=0
            thelist.append(product)#we save in the previous empty list
    return thelist#we will use it in another function but it doesn't show the result here


def log():#this function check if the user is entering the correct username and password
    user = input("enter username:")
    password = input("enter the password:")
    s = 1#this counter make sure that the user has only three attempts that why it starts from 1 (1,2,3)
    while s < 3:
        if user in x and users[user] == password:#check if the user name is in user dict keys and that the password is correct
            print("successfully logged in!")
            return user #the user entered the correct informations

        s = s + 1#if not it keeps moving on till the third attempt
        print("your user and/or password is not correct .please try again!")
        user = input("enter username:")
        password = input("enter the password:")
    print("your account has been blocked . please contact the administrator")#if he reaches three attempt and the third one is still wrong then he will be blocked
    return none# he didn't enter the system
def menu():#this function present the options for the user to choose from
    print("please choose one of the following services:")
    print("1.search for a product", "\n", "2.see Basket", "\n", "3.check out", "\n", "4.logout", "\n", "5.Exit", "\n")
if log():#the previous function log has as output booleen so it determines whether the user entered the system or not
    menu()#present the options
    options = [1, 2, 3, 4, 5]#the options number are from 1 to 5
    choice = int(input("your choice:"))#a int that the user going to enter
    if choice not in options:#if the number that he chose is part of the options list that he can access to the options
        print("enter a valid menu number")
    elif choice == 1:#if he pick option one he can pick a product from the dict-list product
        result = search()
        if result:#it will search for the that the user entered in dict_list products
            print("Found similar items:")#and if he founf something similar he will print the result
            s = 1
            for product in result:
                print(f"{s}. {product['name']}${product['price']}")
                s = s + 1
        else:
            print("No matching products found.")#if the product is not in dict_list products then the system will avert you
    elif choice == 2:#if the user pick the second option he will see the products that he picked
        basket_check()
    elif choice == 3:
        print("option 3 is chosen ")
    elif choice == 4:
        print("option 4 is chosen ")
    elif choice == 5:
        print("option 5 is chosen ")
    else:
        print("Invalid option .please enter another option")#if he enterd a number other than the 5 options he have to choose another one
else:
    print("Invalid username or password . login failed")#or he can t log in)

def add_in_basket(result, basket):#this function  add the product that the user picked in the basket
    a = int(input("Please select which item you want to add to your basket (Enter 0 for the main menu)"))
    if a==0:#if the user doesn't select anything then the system will show him an empty basket with 0 amount in it
        menu()
    elif 0 < a <= len(result):#the number that the user will select has to be in the list of the product that the user serched
        f = result[a - 1]#we remive the index from the list
        amount = int(input(f"Adding {f['name']}. Enter Amount: "))
        if amount <= f['stock_Amount']:#if this product on stock
            if f['name'] in basket:
                basket[f['name']]['amount'] += amount#if the product in the basket
            else:
                basket[f['name']] = {'price': f['price'], 'amount': amount}
            print(f"Added {f['name']} into your Basket.")#but if gthe product is not in the basket add it
        else:
            print(f"Sorry! The amount exceeds the limit. Please try again with a smaller amount.")#if the user pick a number higher the stock of this number warn him to give a smaller number
    else:
        print("Invalid selection. Please provide a valid item number.")
add_in_basket(result, basket)
print("going back to the main menu")
menu()
choice = int(input("your choice:"))
def basket_check():
    if not basket:
        print("Your basket is empty. Total 0$")
    else:
        total = 0
        s=1
        print("Your basket contains:")
        for  item, details in basket.items():
            items=details['price'] * details['amount']
            total +=items
            print(f"{s}.{item} price={details['price']}$ amount={details['amount']} total={details['price'] * details['amount']}$")
            s=s+1
        print(f"Total {total}$")
    menu()
basket_check()
def basket_sub_menu():
    print("please choose an option")
    print("1.Update amount")
    print("2.Remove an item")
    print("3.check out")
    print("go back to the main menu")
basket_sub_menu()
def update():
    print("Please select which item to change its amount:")
    s=1
    for item, details in basket.items():
        print(f"{s}.{item} price={details['price']}$ amount={details['amount']} total={details['price'] * details['amount']}$")
        s=s+1
    l = int(input("Your selection: "))
    if  0 < int(l) <= len(basket):
        m = list(basket.keys())[l-1]
        n_amount = int(input("Please type the new amount for {m}: "))

        if n_amount <= m['stock_amount']:
            basket[m]['amount'] = n_amount
            print(f"Your basket now contains:")
            basket_check()
        else:
            print(f"Sorry! The amount exceeds the limit. Please try again with a smaller amount.")
            update()
    else:
        print("Invalid selection. Please provide a valid item number.")
        update()
options = [1, 2, 3, 4, 5]
choice = int(input("your choice:"))
if choice not in options:
    print("enter a valid menu number")
elif choice == 1:
    update()
elif choice == 2:
    delete()
elif choice == '3':
    check_out()
elif choice == '4':
    menu()
else:
    print("Invalid menu entry. Please provide a valid menu number.")
    basket_sub_menu()

def delete():
    print("Please select which item to remove:")
    for i, (item, details) in enumerate(basket.items(), start=1):
        print(
            f"{i}.{item} price={details['price']}$ amount={details['amount']} total={details['price'] * details['amount']}$")

    choice = input("Your selection: ")

    if choice.isdigit() and 0 < int(choice) <= len(basket):
        selected_item = list(basket.keys())[int(choice) - 1]
        del basket[selected_item]
        print(f"Your basket now contains:")
        basket_check()
    else:
        print("Invalid selection. Please provide a valid item number.")
        delete()

def check_out():
    if not basket:
        print("Your basket is empty. Total 0$")
        basket_check()
        return

    print("Processing your receipt...")
    print("*** Medipol Online Market ****")
    print("**************")
    print("444 8 544")
    print("medipol.edu.tr")
    print("————————————")
    total = 0
    for item, details in basket.items():
        print(f"{item} {details['price']}$ amount={details['amount']} total={details['price'] * details['amount']}$")
        total += details['price'] * details['amount']
        product[item]['stock'] -= details['amount']
    print("————————————")
    print(f"Total {total}$")
    print("————————————")
    print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M"))
    print("Thank You for using our Market!")

    # Reset the basket
    basket.clear()
    menu()
def activate_account():
    print("Activate User Account")
    activate = input("Enter the username to activate: ")

    if activate in users and users[activate]['blocked']:
        users[activate]['blocked'] = False
        print(f"{activate}'s account has been activated successfully.")
    else:
        print(f"User '{activate}' not found or account is not blocked.")


def deactivate_account():
    print("Deactivate User Account")
    deactivate = input("Enter the username to deactivate: ")

    if deactivate in users and not users[deactivate]['blocked']:
        users[deactivate]['blocked'] = True
        print(f"{deactivate}'s account has been deactivated successfully.")
    else:
        print(f"User '{deactivate}' not found or account is already blocked.")


def add_user():
    print("Add User")
    new_username = input("Enter the new username: ")

    if new_username in users:
        print(f"User '{new_username}' already exists.")
        return

    new_password = input("Enter the new password: ")
    users[new_username] = {'password': new_password, 'attempts': 0, 'blocked': False}
    print(f"User '{new_username}' has been added successfully.")


def delete_previoususer():
    print("Remove User")
    user_remove = input("Enter the username to remove: ")

    if user_remove in users and user_remove != 'admin':
        del users[user_remove]
        print(f"User '{user_remove}' has been removed successfully.")
    else:
        print(f"Cannot remove user '{user_remove}'. User not found or cannot remove admin.")
if log:
    if log == 'admin':
        # Admin menu
        print(
            f"Welcome, {log}! Please choose one of the following options by entering the corresponding menu number.")
        print("1. Activate User Account")
        print("2. Deactivate User Account")
        print("3. Add User")
        print("4. Remove User")
        print("5. Logout")
        print("6. Exit")

        admin_choice = input("Your Choice: ")

        if admin_choice == '1':
            activate_account()
        elif admin_choice == '2':
            deactivate_account()
        elif admin_choice == '3':
            add_user()
        elif admin_choice == '4':
            delete_previoususer()
        elif admin_choice == '5':
            break   # Go back to login function
        elif admin_choice == '6':
            exit()
        else:
            print("Invalid menu entry. Please provide a valid menu number.")
    else:
        # Show user menu
        menu()
        user_choice = input("Your Choice: ")

        if user_choice == '1':
            search_result = search()
            if search_result:
                add_in_basket(search_result, basket)
        elif user_choice == '2':
            basket_check()
        elif user_choice == '3':
            # Implement checkout functionality
            pass
        elif user_choice == '4':
            break
        else:
            print("Invalid menu entry. Please provide a valid menu