kaynak="şçöğüıŞÇÖĞÜİ"
hedef="scoguiSCOGUI"

çeviri_tablosu=str.maketrans(kaynak,hedef)

metin=input("Bir metin girin: ")

print(metin.translate(çeviri_tablosu))