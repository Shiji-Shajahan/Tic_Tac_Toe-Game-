print('Scrabble score')
#Ask the user to input a word
#Calculate the score that the word has in the Scrabble game
#This is the dictionary containing the points each of the different letters give:.
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
        "x": 8, "z": 10}
for character in score:
  value=score[character]
  print(f' For the character {character} the score is {value}')
user_input=input('Please enter a word')
value_2=[]
for element in user_input.lower():
    value_1=score[element]
    print(f'For the element {element} the value is {value_1}')
    value_2.append(value_1)
print(value_2)
print('The Scrabble score is',sum(value_2))

#Method2
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
        "x": 8, "z": 10}
user_input=input('Please enter a word')
value_1=[]
for element in user_input.lower():
  print(element)
  print(score[element])
  value_1.append(score[element])
print(value_1)
print('The Scrabble score is',sum(value_1))