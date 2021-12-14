import re

while True:
    

    # La password deve essere lunga almeno 8 caratteri
    password = input("Dammi la password da testare: ")              
    

    # La password deve contenere almeno un carattere maiuscolo
    
    if len(password) < 8: 
       print("La password deve essere lunga almeno 8 caratteri") 
       continue
  

    if not re.search("[A-Z]+",password):
         print("La password deve contenere almeno un carattere maiuscolo")
         continue

     
    # La password deve contenere almeno un carattere minuscolo
    
    if not re.search("[a-z]+",password):
         print("La password deve contenere almeno un carattere minuscolo")
         continue

    # La password deve contenere almeno un numero
    if not re.search("[0-9]+",password):
        print("La password deve contenere almeno un numero")
        continue
    

    # La password deve contenere almeno un carattere speciale: .,_-
    
    if not re.search("[\.,_-]+",password):
        print("La password deve contenere almeno un carattere speciale: .,_-")
    

print("Chiudo il programma.")