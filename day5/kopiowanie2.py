import copy # kopiuje wartości a nie adres w pamięci(bez import copy)

nabial = ["mleko", "jajka", "ser"]
chemia = ["domestos", "płyn do naczyń"]

zakupy_kwiecien = [nabial, chemia]
print("kwiecień: ", zakupy_kwiecien)

zakupy_maj = zakupy_kwiecien.copy()
print("maj: ", zakupy_maj)

zakupy_czerwiec = [x for x in zakupy_kwiecien]
print("czerwiec: ", zakupy_czerwiec)
zakupy_lipiec = copy.deepcopy(zakupy_kwiecien)
print()
print()
zakupy_kwiecien[1].append("gąbka")
print("kwiecień: ", zakupy_kwiecien)
print("maj: ", zakupy_maj)
print("czerwiec: ", zakupy_czerwiec)
print("lipiec: ", zakupy_lipiec)