# drukuj liczby od 1 do 100
# jeśli podzielna przez 3 drukuj Fizz
# jeśli podzielna przez 5 drukuj Buzz
# jeśli podzielna przez 3 i 5 drukuj FizzBuzz

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
        
    if i % 3 == 0:
        print("Fizz")
        continue

    if i % 5 ==0:
        print("Buzz")
        continue

    print(i)
