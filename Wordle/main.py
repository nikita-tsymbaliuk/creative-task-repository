import random

def processGuess(key, trial):
  position = 0
  subject = ""
  for letter in trial:
    if letter == key[position]:
      subject += "+"
    elif letter in key:
      subject += ":"
    else:
      subject += "-"
    position += 1
  print(subject)
  return subject == "+++++" #True of correct, False otherwise

#loading words and storing them at list
word_list = []
word_file = open("words.txt")
for word in word_file:
  word_list.append(word.strip())

#picking a word
answer = random.choice(word_list)

print(answer)
number_of_attempts = 5
guessed_correctly = False

while number_of_attempts > 0 and not guessed_correctly:
  #getting guess from the participant
  guess = input("Input a 5-letter word and press enter: ")
  print("You have", number_of_attempts, "attempts left and you have guessed", guess)
  number_of_attempts -= 1

  #process guess
  guessed_correctly = processGuess(answer, guess)

if guessed_correctly:
  print("Bingo, you have guessed the correct word -", answer, "in", number_of_attempts, "attempts!")
else:
  print("Sorry, you have used your guesses...the correct word is -", answer)