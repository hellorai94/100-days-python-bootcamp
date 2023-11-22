programming_dictionary = {
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
}

print(programming_dictionary["Loop"])

# Add new items to dictionary
programming_dictionary["Try"] = "Making my try to add a item in the dictionary"

print(programming_dictionary["Try"])

# Create a empty dictonary
empty_dictionary = {}

# Edit an item in a dictonary
programming_dictionary["Try"] = "Agora em português: Fazendo a minha tentativa de adicionar um item ao dicionário"
print(programming_dictionary["Try"])

# Loop through a dictionary
for key in programming_dictionary:
    print(programming_dictionary[key])

# Nesting Dictionary in a Dictionary 

travel_log = {
    "Brazil": {"cities_visited": ["Cachoeira","Salvador", "Rio de Janeiro"], "total_visits": "I live here"}, 
    "France": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
    }

print(travel_log)
  


