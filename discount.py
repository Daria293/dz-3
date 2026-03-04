price = input("Цена товара:")
discount = input("Скидка:")
price2 = int(price) - (int(price) / 100 * int(discount))
print("Цена со скидкой:", price2)