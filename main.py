import sys 
import random 
import requests
from PyQt5 import QtWidgets

# Bir sınıf oluşturuyoruz ve QtWidgets.QWidget sınıfından kalıtım yapıyoruz 
class MainWindow(QtWidgets.QWidget):
    def __init__(self): # Sınıfın yapıcı yöntemi 
        super().__init__() # Kalıtım yapılan sınıfın yapıcı yöntemi çağırılır

        self.setWindowTitle("Film öneri sistemi") # Uygulama penceresinin başlığı 
        self.setGeometry(200, 200, 500, 400) # Uygulama penceresinin konumu ve boyutu

        self.movie_button = QtWidgets.QPushButton("Film önerisi") # Bir QPushButton nesnesi oluşturulur ve adı "Film önerisi" olarak ayarlanır
        self.movie_button.clicked.connect(self.get_movie_recommendation) # QPushButton nesnesine tıklandığında çağrılacak yöntem ayarlanır

        self.movie_info = QtWidgets.QTextBrowser() # Bir QTextBrowser nesnesi oluşturulur

        vbox = QtWidgets.QVBoxLayout() # Bir QVBoxLayout nesnesi oluşturulur

        vbox.addWidget(self.movie_button) # QPushButton nesnesi QVBoxLayout nesnesine eklenir
        vbox.addWidget(self.movie_info) # QTextBrowser nesnesi QVBoxLayout nesnesine eklenir

        self.setLayout(vbox) # Ana bileşen olarak QVBoxLayout nesnesi ayarlanır

        self.show() # Uygulama penceresi gösterilir

    # Bu fonksiyon, The Movie Database (TMDb) API'sine bir HTTP isteği yapar ve popüler filmlerden rastgele bir film önerisi alır
    def get_movie_recommendation(self):
        url = "https://api.themoviedb.org/3/discover/movie?api_key=e5968e488e034640cf2d4bc454ec1505&language=tr-TR&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres=&with_watch_monetization_types=flatrate"
        response = requests.get(url) # API'den veri alınır
        data = response.json() # Aldığımız veriler JSON formatına dönüştürülür
        results = data['results'] # Sözlükteki results anahtarına karşılık gelen liste objesini alır. Bu liste, API'den döndürülen filmlerin listesini içerir

        if len(results) > 0:
            movie = random.choice(results) # results listesinden rastgele bir film seçer
            # Burada movie değişkenin içindeki rastgele üretilen filmin adını, konusunu ve ımdb puanını alıyoruz 
            recommendation = f"Film Adı: {movie['original_title']} ({movie['release_date'][0:4]})\n" \
                             f"IMDB Puanı: {movie['vote_average']}\n"\
                             f"Filmin Konusu: {movie['overview']}\n"
            self.movie_info.setText(recommendation) # Aldığımız bilgileri ekrana yazdırıyoruz 
        else:
            self.movie_info.setText("Önerilecek film bulunamadı.")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()              
    window.show()
    sys.exit(app.exec_())