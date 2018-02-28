class Silnik(object):
    def __init__(self, pojemnosc, moc_KM, paliwo):
        self.V = pojemnosc
        self.moc_KM = moc_KM
        self.paliwo = paliwo

def main():
    v6 = Silnik(5600, 600, "benzyna")
    print(v6.V)
    print(v6.moc_KM)
    print(v6.paliwo)
    print(type(v6))

if __name__ == '__main__':
    main()
