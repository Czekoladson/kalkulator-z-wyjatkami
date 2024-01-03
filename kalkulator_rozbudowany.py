import sys
print("Kalkulator :)")

while True:
    print("Dodawanie(+)\n Odejmowanie(-)\n Mnożenie(*)\n Dzielenie(/)\nWyjście(exit lub e)\n")
    działanie = input("wybierz działanie: ")
    
    if działanie == "exit" or działanie =="e":
             sys.exit()
    while True:
    
        if działanie == "+" or działanie == "-" or działanie == "*" or działanie == "/":
            break
    
    if działanie not in ["+" ,"-" ,"*" ,"/"]:
        print("Podaj jedno z dostepnych opcji !")

    def działaniaa(działanie,a,b):

        if działanie == "+":
            return a + b
        if działanie == "-":
            return a - b
        if działanie == "*":
            return a * b
        if działanie == "/":
            return a / b
        
    try:

        liczba_1 = int(input("Wpisz pierwszą liczbę: "))
        liczba_2 = int(input("Wpisz drugą liczbę: "))

        if działanie == "/" and liczba_1 == 0:
            raise ZeroDivisionError
    except ValueError:
        print("Podaj liczbę !")
        continue
    except ZeroDivisionError:
        print("Nie można dzielić przez zero !")
        continue

    wynik = działaniaa(działanie,liczba_1,liczba_2)

    print("Wynik to: ",wynik)    
    print("===============")
    
        

   
        