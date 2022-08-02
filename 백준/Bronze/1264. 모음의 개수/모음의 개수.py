sentences = []
while True:
  sentence = input().replace(' ', '')
  if sentence == '#':
    break
  sentences.append(sentence)

def get_rid_of_vowels(sentence):
  vowels = [ 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  cnt = 0
  for i in sentence:
    if i in vowels:
      cnt += 1
  print(cnt)

for sentence in sentences:
  get_rid_of_vowels(sentence)