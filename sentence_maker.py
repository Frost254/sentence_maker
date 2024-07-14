arrayWords = []

def get_input():

  while True:
      values = input("Say something: ")
      if values == "\\end":
          break
      else:
          values = values.capitalize()
          arrayWords.append(values)
  
  print(arrayWords)

# Create the sentence
def sentence_maker():
  sentence = ""
  for word in arrayWords:
      interrogatives = ["Who", "What", "When", "Where", "Why", "How"]
      if word.startswith(tuple(interrogatives)):
          sentence += word + "? "
      else:
          sentence += word + ". "
  
  # Remove the trailing comma and space
  if sentence.endswith('. '):
      sentence = sentence[:-2]
  print(sentence)

get_input()
sentence_maker()
