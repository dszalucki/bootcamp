from random import shuffle
from random import choice

pytania = [
    # Pytania są w formacie: (pytanie, lista_odpowiedzi), przy czym poprawna odpowiedź
    # zawsze znajduje się na pierwszym miejscu.
    ('Który spośród wymienionych języków programowania jest najstarszy?',
     ['Python', 'F#', 'Ruby', 'LFE', 'Clojure']),
    ('Twórcą Pythona jest…',
     ['Guido van Rossum', 'Larry Wall', 'John Hughes', 'Joe Armstrong', 'Ken Thompson', 'Rich Hickey']),
    ('Implementacja Pythona o nazwie PyPy jest napisana w języku…',
     ['RPython', 'Cython', 'C', 'Common Lisp']),
    ('Klasy danych (PEP 557) to nowość przypisana do Pythona w wersji…',
     ['3.7', '2.7', '3.6', '1.0']),
    ('Z którą gałęzią sztuki powiązana jest nazwa szkieletu sieciowego Django?',
     ['muzyka', 'film', 'literatura']),
    ('Która z wymienionych nazw odpowiada dialektowi Lispu napisanemu w Pythonie?',
     ['Hy', 'MyPy', 'PyPI', 'Pylint', 'elisp']),
    ('Dopełnienia listowe pojawiły się w Pythonie w wersji…',
     ['2.0', '3.0', '3.6', '1.6']),
]
uczestnicy = []

while True:
    imie = input('Podaj imię gracza lub „STOP”: ')
    if imie == "STOP":
        break
    uczestnicy.append(imie)

print("W grze znajdują się:")

for i in uczestnicy:
        print(i)

print(f'na pytanie odpowie {choice(uczestnicy)}')

while True:
    for i in pytania:

        pytanie = pytania[0]
        true_pytanie = pytanie[0]
        print(pytanie)
    print(input("Prosimy o podanie numeru odpowiedzi: "))