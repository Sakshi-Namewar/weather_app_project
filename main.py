import sys
import requests
from PyQt5.QtWidgets import( QApplication, QWidget, QLabel,
                            QLineEdit,QPushButton, QVBoxLayout )
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name:",self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel( self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

 

        vBox = QVBoxLayout()
        vBox.addWidget(self.city_label)
        vBox.addWidget(self.city_input)
        vBox.addWidget(self.get_weather_button)
        vBox.addWidget(self.temperature_label)
        vBox.addWidget(self.emoji_label)
        vBox.addWidget(self.description_label)

        self.setLayout(vBox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel,QPushButton {
                font-Family: Calibri;
            }
            QLabel#city_label{
                font-Size: 40px;
                font-style: italic;
                }
            QLineEdit#city_input {
                font-Size: 40px;
                }
            QPushButton#get_weather_button {
                font-Size: 30px;
                font-weight: bold;  
                }
            QLabel#temperature_label {  
                font-Size: 75px;
                font-weight: bold;
                }
            QLabel#emoji_label { 
                font-Size: 100px;
                font-Family: Segoe UI Emoji;
                }  
            QLabel#description_label {
                font-Size: 50px; 
                }   
            """)
        self.get_weather_button.clicked.connect(self.get_weather)
               
    def get_weather(self):
        api_key= "203d6762262c1fa75b0bff627f8260bd"
        city= self.city_input.text()
        url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response= requests.get(url)
            response.raise_for_status()  # Check for HTTP errors
            data = response.json()
        
            if data["cod"]== 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError:
            status = response.status_code
            if status == 404:
                self.display_error("City not found.\n Please try again.")
            elif status == 401:
                self.display_error("Invalid API key.\n Please check your API key.")
            elif status == 500:
                self.display_error("Internal server error.\n Please try again later.")
            elif status == 503:
                self.display_error("Service unavailable.\n Please try again later.")
                
        except requests.exceptions.ConnectionError:
            self.display_error("Network error.\n Please check your internet connection.")

        except requests.exceptions.Timeout: 
            self.display_error("Timeout error.\n Please try again later.")

        except requests.exceptions.RequestException as request_error:
            self.display_error(f"An error occurred: {request_error}")  

    def display_error(self, message):
       self.temperature_label.setStyleSheet("font-size: 30px;")
       self.temperature_label.setText(message)

    def display_weather(self,data): 
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15  # Convert from Kelvin to Celsius
        temperature_f = (temperature_k * 9/5) - 459.67  # Convert to Fahrenheit
        weather_description= data["weather"][0]["description"]

        print(temperature_k)

        self.temperature_label.setText(f"{temperature_c:.0f}°C")
        self.description_label.setText(weather_description)
        weather_id = data["weather"][0]["id"]  # Get emoji
        print("Weather ID:", weather_id)  # Add this line
        emoji = self.get_weather_emoji(weather_id)
        self.emoji_label.setText(emoji) 
    

        
    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 781:
            return "🌫️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif weather_id == 801:
            return "🌤️"  # few clouds
        elif weather_id == 802:
            return "⛅"   # scattered clouds
        elif weather_id == 803:
            return "🌥️"  # broken clouds
        elif weather_id == 804:
            return "☁️"   # overcast clouds
        else:
            return "🌈"
       
if __name__ == "__main__":
        app= QApplication(sys.argv)
        WeatherApp=WeatherApp()
        WeatherApp.show()
        sys.exit(app.exec_())