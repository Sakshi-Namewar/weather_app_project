# weather_app_project
# 🌤️ Weather App (Python + PyQt5)

Weather app built with Python & PyQt5. Supports °C/°F toggle, emoji-based condition, and error handling using OpenWeatherMap API.

---

## 🧠 Core Code Breakdown

### 1. Importing Modules

```python
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox
from PyQt5.QtCore import Qt
```

>  Import core modules for GUI (`PyQt5`), system control (`sys`), and API calling (`requests`).

---

### 2. Designing the GUI

```python
lass WeatherApp(QWidget):
    def _init_(self):
        super()._init_()
        self.city_label = QLabel("Enter city name:",self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel( self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()
```

> Define the GUI layout and all widgets: labels, input, button, dropdown, and display labels.

---

### 3. Arranging & Styling Widgets

```python
def initUI(self):
        self.setWindowTitle("Weather App")

        Box = QVBoxLayout()
        vBox.addWidget(self.city_label)
        vBox.addWidget(self.city_input)
        vBox.addWidget(self.get_weather_button)
        vBox.addWidget(self.temperature_label)
        vBox.addWidget(self.emoji_label)
        vBox.addWidget(self.description_label)

        self.setLayout(vBox)
```

> Used `QVBoxLayout()` to arrange widgets vertically and make the UI look clean and centered.

---

### 4. API Integration + Error Handling

```python
def get_weather(self):
    api_key = "203d6762262c1fa75b0bff627f8260bd"
    city = self.city_input.text()
    url =  f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

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
 

```

> This function fetches the weather, handles errors, and sends valid data to the `display_weather()` function.

---

### 5. Displaying Weather Output

```python
def display_weather(self,data): 
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15  # Convert from Kelvin to Celsius
        temperature_f = (temperature_k * 9/5) - 459.67  # Convert to Fahrenheit
        weather_description= data["weather"][0]["description"]

        print(data)

        self.temperature_label.setText(f"{temperature_f:.0f}°F")
        self.description_label.setText(weather_description)
        weather_id = data["weather"][0]["id"]  # Get emoji
        emoji = self.get_weather_emoji(weather_id)
        self.emoji_label.setText(emoji)
```

### 6. Weather Emoji Logic

```python
@staticmethod
    def get_weather_emoji(weather_id):
        pass

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
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return "🌈"
```
### 7. Running the App
```python
if _name_ == "_main_":
        app= QApplication(sys.argv)
        WeatherApp=WeatherApp()
        WeatherApp.show()
        sys.exit(app.exec_())
```
