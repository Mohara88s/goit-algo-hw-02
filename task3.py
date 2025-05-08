from collections import deque

# Словник відповідності дужок
brackets_dict = {'{':'}','[':']','(':')'}

# Функція перевірки на симетричність дужок
def is_symmetry_of_brackets(text):
    stack = []
    for s in text:
        print(s)
        if s in brackets_dict.keys():
            stack.append(s)
        if s in brackets_dict.values():
            if len(stack) == 0:
                print("Error with brackets! You should open then close!")
                return False
            elif brackets_dict[stack[-1]] == s:
                stack.pop()
            else:
                print("Error with symmetry of brackets!")
            
        
        print(stack)

    if len(stack) != 0:
        print("Error with the number of brackets!")
        return False
    
    return True


        

def main():
    string = "І (що сало? Ласощі…)"
    is_symmetry_of_brackets(string)

if __name__=="__main__":
    main()
