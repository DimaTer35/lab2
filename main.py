def add(a, b):
    """Возвращает сумму двух чисел a и b. Проверяет, что входные данные являются числами."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Оба аргумента должны быть числами.")
    return a + b

if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))

def new_function():
    return "New feature added!"
