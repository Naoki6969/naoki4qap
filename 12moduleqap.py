per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("Необходимо ввести сумму депозита:"))
deposit = [money*perst/100 for perst in per_cent.values()]
print(deposit)
print("Максимальная сумма, которую вы можете заработать —", max(deposit))