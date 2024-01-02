
def spam(podzielone_przez):         #nie rozbudowana wersja
    return 42 / podzielone_przez

try:

   print(spam(2))
   print(spam(4))
   print(spam(0))
   print(spam(13))
except ZeroDivisionError:
    print("Nie można dzielić przez zero !") 

    

