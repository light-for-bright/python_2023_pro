# 1
class SchoolStudent:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def greeting(self):
        print(f"Привет, я {self.name}, учусь в {self.grade} классе!")

student = SchoolStudent("Иван", 5)
student.greeting()

# 2
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} издает звук: {self.sound}")

dog = Animal("Собака", "Гав-гав!")
cat = Animal("Кошка", "Мяу-мяу!")
dog.make_sound()
cat.make_sound()

# 3
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Книга: {self.title}, Автор: {self.author}")

book = Book("Гарри Поттер", "Джоан Роулинг")
book.display_info()

# 4
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def introduce(self):
        print(f"Этот фрукт - {self.name}, его цвет {self.color}.")

apple = Fruit("Яблоко", "красный")
banana = Fruit("Банан", "желтый")
apple.introduce()
banana.introduce()

# D.1
class FootballPlayer:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.goals = 0

    def score_goal(self):
        self.goals += 1

player = FootballPlayer("Лионель Месси", "нападающий")
player.score_goal()
player.score_goal()
print(f"{player.name} забил {player.goals} голов.")

# D.2
class CoffeeMachine:
    def __init__(self):
        self.water = 1000  # мл
        self.coffee = 200  # гр

    def make_coffee(self):
        if self.water >= 200 and self.coffee >= 20:
            self.water -= 200
            self.coffee -= 20
            return "Кофе готов!"
        else:
            return "Ошибка: недостаточно ингредиентов."

coffee_machine = CoffeeMachine()
print(coffee_machine.make_coffee())

# D.3
class OnlineStore:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)

    def checkout(self):
        total_price = sum(item["price"] for item in self.cart)
        return f"Заказ оформлен! Общая сумма заказа: {total_price} руб."

    def display_cart(self):
        print("Список товаров в корзине:")
        for item in self.cart:
            print(f"{item['name']} - {item['price']} руб.")

store = OnlineStore("Мой магазин")
store.add_to_cart({"name": "Футболка", "price": 500})
store.add_to_cart({"name": "Джинсы", "price": 1000})
store.display_cart()
print(store.checkout())
