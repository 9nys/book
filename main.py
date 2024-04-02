class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


# Приклад використання:
book1 = Book("Чуже завжди краще", "Валерія Дражинська")
book2 = Book("Межі пристойності", "Лана Вернік")

print("Чи рівні книги book1 та book2?", book1 == book2)
print("Чи нерівні книги book1 та book2?", book1 != book2)
