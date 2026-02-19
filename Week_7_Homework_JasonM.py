
#Pizzas are finished

pizza_orders = ["pepperoni", "pineapple", "cheese", "Hawaiian", "Meat Lovers"]
finished_pizzas = []
while pizza_orders:
    current_pizza = pizza_orders.pop(0)
    print(f"Your {current_pizza} Pizza is finished!.")
    finished_pizzas.append(current_pizza)
    
#Pizzas have been made

print("\nThe following pizzas have been made:")
for finished_pizza in finished_pizzas:
    print(f"The {finished_pizza} Pizza has been made")