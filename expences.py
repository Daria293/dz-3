meal = input("Ваши траты на еду:")
transport = input("Ваши траты на транспорт:")
attractives = input("Ваши траты на развлечения:")
total = int(meal) + int(transport) + int(attractives)
middle = int(total) / 3
print("Общая сумма ваших трат:", total )
print("В среднем вы тратите:", middle)