import random

# --- Función para obtener la palabra según el archivo ---
def get_word(file_name):
    with open(f'./{file_name}.txt', 'r', encoding='utf-8') as f:
        words = f.read().split('\n')
    # Filtramos líneas vacías
    words = [w for w in words if w != '']
    index = random.randint(0, len(words) - 1)
    return words[index].lower()

# --- Función para dibujar el ahorcado ---
def draw(errors):
    # Usamos if/else simple para mantener la compatibilidad
    if errors == 0:
        print('''
    |-----------------------
    |           
    |           
    |         
    |         
    |_______________________
    ''')
    elif errors == 1:
        print('''
    |-----------------------
    |           |
    |           
    |         
    |         
    |________________________    
    ''')
    elif errors == 2:
        print('''
    |-----------------------
    |           |
    |           O
    |         
    |         
    |_______________________   
    ''')
    elif errors == 3:
        print('''
    |-----------------------
    |           |
    |           O
    |         /|\\
    |         
    |_______________________    
    ''')
    elif errors == 4:
        print('''
    |-----------------------
    |           |
    |           O
    |         /|\\
    |           |
    |         
    |________________________    
    ''')
    elif errors == 5:
        print('''
    |-----------------------
    |           |
    |           O
    |         /|\\
    |           |
    |         / \\
    |________________________    
    ''')

# --- Función para mostrar guiones y letras acertadas ---
def write_word(word, chars=''):
    dashed_word = ''
    for char in word:
        if char in chars:
            dashed_word += char + ' '
        else:
            dashed_word += '_ '
    return dashed_word

# --- Menú para elegir categoría ---
def menu():
    print('\n--- SELECCIONA UNA CATEGORÍA ---')
    print('1. Comidas')
    print('2. Animales')
    print('3. Lugares')
    print('4. Cosas')
    print('5. Nombres')
    
    opcion = input('Elige un número (1-5): ')
    
    opciones = {
        '1': 'comidas',
        '2': 'animales',
        '3': 'lugares',
        '4': 'cosas',
        '5': 'nombres'
    }
    
    return opciones.get(opcion, 'comidas') # Por defecto comida

# --- Función principal del juego ---
def game():
    categoria = menu()
    word = get_word(categoria)

    print(f'\nCategoría seleccionada: {categoria.upper()}')
    print('¡Juego del ahorcado!')
    print('Adivina la palabra')
    print(write_word(word))

    errors = 0
    chars = ''

    while True:
        char = input('\nIngrese una letra (o la palabra completa): ').lower()
        
        # Validar entrada
        if len(char) == 1 and char.isalpha():
            if char in chars:
                print("Ya intentaste esa letra.")
                continue
            chars += char
            
            if char not in word:
                draw(errors)
                errors += 1
        elif char == word:
            print(f'¡Felicidades, adivinaste! La palabra era: {word}')
            break
        else:
            print("Entrada no válida.")
            continue

        dashed_word = write_word(word, chars)
        print(dashed_word)

        if dashed_word.replace(' ', '') == word:
            print('¡Ganaste! 🎉')
            break
            
        if errors == 6:
            print('Perdiste 💀')
            print(f'La palabra era: {word}')
            break
        
if __name__ == "__main__":
    game()