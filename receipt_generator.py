foods = []
prices = []
total = 0


while True:
    food = input("Enter a food to buy (q to Quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: Rs. "))
        foods.append(food)
        prices.append(price)

print("----------YOUR CART-----------")

for food in foods:
    print(food)

for price in prices:
    total += price

print()
print(f"Your total is : Rs. {total}") 
print("Thanks for Shopping !!")