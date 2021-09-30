def word_count():
   sentence = input("Enter String: ")
   word = sentence.split()
   counts = dict()
   
   for i in word:
      if i in counts:
         counts[i] += 1
      else:
         counts[i] = 1
   print(counts)
word_count()
