from collections import deque

# Функція перевірки на паліндром
def is_palindrome(text):
    d= deque([char for char in text.lower() if char.isalpha()])
    while len(d)>1:
        if d.pop() != d.popleft():
            return False  
    return True
        

def main():
    # Перевірка паліндромів
    assert is_palindrome("Дід і дід") is True
    assert is_palindrome("І що сало? Ласощі…") is True
    assert is_palindrome("«Бувалу булаву б…»") is True
    assert is_palindrome("«Мило, — Галина до Данила, — голим!»") is True
    assert is_palindrome("«Бувалу булаву б…»") is True
    assert is_palindrome("Able was I ere I saw Elba") is True
    assert is_palindrome("God, a red nugget, a fat egg under a dog") is True
    assert is_palindrome("Lewd did I live, evil I did dwel") is True
    assert is_palindrome("May a moody baby doom a yam?") is True
    assert is_palindrome("Naomi, did I moan?") is True
    # Перевірка не паліндромів
    assert is_palindrome("Тільки уточнити") is False
    assert is_palindrome("Queue and deque") is False


if __name__=="__main__":
    main()
