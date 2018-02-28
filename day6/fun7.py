# funkcja zwraca odwócony string

def odwroc_str(zdanie):
    return zdanie[::-1]

odwrocony = odwroc_str("Ala ma kota")
print(odwrocony)

print(odwroc_str("Stół z powyłamywanymi nogami"))

def odwroc_input():
    zdanie = input("Podaj zdanie: ")
    return zdanie[::-1]

print(odwroc_input())
print(odwroc_input())

