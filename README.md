# Film Öneri Sistemi

Bu proje, Python dilinde geliştirilen bir film öneri sistemi uygulamasıdır. The Movie Database (TMDb) API'si kullanılarak popüler filmlerden rastgele bir film önerisi sunmaktadır.

## Özellikler

- Basit ve kullanıcı dostu bir grafik arayüzü sağlar.
- TMDb API'sini kullanarak popüler filmlerden birini rastgele seçer.
- Film hakkında bilgileri (film adı, çıkış tarihi, IMDB puanı ve konusu) gösterir.

## Gereksinimler

- Python 3.x
- PyQt5 kütüphanesi
- requests kütüphanesi

## Kurulum

1. Bu projeyi bilgisayarınıza klonlayın veya indirin.
git clone https://github.com/seyitbyrm/film-oneri-botu.git

2. Proje klasörüne girin.
cd film-oneri-botu

3. Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın.
pip install PyQt5

4. `main.py` dosyasını çalıştırarak uygulamayı başlatın.
python main.py

## Kullanım

1. Uygulama başladığında, "Film Önerisi" butonunu görürsünüz.
2. "Film Önerisi" butonuna tıklayın.
3. Uygulama, TMDb API'sine bir istek göndererek popüler filmlerden birini seçer.
4. Seçilen film hakkındaki bilgiler (film adı, çıkış tarihi, IMDB puanı ve konusu) ekranda görüntülenir.
