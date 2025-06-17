import time

class Dog:

    def __init__(self, dog_name: str, breed: str, color: str, ) -> None:
        self.breed = breed
        self.color = color
        self.dog_name = dog_name
        self.is_barking: bool = False
        self.is_eating: bool = False
        self.is_playing: bool = False
    
    # FUNCTION FOR BARKING 
    def bark(self):

        if self.is_barking == False:
            print(f'{self.dog_name} is now barking. Woof woof!')
            self.is_barking = True
        else: # Entered "start barking" even if dog is already barking
            print(f'{self.dog_name} is already barking!')

    # FUNCTION FOR STOP BARKING
    def stop_barking(self):
        
        if self.is_barking == True:

            self.is_barking = False
            print(f"{self.dog_name} has stopped barking. Peace at last.")

        else: # Entered stop barking even if they aren't actually barking 
            
            print(f"{self.dog_name} isn't actually barking. Perhaps you're hearing things?")

    # FUNCTION FOR EATING
    def eat(self):

        if self.is_eating == False:

            self.is_eating = True
            print(f'{self.dog_name} is now eating! Nom nom...')
    
        else: 
            print(f'{self.dog_name} is already eating.')

    # FUNCTION FOR STOP EATING
    def stop_eating(self):

        if self.is_eating == True:

            self.is_eating = False
            print(f'{self.dog_name} has stopped eating. Is the doggy full though?')
        else: # Entered stop playing even if they aren't actually playing
            print(f"{self.dog_name} isn't actually eating. Perhaps you're the hungry one?")

    # FUNCTION FOR PLAYING
    def play(self):

        if self.is_playing == False:

            print(f'{self.dog_name} is now playing with a toy. Yay!')
            self.is_playing = True

        else:

            print(f'{self.dog_name} is already playing.')
    
    # FUNCTION FOR STOP PLAYING
    def stop_playing(self):
        
        if self.is_playing == True:

            self.is_playing = False
            print(f'{self.dog_name} has stopped playing. Is the doggy satisfied though?')

        else: # Entered stop playing even if they aren't actually playing
            print(f"{self.dog_name} isn't actually playing. Perhaps your mind is playing tricks?")

    # DOG NAMES, FOR "VIEW DOGS"
    def __str__(self):
        return f'{self.dog_name} the {self.color} {self.breed}'


# DOG OBJECTS
Toto: Dog = Dog('Toto', 'Poodle', 'Brown')
Solaire: Dog = Dog('Solaire', 'Chinese Crested', 'Black')
Pogs: Dog = Dog('Pogs', "Chinese Crested", 'Grey' )

# DISPLAY MAIN MENU
def main_menu():

    
    print("\n-----------------------------------")
    print("||\t      ACTIONS            ||")
    print("-----------------------------------")
    print("\t  [1] View Dogs ")
    print("\t  [2] Play ")
    print("\t  [3] Eat ")
    print("\t  [4] Bark ")
    print("\t  [5] Exit ")
    print("-----------------------------------")

# GET MAIN MENU USER INPUT
def get_mm_input():

    while True:

        try:

            action = int(input("\nWhat action do you want to do?: "))

            if action > 5 or action < 1:
                raise ValueError
            else:
                break

        except ValueError:
            print("Invalid input. That's probably not in the choices, is it?")

    return action


# TITLE BLOCK
def display_title_block():

    title_block = """
                                                                                                                                                    
    ,-.----.                                                       ,-.----.                                                                           
    \    /  \                                                      \    /  \    ,--,                                                             ,-.  
    |   :    \               ,-.----.  ,-.----.                    |   :    \ ,--.'|                         ,-.----.                        ,--/ /|  
    |   |  .\ :         ,--, \    /  \ \    /  \                   |   |  .\ :|  | :                         \    /  \              __  ,-.,--. :/ |  
    .   :  |: |       ,'_ /| |   :    ||   :    |                  .   :  |: |:  : '                         |   :    |           ,' ,'/ /|:  : ' /   
    |   |   \ :  .--. |  | : |   | .\ :|   | .\ :     .--,         |   |   \ :|  ' |     ,--.--.        .--, |   | .\ :  ,--.--.  '  | |' ||  '  /    
    |   : .   /,'_ /| :  . | .   : |: |.   : |: |   /_ ./|         |   : .   /'  | |    /       \     /_ ./| .   : |: | /       \ |  |   ,''  |  :    
    ;   | |`-' |  ' | |  . . |   |  \ :|   |  \ :, ' , ' :         ;   | |`-' |  | :   .--.  .-. | , ' , ' : |   |  \ :.--.  .-. |'  :  /  |  |   \   
    |   | ;    |  | ' |  | | |   : .  ||   : .  /___/ \: |         |   | ;    '  : |__  \__\/: . ./___/ \: | |   : .  | \__\/: . .|  | '   '  : |. \  
    :   ' |    :  | : ;  ; | :     |`-':     |`-'.  \  ' |         :   ' |    |  | '.'| ," .--.; | .  \  ' | :     |`-' ," .--.; |;  : |   |  | ' \ \ 
    :   : :    '  :  `--'   \:   : :   :   : :    \  ;   :         :   : :    ;  :    ;/  /  ,.  |  \  ;   : :   : :   /  /  ,.  ||  , ;   '  : |--'  
    |   | :    :  ,      .-./|   | :   |   | :     \  \  ;         |   | :    |  ,   /;  :   .'   \  \  \  ; |   | :  ;  :   .'   \---'    ;  |,'     
    `---'.|     `--`----'    `---'.|   `---'.|      :  \  \        `---'.|     ---`-' |  ,     .-./   :  \  \`---'.|  |  ,     .-./        '--'       
    `---`                    `---`     `---`       \  ' ;          `---`             `--`---'        \  ' ;  `---`   `--`---'                       
                                                    `--`                                              `--`                                          
    """
    
    for item in title_block:
        print(item, end ='', flush=True)
        time.sleep(0.000001)

