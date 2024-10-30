import random

# karātavu pakāpes #

def meginajumi(attempts):
    stages = [
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[attempts]

# iespējamie vārdi #

def vardini():
    words = ['kartupelis', 'tomats', 'burkans', 'sipols', 'kiploks', 'selerija', 'pretpulkstenraditajvirziens', 'saursliezudzelzcels']
    return random.choice(words).lower()

# spele #

def spele():
    word = vardini()
    word_completion = "_" * len(word)  
    guessed = False
    guessed_letter = []  
    guessed_word = []  
    attempts = 6  


    print("sākam spēli!")
    print(meginajumi(attempts))
    print(word_completion)
    print("\n")

#

    while not guessed and attempts > 0:
        guess = input("mini burtu!").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letter:
                print(f"tu jau esi minējis {guess}!")
            elif guess not in word:
                print(f"{guess} nav šajā vārdā!")
                attempts -= 1
                guessed_letter.append(guess)
            else:
                print(f"apsveicu! {guess} ir šajā vārdā!")
                guessed_letter.append(guess)
                word_as_list = list(word_completion)  
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_word:
                print(f"tu jau esi minējis {guess}!")
            elif guess != word:
                print(f"{guess} nav pareizs vārds!")
                attempts -= 1
                guessed_word.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("ta nu gan nevar")
            
        print(meginajumi(attempts))
        print(word_completion)
        print("\n")
    
    if guessed:
        print(f"apsveicu! tu uzminēji vārdu '{word}'!")
    else:
        print(f"Nepareizi!!! vārds bija '{word}'! Mēģini vēlreiz!")

if __name__ == "__main__":
    spele()
