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
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.unit_selector = QComboBox(self)
        self.unit_selector.addItems(["°C", "°F"])
        self.temperature_label = QLabel(self)
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

    vBox = QVBoxLayout()
    vBox.addWidget(self.city_label)
    vBox.addWidget(self.city_input)
    vBox.addWidget(self.get_weather_button)
    vBox.addWidget(self.unit_selector)
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
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["cod"] == 200:
            self.display_weather(data)

    except requests.exceptions.HTTPError:
        status = response.status_code
        if status == 404:
            self.display_error("City not found.\nPlease try again.")
        elif status == 401:
            self.display_error("Invalid API key.")
        else:
            self.display_error(f"HTTP error: {status}")

    except requests.exceptions.ConnectionError:
        self.display_error("Check your internet connection.")
    except requests.exceptions.Timeout:
        self.display_error("Request timed out.")
    except requests.exceptions.RequestException as e:
        self.display_error(f"Error: {e}")
```

> This function fetches the weather, handles errors, and sends valid data to the `display_weather()` function.

---

### 5. Displaying Weather Output

```python
def display_weather(self, data):
    temperature_k = data["main"]["temp"]
    weather_description = data["w
```
