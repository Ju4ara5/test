expression = input('Выражение: ')


def parentheses(expression):
    expression = ''.join(elem for elem in expression if elem in '({[]})')
    print(expression)

    while expression:
        bo_ol = True
        for elem in '()', '{}', '[]':
            if elem in expression:
                expression = expression.replace(elem, '')
                bo_ol = False
        if bo_ol:
            print('Не верно')
            return False

    print('Верно')
    return True


parentheses(expression)

"""
Убираем всё кроме скобок. 
Удаляем пустые скобки, пока выражение не останется пустым. 
Однако если выражение что-то содержит и в нем нет пустых скобок -> return False
"""
