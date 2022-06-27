def num_primo(num):
  primo = True
  for i in range(2, num):
    if num % i == 0:
      primo = False
      break
  if primo:
    print("n° primo")
  else:
    print("n° no es primo")  
  

num_primo(5)