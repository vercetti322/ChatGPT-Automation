# string concatenation (aka how to our strings together)
# suppose you want to create a string that says "subscribe to ________"
# youtuber = "Jatin Jindal" # some string variable
# ways to do this
# print("Subscribe to "+ youtuber) 
# print("Susbscribe to {}".format(youtuber))
# print(f"Susbscribe to {youtuber}")

adj = input("Adjective : ")
verb1 = input("Verb : ")
verb2 = input("Verb : ")
famous_person = input("Famous person : ")

madlib = f"Computer programming is so {adj}! It makes me excited all the time \
because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
