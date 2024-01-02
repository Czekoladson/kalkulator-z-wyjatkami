
def spam(podzielone_przez):         #nierozbudowana wersja
    return 42 / podzielone_przez

try:

   print(spam(2))
   print(spam(4))
   print(spam(0))
   print(spam(13))
except ZeroDivisionError:
    print("Nie można dzielić przez zero !") 


try:        #więcej przykładowych błędów
    liczba1 = int(input("Podaj pierwszą liczbę: "))
    liczba2 = int(input("Podaj drugą liczbę: "))

    wynik = liczba1 / liczba2
    print("Wynik dzielenia: ", wynik)

except ZeroDivisionError:
    print("Nie można dzielić przez zero!")
except ValueError:
    print("Wprowadzono nieprawidłową wartość!")
except Exception as e:
    print("Wystąpił błąd:", e)

    

