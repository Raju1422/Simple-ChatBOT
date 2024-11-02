import requests
import logging
from dotenv import load_dotenv
import os
load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
class AiChatBot:

    def __init__(self) -> None:
        self.name = input("Please Enter your Name : ")
        print(f"Hi {self.name}, Welcome To AI CHATBOT CLI")
        log_file_name = f'chatbot_log_{self.name}.txt'
        logging.basicConfig(filename=log_file_name, level=logging.INFO, 
                            format='%(asctime)s - %(message)s')
    
    def log_conversation(self, message):
        logging.info(message)
    
    def get_weather_data(self,city):
        try:
            url=f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
            response =requests.get(url)
            data= response.json()
            return data
        except Exception as e:
            return e
        
    def greet(self):
        try :
            print("These are the service i will provide to you ")
            while True:
                print("\nOptions:")
                print("1. Ask for weather information")
                print("2. Perform a calculation")
                print("3. Exit")

                choice = input("Enter your choice (1-3): ")

                if choice == "1":
                    self.ask_weather()
                elif choice == "2":
                    self.ask_calculation()
                elif choice == "3":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice! Please select a valid option.")
        except Exception as e :
            self.log_conversation(f"Error in greet: {str(e)}")
            print(e)
            
    def ask_weather(self):
        try : 
            print("It seems you're interested in the weather. Ask me about a specific city!")
            city = input("Enter city name : ")
            data = self.get_weather_data(city)
            self.log_conversation(f"User asked for weather in {city}")
            if "error" in data:
                print( data["error"]["message"])
            else:
                location = data["location"]
                current = data["current"]
                print(f"Weather in {location['name']}, {location['region']}, {location['country']}:")
                print(f"Temperature: {current['temp_c']}°C")
                print(f"Condition: {current['condition']['text']}")
                print(f"Humidity: {current['humidity']}%")
                print(f"Wind: {current['wind_kph']} km/h")
        except Exception as e:
            self.log_conversation(f"Error in ask_weather: {str(e)}")
            print(e)

    def ask_calculation(self):
        try :
            print("I can help with math operations! Tell me what numbers and operation you'd like to perform.")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            print("\nOperations:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            operation = input("Enter your choice (1-4): ")
            result = self.calculate(operation,num1,num2)
            print(f"Result : {result}")
            self.log_conversation(f"User performed calculation:  operation number is {operation} {num1}  {num2} = {result}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return 
        except Exception as e :
            self.log_conversation(f"Error in ask_calculation: {str(e)}")
            print(e)

    def calculate(self, operation, num1, num2):
        try:
            if operation == "1":
                return num1 + num2
            elif operation == "2":
                return num1 - num2
            elif operation == "3":
                return num1 * num2
            elif operation == "4":
                if num2 == 0:
                    return "Error: Division by zero is not allowed."
                return num1 / num2
            else:
                return "Invalid operation."
        except Exception as e:
            self.log_conversation(f"Error in calculate: {str(e)}")
            return "An error occurred during calculation."


if __name__ == "__main__":
    bot = AiChatBot()
    bot.greet()