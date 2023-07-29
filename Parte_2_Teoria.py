# Libreria para leer toda la simbologia
import codecs

# Creacion del stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
# Funcion de balanceo 
def is_balanced(expression):
    stack = Stack()
    # Indica que se abren parentesis, corchetes o llaves
    opening_brackets = "([{"
    # Indica que se cierran porque encontraron su pareja
    closing_brackets = ")]}"
    steps = []
    
    # Ciclo para recorrer todos los caracteres
    for char in expression:
        steps.append(str(stack.items))
        # Si hay uno de estos "([{" lo agrega al stack
        if char in opening_brackets:
            stack.push(char)
        # Si encuentra la pareja ")]}" lo quita del stack
        elif char in closing_brackets:
            if stack.is_empty() or closing_brackets.index(char) != opening_brackets.index(stack.pop()):
                return False, steps
    return stack.is_empty(), steps

# Abre el archivo utilizando el codec utf-8 y les coloca el formato
def main(file_path):
    with codecs.open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            expression = line.strip()
            is_balanced_result, steps = is_balanced(expression)
            print(f"Expresion: {expression}")
            print(f"Esta balanceada?: {'Si' if is_balanced_result else 'No'}")
            print("Steps:")
            for index, step in enumerate(steps, start=1):
                print(f"Paso {index}: {step}")
            print("-" * 40)

if __name__ == "__main__":
    file_path = "expresiones.txt"  
    main(file_path)
