#Спросить почему используется двойное равно ==
#Спросить зачем создается item_from_apple = None


def main():
    order = {
            "Продукт": None, 
            "Количество" : 0,
            "Общая сумма" : 0
            }

    appleProducts = [
                {"Продукт": "iphone", "Цена" : 8},
                {"Продукт": "macbook", "Цена" : 1200},
                {"Продукт": "airpods", "Цена" : 500}
                ]

    print ("Здравствуйте! это магазин iMardan.\n")
    choices = ["1-Купить", "2-Убрать", "3-Корзина", "4-Выйти"]

#def select():
    for choice in choices:
        a = input(f"Выберите цифру?\n {choices}\n")

        if a == "1":
            print (appleProducts)
            productName = input("Введите название продукта: ")
            productNumber = int(input("Сколько штук добавить в корзину?"))

            for item in appleProducts:
                if item["Продукт"] == productName:
                    order ["Продукт"] = productName
                    order ["Количество"] = productNumber
                    order ["Общая сумма"] = int(item["Цена"]) * productNumber

        elif a == "3":
             print (order)

        elif a == "4":
            break

        else:
            print(f"Напишите цифру из списка\n ")
main()
