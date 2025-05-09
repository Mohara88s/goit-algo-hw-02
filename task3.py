from collections import deque

# Словник відповідності дужок
brackets_dict = {'{':'}','[':']','(':')'}

# Функція перевірки на симетричність дужок
def is_symmetry_of_brackets(text):
    # Створюю стек
    stack = []
    # Проходжусь по тексту
    for s in text:
        # За умови що дужка відкриваюча додаю на стек
        if s in brackets_dict.keys():
            stack.append(s)
        # За умови що дужка закриваюча перевіряю чи є відповідна відкриваюча останньою в стеку, та зараховую пару, видаленням відкриваючої дужки зі стеку. Якщо пари нема то помилка.
        if s in brackets_dict.values():
            if len(stack) == 0:
                print("Error with brackets! You should open then close!")
                return False
            elif brackets_dict[stack[-1]] == s:
                stack.pop()
            else:
                print("Error with symmetry of brackets!")
            
    # Яккщо лишилися відкриті дужки то помилка
    if len(stack) != 0:
        print("Error with the number of brackets!")
        return False
    # Якщо дійшли сюди то ми молодці, бо магія дужок виконалася і прекрасна симетрія підтверджена!
    # :)
    # Гарного дня!
    return True



def main():
    # Перевірки
    assert is_symmetry_of_brackets("Дід( і )дід") is True
    assert is_symmetry_of_brackets("Дід( і дід") is False
    assert is_symmetry_of_brackets("Дід( {і} )дід") is True
    assert is_symmetry_of_brackets("Дід{(} і )дід") is False

    # Перевірки згідно прикладу
    assert is_symmetry_of_brackets("( ){[ 1 ]( 1 + 3 )( ){ }}:") is True
    assert is_symmetry_of_brackets("( 23 ( 2 - 3);:") is False
    assert is_symmetry_of_brackets("( 11 }:") is False

if __name__=="__main__":
    main()
