print("╔" + "═" * 46 + "╗")
print("╠" + "═" * 13 + "-Faiz Hesaplayıcısı-" + "═" * 13 + "╣")
print("╠" + "═" * 3 + "BATUHAN YENIOCAK tarafından yapılmıştır." + "═" * 3 + "╣")
print("╠" + "═" * 46 + "╝")

ad = input("║ " + "Adınız giriniz                      : ")

kredi_tutari = round(float(input("║ " + "Kredi tutarınızı giriniz            : ")), 2)
yillik_faiz_orani = float(input("║ " + "Yıllık faiz oranını giriniz (yıllık): "))
print("╠" + "═" * 2 + " " + "Zaman uzunluğu")

yil_vade = int(input("║ " + "Yıl cinsinden kredi vadesi: "))
ay_vade = int(input("║ " + "Ay cinsinden kredi vadesi : "))
aylik_yenileme = int(input("║ " + "Aylık zaman periyodu      : "))
toplam_ay = yil_vade * 12 + ay_vade

def ciktilar():
    print("╠" + "═" * 46 + "╣" + "\n" + "║" + " " + ad + " için çıktılar: ")
    i=aylik_yenileme
    yil = 0
    a = 0
    b= yillik_faiz_orani
    odeme = (kredi_tutari/100) * (yillik_faiz_orani/12) * toplam_ay
    while(i <= toplam_ay):
        print("╠" + "═══" + " " + "Yıl:", (yil), "Ay:", int(i%12))
        print("╠" + "══" + " " "Aylık ödeme: " + str("\n") + "╠" + "═" + " " + str(i) + "$")
        print("╠" + "══" + " " "Toplam ödeme: " + str("\n") + "╠" + "═" + " " + str(kredi_tutari + i) + "$")
        print("╠" + "═" * 47)
        i += round(aylik_yenileme, 2)
        if (i%12==0):
            yil+=1
ciktilar()

input("╠" + " Programı kapatmak için ENTER'a tıklayınız." + "\n" + "╚" + "═" * 47)
