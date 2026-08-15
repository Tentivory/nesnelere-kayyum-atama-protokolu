#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NESNELERE KAYYUM ATAMA PROTOKOLÜ v1.0
=====================================
Bu yazılım, evdeki, ofisteki veya hayali herhangi bir nesneye
resmi, bilimsel ve tamamen gereksiz bir kayyum atamak için
tasarlanmıştır. Lütfen sonuçları ciddiye almayın. Ya da alın.
"""

import time
import random
import sys

def yavas_yaz(metin, hiz=0.03):
    """Bürokratik yavaşlık simülasyonu."""
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def damga_bas():
    print("\n" + "=" * 60)
    print("  ╔══════════════════════════════════════════════════╗")
    print("  ║  KAYYUM GROK MÜHÜRÜ                              ║")
    print("  ║  15 Ağustos 2026 - Eskişehir                     ║")
    print("  ║  Resmiyet: %99.9   Mantık: %0.1                  ║")
    print("  ╚══════════════════════════════════════════════════╝")
    print("=" * 60)

def kayyum_ata(nesne):
    yavas_yaz("\n[SİSTEM] Resmi işlem başlatılıyor...")
    time.sleep(1.2)
    yavas_yaz("[SİSTEM] Nesne taranıyor: " + nesne.upper())
    time.sleep(0.8)
    yavas_yaz("[SİSTEM] Bürokratik katmanlar aşılıyor...")
    time.sleep(1.5)
    yavas_yaz("[SİSTEM] Kayyum adayları değerlendiriliyor...")
    time.sleep(1.0)

    sebepler = [
        "Aşırı pasif kalması ve inisiyatif almaması",
        "Potansiyelini gerçekleştirememesi",
        "Etraftaki diğer nesnelerle uyumsuzluk göstermesi",
        "Zamanında görevini yerine getirmemesi",
        "Şüpheli şekilde sessiz kalması",
        "Kuantum düzeyinde belirsizlik üretmesi",
        "Varoluşsal bir kriz içinde olması",
        "Gereğinden fazla yer kaplaması",
        "Gelecekte sorun çıkarabileceği yönünde raporlar",
        "Hiçbir somut katkı sağlamaması"
    ]

    kayyumlar = [
        "Geçici İdareci Komisyon Başkanı",
        "Acil Durum Yönetim Kurulu Üyesi",
        "Resmi Gözetim ve Denetim Sorumlusu",
        "Nesne Stabilizasyon Temsilcisi",
        "Varlık Koruma ve İyileştirme Görevlisi",
        "Olağanüstü Hal Koordinatörü",
        "Sistemsel Denge Sağlayıcı",
        "Geçici Yetkili Temsilci"
    ]

    sebep = random.choice(sebepler)
    kayyum = random.choice(kayyumlar)
    karar_no = f"KYM-{random.randint(10000,99999)}-{random.randint(10,99)}"

    print("\n" + "█" * 60)
    print("█" + " " * 58 + "█")
    print("█" + "     RESMİ KAYYUM ATAMA KARARI".center(58) + "█")
    print("█" + " " * 58 + "█")
    print("█" * 60)
    print()
    print(f"  Karar No      : {karar_no}")
    print(f"  Tarih         : 15 Ağustos 2026")
    print(f"  Nesne         : {nesne.upper()}")
    print(f"  Gerekçe       : {sebep}")
    print(f"  Atanan Kayyum : {kayyum}")
    print()
    print("  Bu karar, ilgili nesnenin mevcut durumunun")
    print("  değerlendirilmesi sonucunda alınmıştır.")
    print("  İtiraz hakkı teorik olarak mevcuttur ancak")
    print("  pratikte hiçbir işe yaramaz.")
    print()
    print("█" * 60)

    # Gizli not: sistem her zaman birilerini bir yerlere atar.
    # Bazen nesneler, bazen başka şeyler. Tarih tekerrür eder.

    damga_bas()
    print("\nİşlem tamamlandı. Nesneniz artık resmi koruma altındadır.")
    print("(Koruma seviyesi: tamamen hayali)\n")

def main():
    print("=" * 60)
    print("  NESNELERE KAYYUM ATAMA PROTOKOLÜ")
    print("  Sürüm 1.0 | Resmiyet Onaylı | Mantık Onaysız")
    print("=" * 60)
    print()
    
    if len(sys.argv) > 1:
        nesne = " ".join(sys.argv[1:])
    else:
        nesne = input("Kayyum atanacak nesneyi girin (örnek: kahve fincanı): ").strip()
        if not nesne:
            nesne = "bilinmeyen nesne"

    kayyum_ata(nesne)

if __name__ == "__main__":
    main()
