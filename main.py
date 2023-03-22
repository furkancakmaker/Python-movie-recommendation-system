import sys 
import random 
import requests
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Film öneri sistemi")
        self.setGeometry(200, 200, 500, 400)

        self.movie_button = QtWidgets.QPushButton("Film önerisi")
        self.movie_button.clicked.connect(self.get_movie_recommendation)

        self.movie_info = QtWidgets.QTextBrowser()

        vbox = QtWidgets.QVBoxLayout()

        vbox.addWidget(self.movie_button)
        vbox.addWidget(self.movie_info)

        self.setLayout(vbox)

        self.show()

    def get_movie_recommendation(self):
        url = "https://api.themoviedb.org/3/discover/movie?api_key=e5968e488e034640cf2d4bc454ec1505&language=tr-TR&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres=&with_watch_monetization_types=flatrate"
        response = requests.get(url)
        data = response.json()
        results = data['results']

        if len(results) > 0:
            movie = random.choice(results)
            recommendation = f"Film Adı: {movie['original_title']} ({movie['release_date'][0:4]})\n" \
                             f"IMDB Puanı: {movie['vote_average']}\n"\
                             f"Filmin Konusu: {movie['overview']}\n"
            self.movie_info.setText(recommendation)
        else:
            self.movie_info.setText("Önerilecek film bulunamadı.")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()              
    window.show()
    sys.exit(app.exec_())