# Vytvorte program, ktory vypise slovo
# po pismenku, tak ze sa kazdym riadkom
# prida jedno pismenko. Slovo ma byt nacitane
# pomocou inputu.
# Priklad: Slovo "Pes" sa vypise nasledovne:
# P
# Pe
# Pes

def main():
    slovo = input('Zadaj slovo, ktore sa ma vypisat: ')
    for x in range(len(slovo)):
        print(slovo[:x+1])
main()

# Opak cvicenia z: Python-S/cvicenie/18-5-2022.py
# https://github.com/analnyroztahovac/Python-S/edit/main/cvicenie/18-5-2022.py
