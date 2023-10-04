# Weather-Speaks
# Weather Information 

This is a simple Python script that allows you to retrieve and hear weather information for a specific city using the WeatherAPI. The script prompts you to enter a city, and then you can choose to get information about temperature, humidity, wind speed, or cloud cover for that city.

## Prerequisites

Before you can run this script, you need to have the following installed on your system:

- Python 3.x
- The `requests` library for making HTTP requests. You can install it using `pip`:
  ```bash
  pip install requests
  ```
- The `win32com.client` library for text-to-speech functionality. This library is available on Windows systems by default.

## How to Use

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory where you have saved the script.

4. Run the script using the following command:
   ```bash
   main.py
   ```

5. Follow the prompts:
   - Enter the city for which you want to check the weather.
   - Choose the desired weather information by entering a number from 1 to 4:
     1. Temperature
     2. Humidity
     3. Wind Speed
     4. Cloud Cover

6. The script will then make a request to the WeatherAPI and provide you with the requested weather information through text-to-speech.

7. The weather information will be spoken aloud to you using your system's text-to-speech capabilities.

## Example

Here's an example of how to use the script:

```
Enter city: New York
What do you want to know about today's weather?
1. Temperature
2. Humidity
3. Wind
4. Clouds

Enter your choice: 1
The current temperature in New York is 20 degrees!
```

## Notes

- Make sure you have an active internet connection, as the script relies on making an API request to retrieve weather data.

- The WeatherAPI key used in this script is a placeholder. You should replace it with your own API key from [WeatherAPI](https://www.weatherapi.com/) for long-term usage.

- You can customize the text-to-speech output or add more features to this script according to your preferences.
