# Global dictionary of products
products = {}
ADD = 1
SHOW = 2
SEARCH = 3
SEARCH_PRICE = 4

COL_NAME = 0
COL_PRICE = 1

def add_product():
    print('Enter product information')
    id = input('Enter product id: ')
    name = input('Enter product name: ')
    price = int(input('Enter product price: '))
    # product_list.append([id, name, price]) # 2d list
    products[id] = [name, price] # dictionary
    print('Product added')

def show_products():
    print('All products')
    for id in products:
        print(f'{id:5}{products[id][COL_NAME]:<15}{products[id][COL_PRICE]:>5}')

def search_product(exact=True):
    name = input('Enter product name to search: ')
    if exact:
        found_products = [p for p in products.items() if p[1][COL_NAME] == name] 
    else:
        found_products = [p for p in products.items() if name in p[1][COL_NAME]]
    print_products(found_products)

def search_by_price(less_than=True):
    price = int(input('Enter price to search: '))
    if less_than:
        found_products = [product for product in products.items() if product[1][1] < price]
    else:
        found_products = [product for product in products.items() if product[1][1] > price]
    print_products(found_products)

def print_products(products):
    if len(products) == 0:
        print('Product not found')
        return
    for product in products:
        print(f'{product[0]:5}{product[1][0]:<15}{product[1][1]:>5}') 

def change_price():
    id = int(input('Enter product id to change price: '))
    if id not in products:
        print('Product not found')
        return
    new_price = int(input('Enter new price: '))
    products[id][COL_PRICE] = new_price
    print('Price changed for product', id)

def delete_product():
    id = int(input('Enter product id to delete: '))
    if id not in products:
        print('Product not found')
        return
    del products[id]
    print('Product deleted')

def print_menu():
    print('1. Add product')
    print('2. Show products')
    print('3. Search product by name')
    print('4. Search product by price')
    print('5. Change price')
    print('6. Delete product')
    print('7. Exit')

def main_program():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == ADD:
            add_product()
        elif choice == SHOW:
            show_products()
        elif choice == SEARCH:
            print('1. Exact search')
            print('2. Partial search')
            search_choice = int(input('Enter your choice: '))
            search_product(search_choice == 1)
        elif choice == SEARCH_PRICE:
            print('1. Less than')
            print('2. More than')
            search_choice = int(input('Enter your choice: '))
            search_by_price(search_choice == 1)
        elif choice == 5:
            change_price()
        elif choice == 6:
            delete_product()
        elif choice == 7:
            running = False 
        else:
            print('Invalid choice')