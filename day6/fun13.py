# funkcja sprawdzająca czy podany string jest palindromem

# import day6.fun7
# day6.fun7.odwroc_str()


from fun7 import *

def czy_palindrom(fraza):
    """Sprawdza czy fraza jest palindromem"""
    odwrocona = odwroc_str(fraza)

    # for litera1, litera2 in zip(fraza, odwrocona):
    #     if litera1 != litera2:
    #         return False
    #
    #     return True

    for litera1, litera2 in zip(fraza, odwrocona):
        if litera1 == litera2:
            continue
        else:
            return False

    return True
print(czy_palindrom("kajak"))
print(czy_palindrom("Alamakota"))