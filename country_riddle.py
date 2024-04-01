import random

# Dictionary of countries with their clues
countries = {
    "France": ["The capital is Paris", "The currency is Euro", "It is famous for the Eiffel Tower", "The national flag is blue, white, and red", "It is located in Europe"],
    "Germany": ["The capital is Berlin", "The currency is Euro", "It is famous for its cars like BMW and Mercedes", "The national flag has black, red, and gold colors", "It is located in Europe"],
    "Japan": ["The capital is Tokyo", "The currency is Yen", "It is famous for sushi and cherry blossoms", "The national flag is white with a red circle in the middle", "It is located in Asia"],
    "Australia": ["The capital is Canberra", "The currency is Australian Dollar", "It is famous for its unique wildlife like kangaroos and koalas", "The national flag has stars and Union Jack", "It is located in Oceania"],
    "Brazil": ["The capital is Brasília", "The currency is Brazilian Real", "It is famous for the Amazon Rainforest and Carnival", "The national flag is green with a yellow diamond", "It is located in South America"],
    "Canada": ["The capital is Ottawa", "The currency is Canadian Dollar", "It is famous for its vast landscapes and Niagara Falls", "The national flag has red and white colors with a maple leaf", "It is located in North America"],
    "India": ["The capital is New Delhi", "The currency is Indian Rupee", "It is famous for the Taj Mahal and spicy cuisine", "The national flag has three horizontal stripes of saffron, white, and green", "It is located in Asia"],
    "South Africa": ["The capital is Pretoria", "The currency is South African Rand", "It is famous for its diverse wildlife and Nelson Mandela", "The national flag has black, red, yellow, green, white, and blue colors", "It is located in Africa"],
    "Russia": ["The capital is Moscow", "The currency is Russian Ruble", "It is famous for its vast land area and ballet", "The national flag has white, blue, and red colors", "It is located in Eurasia"],
    "Italy": ["The capital is Rome", "The currency is Euro", "It is famous for its art, architecture, and pasta", "The national flag has green, white, and red colors", "It is located in Europe"],
    "Spain": ["The capital is Madrid", "The currency is Euro", "It is famous for its flamenco dancing and bullfighting", "The national flag has red and yellow colors with a coat of arms", "It is located in Europe"],
    "China": ["The capital is Beijing", "The currency is Chinese Yuan", "It is famous for the Great Wall and pandas", "The national flag has red with five golden stars", "It is located in Asia"],
    "Mexico": ["The capital is Mexico City", "The currency is Mexican Peso", "It is famous for its ancient pyramids and spicy food", "The national flag has green, white, and red colors with an eagle", "It is located in North America"],
    "Argentina": ["The capital is Buenos Aires", "The currency is Argentine Peso", "It is famous for tango dancing and Patagonia", "The national flag has light blue and white colors with a sun", "It is located in South America"],
    "Egypt": ["The capital is Cairo", "The currency is Egyptian Pound", "It is famous for its ancient pyramids and Sphinx", "The national flag has red, white, and black colors with an eagle", "It is located in Africa"],
    "United Kingdom": ["The capital is London", "The currency is Pound Sterling", "It is famous for the Royal Family and Big Ben", "The national flag has red, white, and blue colors", "It is located in Europe"],
    "Saudi Arabia": ["The capital is Riyadh", "The currency is Saudi Riyal", "It is famous for its oil reserves and deserts", "The national flag has green with white and black colors and an Arabic inscription", "It is located in Asia"],
    "Thailand": ["The capital is Bangkok", "The currency is Thai Baht", "It is famous for its temples and beaches", "The national flag has five horizontal stripes of red, white, and blue", "It is located in Asia"],
    "South Korea": ["The capital is Seoul", "The currency is South Korean Won", "It is famous for K-pop and kimchi", "The national flag has red, white, and blue colors with a yin-yang symbol", "It is located in Asia"],
    "Greece": ["The capital is Athens", "The currency is Euro", "It is famous for its ancient history, mythology, and olives", "The national flag has blue and white colors with a cross", "It is located in Europe"],
    "New Zealand": ["The capital is Wellington", "The currency is New Zealand Dollar", "It is famous for its natural beauty and rugby", "The national flag has blue with stars and Union Jack", "It is located in Oceania"],
    "Nigeria": ["The capital is Abuja", "The currency is Nigerian Naira", "It is famous for Nollywood and diverse culture", "The national flag has green and white colors", "It is located in Africa"],
    "Norway": ["The capital is Oslo", "The currency is Norwegian Krone", "It is famous for fjords and Northern Lights", "The national flag has red, white, and blue colors with a cross", "It is located in Europe"],
    "Turkey": ["The capital is Ankara", "The currency is Turkish Lira", "It is famous for its rich history and delicious cuisine", "The national flag has red with a star and crescent", "It is located in Asia"],
    "Peru": ["The capital is Lima", "The currency is Peruvian Sol", "It is famous for Machu Picchu and llamas", "The national flag has red and white colors with a coat of arms", "It is located in South America"],
    "Sweden": ["The capital is Stockholm", "The currency is Swedish Krona", "It is famous for ABBA and IKEA", "The national flag has blue and yellow colors with a cross", "It is located in Europe"],
    "Switzerland": ["The capital is Bern", "The currency is Swiss Franc", "It is famous for chocolates, watches, and Alps", "The national flag has a red square with a white cross", "It is located in Europe"],
    "Ireland": ["The capital is Dublin", "The currency is Euro", "It is famous for St. Patrick's Day and Guinness", "The national flag has green, white, and orange colors", "It is located in Europe"],
    "Indonesia": ["The capital is Jakarta", "The currency is Indonesian Rupiah", "It is famous for Bali and diverse islands", "The national flag has red and white colors", "It is located in Asia"],
    "Iran": ["The capital is Tehran", "The currency is Iranian Rial", "It is famous for its ancient Persian history and carpets", "The national flag has green, white, and red colors with an emblem", "It is located in Asia"],
    "Vietnam": ["The capital is Hanoi", "The currency is Vietnamese Dong", "It is famous for its rich history and delicious cuisine", "The national flag has red with a yellow star", "It is located in Asia"],
    "Chile": ["The capital is Santiago", "The currency is Chilean Peso", "It is famous for its long coastline and wine", "The national flag has red, white, and blue colors with a star", "It is located in South America"],
    "Poland": ["The capital is Warsaw", "The currency is Polish Zloty", "It is famous for pierogi and Pope John Paul II", "The national flag has white and red colors", "It is located in Europe"],
    "Austria": ["The capital is Vienna", "The currency is Euro", "It is famous for classical music and the Alps", "The national flag has red and white colors", "It is located in Europe"],
    "Cuba": ["The capital is Havana", "The currency is Cuban Peso", "It is famous for cigars, vintage cars, and salsa", "The national flag has blue, white, and red colors with a star and stripes", "It is located in North America"],
    "Kenya": ["The capital is Nairobi", "The currency is Kenyan Shilling", "It is famous for its wildlife safaris and Maasai culture", "The national flag has black, red, white, and green colors", "It is located in Africa"],
    "Morocco": ["The capital is Rabat", "The currency is Moroccan Dirham", "It is famous for its vibrant markets and architecture", "The national flag has red with a green pentagram", "It is located in Africa"],
    "Portugal": ["The capital is Lisbon", "The currency is Euro", "It is famous for port wine and Fado music", "The national flag has green and red colors with a shield", "It is located in Europe"],
    "Belgium": ["The capital is Brussels", "The currency is Euro", "It is famous for chocolate, waffles, and the EU headquarters", "The national flag has black, yellow, and red colors", "It is located in Europe"],
    "Denmark": ["The capital is Copenhagen", "The currency is Danish Krone", "It is famous for its design, fairy tales, and pastries", "The national flag has red with a white Scandinavian cross", "It is located in Europe"],
    "Malaysia": ["The capital is Kuala Lumpur", "The currency is Malaysian Ringgit", "It is famous for its diverse culture, rainforests, and beaches", "The national flag has red and white stripes with a blue rectangle and star", "It is located in Asia"],
    "Ukraine": ["The capital is Kyiv", "The currency is Ukrainian Hryvnia", "It is famous for its history, landscapes, and cuisine", "The national flag has blue and yellow colors", "It is located in Europe"]
}

def play_game():
    correct_answers = 0
    total_questions = 10
    
    for _ in range(total_questions):
        country = random.choice(list(countries.keys()))
        clues = countries[country]
        
        print("Guess the country based on the following clues:")
        
        for i in range(5):
            print(clues[i])
            user_guess = input("Enter your guess: ").strip().capitalize()
            
            if user_guess == country:
                print(f"Correct! The country is {country}.")
                correct_answers += 1
                break
            else:
                if i == 4:
                    print(f"Wrong! The correct answer is {country}.")
                else:
                    print("Wrong guess. Try again!")
        
        print("-----------------------------")
    
    print(f"Quiz completed! You got {correct_answers} out of {total_questions} correct.")

# Play the game
play_game()
