# Practical 6: Weather based recommendations

weather = input("Enter weather (sunny/rainy/cloudy/snowy/windy): ").strip().lower()

if weather == "sunny":
    print("Recommendation: Wear sunglasses, apply sunscreen and carry water.")
elif weather == "rainy":
    print("Recommendation: Carry an umbrella or raincoat and drive carefully.")
elif weather == "cloudy":
    print("Recommendation: Carry a light jacket, it may rain later.")
elif weather == "snowy":
    print("Recommendation: Wear warm clothes, gloves and non-slip shoes.")
elif weather == "windy":
    print("Recommendation: Secure loose items and avoid cycling on open roads.")
else:
    print("Weather not recognised. Please check the forecast before going out.")
