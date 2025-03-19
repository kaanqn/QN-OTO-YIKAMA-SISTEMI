import time

print("      --QN OTO YIKAMA SİSTEMLERİ--")
print("Kartınızı takıp ardından bakiye yükleyiniz...")

total = 0
aktif_hizmetler = {}

def hizmet_suresi(hizmet):
    for i in range(40, 0, -1):
        print(f"Kalan süre: {i} saniye\n", end="\r")
        time.sleep(1)
    del aktif_hizmetler[hizmet]
    print(f"\nSüre doldu: {hizmet} hizmetiniz sona erdi! Yeniden satın almanız gerekmektedir.")

while True:  
    print("\n--> Bakiye yüklemek için                   '1' numarasına basınız.")
    print("--> Yıkama ücreti listesi için             '2' numarasına basınız.")
    print("--> İşlem iptali için                      '3' numarasına basınız.")
    print("--> Bakiyenizi öğrenmek için               '4' numarasına basınız.")
    print("--> Sipariş oluşturmak için                '5' numarasına basınız.")
    print("--> Sahip olduğunuz hizmetleri görmek için '6' numarasına basınız.")
    print("--> Hizmet kullanmak için                  '7' numarasına basınız.\n")
    
    kart_giris = int(input("Tuşlama: "))

    if kart_giris == 1:
        bakiye = int(input("Yüklenecek bakiyeyi tuşlayınız: "))
        total += bakiye
        print("Güncel bakiyeniz:", total, "₺\n")

    elif kart_giris == 2:
        print("Su: 50₺\nKöpük: 40₺\nSüpürge: 30₺\nHava: 30₺\n")

    elif kart_giris == 3:
        print("Çıkış yapıldı!\n")
        break

    elif kart_giris == 4:
        print("Kart bakiyesi:", total, "₺\n")

    elif kart_giris == 5:
        print("1) Su: 50₺\n2) Köpük: 40₺\n3) Süpürge: 30₺\n4) Hava: 30₺")
        print("5) Su + Köpük: 80₺\n6) Su + Köpük + Süpürge: 100₺\n7) Ana menü\n")

        secim = int(input("Seçim yapınız: "))
        
        fiyatlar = {1: ("Su", 50), 2: ("Köpük", 40), 3: ("Süpürge", 30), 4: ("Hava", 30),
                    5: ("Su + Köpük", 80), 6: ("Su + Köpük + Süpürge", 100)}

        if secim in fiyatlar:
            hizmet, fiyat = fiyatlar[secim]
            if total >= fiyat:
                total -= fiyat
                aktif_hizmetler[hizmet] = time.time()
                print(f"{hizmet} hizmetiniz satın alındı! Kalan bakiye: {total} ₺\n")
            else:
                print("Yetersiz bakiye!\n")
        elif secim == 7:
            print("Ana menüye dönülüyor...\n")
        else:
            print("Hatalı tuşlama! Lütfen tekrar deneyiniz.\n")
    
    elif kart_giris == 6:
        if aktif_hizmetler:
            print("Aktif hizmetleriniz:")
            for hizmet, zaman in aktif_hizmetler.items():
                print(f"- {hizmet}")
        else:
            print("Şu anda aktif bir hizmetiniz bulunmamaktadır.\n")
    
    elif kart_giris == 7:
        if not aktif_hizmetler:
            print("Kullanılabilir hizmetiniz bulunmamaktadır3! Önce bir hizmet satın alın.\n")
        else:
            print("Kullanılabilir hizmetleriniz:")
            for idx, hizmet in enumerate(aktif_hizmetler.keys(), start=1):
                print(f"{idx}) {hizmet}")
            secim = int(input("Başlatmak istediğiniz hizmeti seçiniz: "))
            
            hizmet_listesi = list(aktif_hizmetler.keys())
            if 1 <= secim <= len(hizmet_listesi):
                hizmet_suresi(hizmet_listesi[secim - 1])
            else:
                print("Hatalı seçim! Lütfen geçerli bir hizmet numarası giriniz.\n")
    else:
        print("Hatalı tuşlama! Lütfen tekrar deneyiniz.\n")

