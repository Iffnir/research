# -------------------------<<<<< Grocery Item List & Cost >>>>>-------------------------
# -------------------------<<<<<       Version 1.0        >>>>>-------------------------

# -------------------------<<<<< Calculate Function >>>>>-------------------------
def calculate(item_list, item_find):
    item_price = float(item_list[item_find + 1])
    item_amount = int(input(f"How many {item_list[item_find]} do you want: "))
    item_cost = item_price * item_amount
    item_total = f"{item_list[item_find]}({item_amount})"
    cartitems.append(item_total)
    return item_cost


# -------------------------<<<<< Start of Main >>>>>-------------------------
# -------------------------<<<<< Item Lists >>>>>-------------------------
fruit = ["banana", 2.00, "avocado", 1.50, "oranges", 1.50, "apples", 2.00, "kiwi", 1.50]
vege = ["onions", 2.50, "cucumber", 5.25, "potatoes", 3.50, "lettuce", 4.50, "salad mix", 4.00]
deli = ["ham", 4.00, "salmon", 8.00, "sausages", 8.00, "salami", 5.50, "mussels", 8.00]
# -------------------------<<<<< Cart Variables >>>>>-------------------------
cartprice = 0
cartitems = []
# -------------------------<<<<< Start Main Menu Loop >>>>>-------------------------
while True:
    # -------------------------<<<<< Print 1st Level menu to screen >>>>>-------------------------
    print("\nSelect Area to Shop")
    print("(F)ruit")
    print("(V)egetables")
    print("(D)elicatessan")
    print("E(x)it")
    area = input("Enter letter of area to shop: ").lower()
    # -------------------------<<<<< Check if input is a Number >>>>>-------------------------
    if area.isnumeric():
        print("Letter NOT Number")
        continue
    # -------------------------<<<<< Check if input is longer than a single char >>>>>-------------------------
    # -------------------------<<<<< If it is longer slice of only the first chat >>>>>-------------------------
    if len(area) > 1:
        area = area[0]
    # -------------------------<<<<< Main IF-ELIF-ELSE check of input >>>>>-------------------------
    if area == "f":
        print("\nFruit Section")
        print("(A)pples")
        print("A(v)ocado")
        print("(B)anana")
        print("(K)iwifruit")
        print("(O)ranges")
        print("(G)o Back")
        fruit_choice = input("Enter Fruit letter: ").lower()
        # -------------------------<<<<< Check if input is longer than a single char >>>>>-------------------------
        # -------------------------<<<<< If it is longer slice of only the first chat >>>>>-------------------------
        if len(fruit_choice) > 1:
            fruit_choice = fruit_choice[0]
        # -------------------------<<<<< Create List of possible choices >>>>>-------------------------
        choices = ["a", "v", "b", "k", "o", "g"]
        # -------------------------<<<<< Test input against possible choices >>>>>-------------------------
        # -------------------------<<<<< Return to Main Menu Loop >>>>>-------------------------
        if fruit_choice not in choices:
            print("Selection Error")
            continue
        # -------------------------<<<<< Search List for "item" and get INDEX value >>>>>-------------------------
        elif fruit_choice == "a":
            fruit_find = fruit.index("apples")
        elif fruit_choice == "v":
            fruit_find = fruit.index("avocado")
        elif fruit_choice == "b":
            fruit_find = fruit.index("banana")
        elif fruit_choice == "k":
            fruit_find = fruit.index("kiwi")
        elif fruit_choice == "o":
            fruit_find = fruit.index("oranges")
        else:
            continue
        # -------------------------<<<<< Send data to Calculate function >>>>>-------------------------
        fruit_cost = calculate(fruit, fruit_find)
        cartprice += fruit_cost
        # -------------------------<<<<< Format values as Currency >>>>>-------------------------
        money = "${:,.2f}".format(cartprice) # Formatting the cart price with two decimal points
        print(f"\nCost so far = {money}")
        print(f"Cart items = {cartitems}")

    # -------------------------<<<<< RINSE & REPEAT >>>>>-------------------------
    elif area == "v":
        print("\nVegetable Section")
        print("(C)ucumber")
        print("(L)ettuce")
        print("(O)nions")
        print("(P)otatoes")
        print("(S)alad Mix")
        print("(G)o Back")
        vege_choice = input("Enter Vegetable letter: ").lower()

        if len(vege_choice) > 1:
            vege_choice = vege_choice[0]

        choices = ["c", "l", "o", "p", "s", "g"]

        if vege_choice not in choices:
            print("Selection Error")
            continue
        elif vege_choice == "c":
            vege_find = vege.index("cucumber")
        elif vege_choice == "l":
            vege_find = vege.index("lettuce")
        elif vege_choice == "o":
            vege_find = vege.index("onions")
        elif vege_choice == "p":
            vege_find = vege.index("potatoes")
        elif vege_choice == "s":
            vege_find = vege.index("salad mix")
        else:
            continue

        vege_cost = calculate(vege, vege_find)
        cartprice += vege_cost

        money = "${:,.2f}".format(cartprice)
        print(f"\nCost so far = {money}")
        print(f"Cart items = {cartitems}")

    # -------------------------<<<<< RINSE & REPEAT >>>>>-------------------------
    elif area == "d":
        print("\nDelicatessan")
        print("(H)am")
        print("(M)ussels")
        print("(S)alami")
        print("Sa(L)mon")
        print("Sa(U)sages")
        print("(G)o Back")
        deli_choice = input("Enter Food letter: ").lower()

        if len(deli_choice) > 1:
            deli_choice = deli_choice[0]

        choices = ["h", "m", "s", "l", "u", "g"]

        if deli_choice not in choices:
            print("Selection Error")
            continue
        elif deli_choice == "h":
            deli_find = deli.index("ham")
        elif deli_choice == "m":
            deli_find = deli.index("mussels")
        elif deli_choice == "s":
            deli_find = deli.index("salami")
        elif deli_choice == "l":
            deli_find = deli.index("salmon")
        elif deli_choice == "u":
            deli_find = deli.index("sausages")
        else:
            continue

        deli_cost = calculate(deli, deli_find)
        cartprice += deli_cost

        money = "${:,.2f}".format(cartprice)
        print(f"\nCost so far = {money}")
        print(f"Cart items = {cartitems}")

    else:
        break

money = "${:,.2f}".format(cartprice)
print("\nThank you for shopping with us.")
print(f"Total cost = {money}")
print(f"Items bought = {cartitems}")