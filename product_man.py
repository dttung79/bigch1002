# Global dictionary of products
products = {}
ADD = 1
SHOW = 2
SEARCH = 3
SEARCH_PRICE = 4

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
        print(f'{id:5}{products[id][0]:<15}{products[id][1]:>5}')

def search_product(exact=True):
    name = input('Enter product name to search: ')
    if exact:
        found_products = [product for product in products.items() if product[1][0] == name] 
    else:
        found_products = [product for product in products.items() if name in product[1][0]]
    if len(found_products) == 0:
        print('Product not found')
    else:
        for product in found_products:
            print(f'{product[0]:5}{product[1][0]:<15}{product[1][1]:>5}')

def search_by_price(less_than=True):
    pass

def change_price():
    pass

def delete_product():
    pass

def print_menu():
    pass

def main_program():
    running = True
    while running:
        print_menu()
    choice = int(input('Enter your choice: '))
    if choice == ADD:
        add_product()
    elif choice == SHOW:
        show_products()
    # continue ...