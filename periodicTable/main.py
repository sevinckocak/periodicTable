print("""************************************
LÜTFEN İŞLEM SEÇİNİZ
1)Son basamağı okul numaramın sonuyla aynı olan elementler
2) 1.deki elementlerin tüm özellikleri
3)Atom Numarası Asal Sayı olan elementler
4)Seçimden çıkmak
************************************""")
def same_last_number():
    with open("7.txt", "r", encoding="utf-8") as file:
        bilgiler = []
        datas = file.readlines()
        for atlama in datas:
            atlama = atlama.replace("\n", "")
            atlama = atlama.split(";")
            if int(atlama[0][-1]) == 7:
                bilgiler.append(atlama[0])
                bilgiler.append(atlama[3])
    print(bilgiler)
def tum_ozellikler():
    with open("7.txt", "r", encoding="utf-8") as file2:
        bilgiler = {}
        atomNumber = []
        massNumber = []
        symbolName = []
        turkishFullName = []
        englishFullName = []
        state = []
        datas2 = file2.readlines()
        for atlama2 in datas2:
            atlama2 = atlama2.replace("\n", "")
            atlama2 = atlama2.split(";")
            if int(atlama2[0][-1]) == 7:
                atomNumber.append(atlama2[0])
                massNumber.append(atlama2[1])
                symbolName.append(atlama2[2])
                turkishFullName.append(atlama2[3])
                englishFullName.append(atlama2[4])
                state.append(atlama2[5])
                bilgiler = {'atom numarası': atomNumber, 'kütle numarası': massNumber, 'sembol adı': symbolName,
                            'türkçe adı': turkishFullName, 'ingilizce adı': englishFullName, 'O.K da durumu': state}
        print(bilgiler)


def asal_sayı_olanlar():
    with open("7.txt", "r", encoding="utf-8") as file1:
        datas1 = file1.readlines()
        for atlama1 in datas1:
            atlama1 = atlama1.replace("\n", "")
            atlama1 = atlama1.split(";")
            if (int(atlama1[0])) > 2:
                for i in range(2, int(atlama1[0])):
                    if (int(atlama1[0]) % i) == 0:
                        break
                    else:
                        print(atlama1[2])
                        break
            elif (int(atlama1[0])) == 2:
                print(atlama1[2])


while True:
    islem_secimi=int(input("Lütfen seçiminizi girin:"))
    if islem_secimi==1:
        print(same_last_number())
    elif islem_secimi==2:
        print(tum_ozellikler())
    elif islem_secimi==3:
        print(asal_sayı_olanlar())
    elif islem_secimi==4:
        print("İşlemden çıkıldı")
        break
    else:
        print("Böyle bir işlem yapılamaz")