# EXIT MESSAGE
def display_exit_msg():

    exit_message1 = "Thank you for playing!" 
    exit_message2 = "The doggies are now going to bed."

    print("\n-----------------------------------")

    for letter in exit_message2:

        print(letter, end='', flush=True)
        time.sleep(0.05)
    
    print("\n")

    for letter in exit_message1:

        print(letter, end='', flush=True)
        time.sleep(0.05)
    
    print("\n-----------------------------------\n")

# APP START
display_title_block()

while True:

    main_menu()
    main_menu_choice = get_mm_input()

    if main_menu_choice == 1:
        
        print("\n-----------------------------------")
        print(Toto)
        print(Solaire)
        print(Pogs)
        print("-----------------------------------\n")
        time.sleep(2)

    elif main_menu_choice == 2:
        
        print("\n-----------------------------------")
        print("[1] Start Playing")
        print("[2] Stop Playing")
        print("[3] Exit ")
        print("-----------------------------------\n")
        

        while True:

            try:
                play_choice = int(input("What action do you want to do?: " )) 

                if play_choice > 3 or play_choice < 1:
                    raise ValueError
                else:
                    break

            except ValueError:
                print("Invalid input. That's probably not in the choices, is it?")

        if play_choice == 1:

            print("\n-----------------------------------")
            Toto.play()
            Solaire.play()
            Pogs.play()
            print("-----------------------------------")
            time.sleep(1.5)

        elif play_choice == 2:

            print("\n-----------------------------------")
            Toto.stop_playing()
            Solaire.stop_playing()
            Pogs.stop_playing()
            print("-----------------------------------")
            time.sleep(1.5)

        else: # play_choice == 3:
            continue


    elif main_menu_choice == 3:

        print("\n-----------------------------------")
        print("[1] Start Eating")
        print("[2] Stop Eating")
        print("[3] Exit ")
        print("-----------------------------------\n")
        

        while True:

            try:
                eat_choice = int(input("What action do you want to do?: " )) 

                if eat_choice > 3 or eat_choice < 1:
                    raise ValueError
                else:
                    break

            except ValueError:
                print("Invalid input. That's probably not in the choices, is it?")

        if eat_choice == 1:

            print("\n-----------------------------------")
            Toto.eat()
            Solaire.eat()
            Pogs.eat()
            print("-----------------------------------")
            time.sleep(1.5)

        elif eat_choice == 2:

            print("\n-----------------------------------")
            Toto.stop_eating()
            Solaire.stop_eating()
            Pogs.stop_eating()
            print("-----------------------------------")
            time.sleep(1.5)

        else: # eat_choice == 3:
            continue


    elif main_menu_choice == 4: # Barking

        print("\n-----------------------------------")
        print("[1] Start Barking")
        print("[2] Stop Barking")
        print("[3] Exit ")
        print("-----------------------------------\n")
        

        while True:

            try:
                bark_choice = int(input("What action do you want to do?: " )) 

                if bark_choice > 3 or bark_choice < 1:
                    raise ValueError
                else:
                    break

            except ValueError:
                print("Invalid input. That's probably not in the choices, is it?")

        if bark_choice == 1:

            print("\n-----------------------------------")
            Toto.bark()
            Solaire.bark()
            Pogs.bark()
            print("-----------------------------------")
            time.sleep(1.5)

        elif bark_choice == 2:

            print("\n-----------------------------------")
            Toto.stop_barking()
            Solaire.stop_barking()
            Pogs.stop_barking()
            print("-----------------------------------")
            time.sleep(1.5)

        else: # eat_choice == 3:
            continue

    else: # main_menu_choice == 5
        break

display_exit_msg()



