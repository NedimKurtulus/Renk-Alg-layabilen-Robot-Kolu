# OpenCV & Arduino Tabanlı Renk Ayıklama Robotu

Bu proje, bir kamera aracılığıyla nesnelerin renklerini algılayan ve algılanan renge göre 4 adet servo motoru belirli bir senaryoda hareket ettiren bir mekatronik sistemdir. Python (OpenCV) görüntü işleme katmanı ile Arduino (Gömülü Sistem) kontrol katmanının seri haberleşme üzerinden entegrasyonunu içerir.

## Çalışma Mantığı

1.  **Görüntü İşleme (Python):** Bilgisayara bağlı kamera üzerinden alınan görüntü HSV renk uzayına çevrilir. Kırmızı ve Yeşil renkler için belirlenen piksel eşikleri (1500 piksel) aşıldığında bir "durum değişikliği" algılanır.
2.  **Haberleşme:** Renk algılandığında Python, Seri Port (USB) üzerinden Arduino'ya tek karakterlik bir komut gönderir (`'G'` veya `'R'`).
3.  **Donanım Kontrolü (Arduino):** * **'G' (Yeşil) komutu gelirse:** 4 servo motor sırayla (s1 -> s2 -> s3 -> s4) 3 saniyelik aralıklarla önceden tanımlanmış açılara hareket eder.
    * **'R' (Kırmızı) komutu gelirse:** Tüm servolar anında 90 derece (nötr) konumuna gelerek durur.

## Teknik Detaylar

### Yazılım Bileşenleri
* **Python:** OpenCV kütüphanesi ile gerçek zamanlı maskeleme ve nesne takibi.
* **Arduino:** `Servo.h` kütüphanesi ile çoklu motor kontrolü ve Seri haberleşme yönetimi.

### Donanım Gereksinimleri
* Arduino Uno / Mega
* 4 Adet Servo Motor (SG90 veya benzeri)
* Harici Güç Kaynağı (Servolar için 5V)
* PC Kamerası veya USB Webcam

## Dosya Yapısı ve Kullanım

* `robot_kontrol.ino`: Arduino kartına yüklenecek olan kontrol kodudur. Servoların 1, 2, 4 ve 5 numaralı pinlere takılması beklenmektedir.
* `renk_algilama.py`: Bilgisayar tarafında çalıştırılacak Python kodudur. Çalıştırmadan önce `serial.Serial('COM7', 9600)` satırındaki port adını kendi sisteminize göre güncelleyiniz.

### Kurulum
```bash
pip install opencv-python numpy pyserial
