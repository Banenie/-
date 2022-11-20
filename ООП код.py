#автомат для заказа напитков при помощи классов
class Drink:
    def __init__(self):
        self.object = "Напиток"

    def lid(self):
        print("Не забудьте надеть крышку на стакан", "\n")

    def accepting(self):
        print("----------------------------------------")
        print("Ваш заказ принят, ожидайте", "\n")

    def bye(self):
        print("Спасибо за заказ, хорошего дня!")
        print("----------------------------------------")

class HotDrink(Drink):
    def __init__(self):
        super().__init__()
        self.type_of_drink = "Горячий напиток"
        self.cost = "100р."

    def warning(self):
        print("Внимание! Напиток горячий", "\n")

class ColdDrink(Drink):
    def __init__(self):
        super().__init__()
        self.type_of_drink = "Холодный напиток"
        self.cost = "80р."

    def warning(self):
        print("Не забудьте взять трубочку", "\n")

class Coffee(HotDrink):
    def __init__(self):
        super().__init__()
        self.__composition = ["Кофейные зерна", "Молоко"]
        self.time = "2 минуты"

    def sugar(self):
        sugar = int(input("Хотите ли вы добавить сахар в напиток? \nДа - 1 \nНет - 2\nВвод: "))
        if sugar == 1:
            self.__composition.append("сахар")
        elif sugar != 2:
            print("----------------------------------------")
            print("Некорректный ввод")
            print("----------------------------------------")
            breakpoint()

class Tea(HotDrink):
    def __init__(self):
        super().__init__()
        self.__composition = ["Чайные листья",]
        self.time = "1 минута"

    def sugar(self):
        sugar = int(input("Хотите ли вы добавить сахар в напиток? \nДа - 1 \nНет - 2\nВвод: "))
        if sugar == 1:
            self.__composition.append("сахар")
        elif sugar != 2:
            print("----------------------------------------")
            print("Некорректный ввод")
            print("----------------------------------------")
            breakpoint()

class MilkShake(ColdDrink):
    def __init__(self):
        super().__init__()
        self.__composition = ["Усилители вкуса", ""]
        self.time = "3 минуты"

    def milk(self):
        milk = int(input("Хотите ли вы альтернативное молоко? \nДа - 1 \nНет - 2\nВвод: "))
        if milk == 1:
            milk = int(input("Какое вы бы хотели? \nКокосовое - 1 \nМиндальное - 2 \n Банановое - 3\nВвод: "))
            if milk == 1:
                self.__composition.append("Кокосовое молоко")
            elif milk == 2:
                self.__composition.append("Миндальное молоко")
            elif milk == 3:
                self.__composition.append("Банановое молоко")
            else:
                print("----------------------------------------")
                print("Некорректный ввод")
                print("----------------------------------------")
                breakpoint()
        if milk == 2:
            self.__composition.append("Молоко коровье")
        else:
            print("----------------------------------------")
            print("Некорректный ввод")
            print("----------------------------------------")
            breakpoint()

    def taste(self):
        taste = int(input("Выберите вкус милкшейка \nБанановый - 1 \nКлубничный - 2 \nВвод: "))
        if taste == 1:
            self.__composition.pop(-1)
            self.__composition.append("Банан")
        elif taste == 2:
            self.__composition.pop(-1)
            self.__composition.append("Клубника")
        else:
            print("----------------------------------------")
            print("Некорректный ввод")
            print("----------------------------------------")
            breakpoint()

class Soda(ColdDrink):
    def __init__(self):
        super().__init__()
        self.__composition = []
        self.time = "выдается сразу"

    def taste(self):
        taste = int(input("Выберите газировку \nCocaCola - 1 \nFanta - 2 \nВвод: "))
        if taste == 1:
            self.__composition.append("CocaCola")
        elif taste == 2:
            self.__composition.append("Fanta")
        else:
            print("----------------------------------------")
            print("Некорректный ввод")
            print("----------------------------------------")
            breakpoint()


answer = int(input("Здравствуйте, вы хотите что-то заказать?\nДа - 1\nНет - 2\nВвод: "))
if answer == 2:
    print("Зачем пришел?")
elif answer == 1:
    answer = int(input("Выберите тип напитка: \nГорячий напиток - 1\nХолодный напиток - 2\nВвод: "))
    if answer == 1:
        answer = int(input("Выберите напиток: \nКофе - 1\nЧай - 2\nВвод: "))
        if answer == 1:
            answer = Coffee()
            answer.sugar()

            answer.accepting()
            print("Стоимость -", answer.cost, "\n")
            print("Примерное время приготовления -", answer.time, "\n")
            answer.lid()
            answer.warning()
            answer.bye()
        elif answer == 2:
            answer = Tea()
            answer.sugar()

            answer.accepting()
            print("Стоимость -", answer.cost, "\n")
            print("Примерное время приготовления -", answer.time, "\n")
            answer.lid()
            answer.warning()
            answer.bye()
        else:
            print("----------------------------------------")
            print("Некорректный ввод")
            print("----------------------------------------")
            breakpoint()
    elif answer == 2:
        answer = int(input("Выберите напиток: \nМилкшейк - 1\nГазировка - 2\nВвод: "))
        if answer == 1:
            answer = MilkShake()
            answer.taste()
            answer.milk()

            answer.accepting()
            print("Стоимость -", answer.cost, "\n")
            print("Примерное время приготовления -", answer.time, "\n")
            answer.lid()
            answer.warning()
            answer.bye()
        elif answer == 2:
            answer = Soda()
            answer.taste()
            answer.accepting()
            print("Стоимость -", answer.cost, "\n")
            print("Примерное время приготовления -", answer.time, "\n")
            answer.lid()
            answer.warning()
            answer.bye()
        else:
            print("----------------------------------------")
            print("Некорректный ввод")
            print("----------------------------------------")
            breakpoint()
    else:
        print("----------------------------------------")
        print("Некорректный ввод")
        print("----------------------------------------")
        breakpoint()
else:
    print("----------------------------------------")
    print("Некорректный ввод")
    print("----------------------------------------")
    breakpoint()
