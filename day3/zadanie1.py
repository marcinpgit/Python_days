# przyjąć input od użytkownika
dane = input("Podaj grę: ")
# sprawdzić czy string ma 9 znaków
if len(dane) == 9:
    # jeśli tak
        # sprawdzę x poziomo
    if dane.index("XXX") == 0:
            # wygrana x
        print("Wygrał X")
        # sprawdzę x pionowo
            # wygrana x
        # sprawdzę x ukośnie
             # wygrana x
    # w przeciwnym razie sprawdze 0
        # j.w.
    # w przeciwnym razie
        # remis

