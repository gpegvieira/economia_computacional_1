# Exercício 6.4
"""O que acontece quando não verificamos se a lista está vazia antes de 
chamarmos o método pop?"""

fila = []
fila.pop(0)

"""IndexError
Traceback (most recent call last)
Cell In[17], line 4
      1 # Exercício 6.4
      3 fila = []
----> 4 fila.pop(0)

IndexError: pop from empty list
"""