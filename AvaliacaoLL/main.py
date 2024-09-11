# -- coding: latin-1 --
from DequeLDLS import Deque # Arquivo DequeLDLS.py.

# Criação de um deque.
deque = Deque()

# Inserindo e exibindo elementos no início.
print("Inserindo 10 no início do deque:")
deque.addFirst(10)
print(deque) # Deve imprimir: 10.
print("Inserindo 5 no início do deque:")
deque.addFirst(5)
print(deque) # Deve imprimir: 5 10.

# Inserindo e exibindo elementos no final.
print("Inserindo 20 no final do deque:")
deque.addLast(20)
print(deque) # Deve imprimir: 5 10 20.
print("Inserindo 30 no final do deque:")
deque.addLast(30)
print(deque) # Deve imprimir: 5 10 20 30.

# Removendo e exibindo elemento do início.
print("\nRemovendo elemento do início do deque:")
deque.deleteFirst()
print(deque) # Deve imprimir: 10 20 30.
print("Removendo outro elemento do início do deque:")
deque.deleteFirst()
print(deque) # Deve imprimir: 20 30.

# Removendo e exibindo elemento do final.
print("Removendo elemento do final do deque:")
deque.deleteLast()
print(deque) # Deve imprimir: 20.
print("Removendo outro elemento do final do deque:")
deque.deleteLast()
print(deque) # Deve imprimir: None.

# Verificando se o deque está vazio e tentando remover de um deque vazio.
print("\nO deque está vazio?", deque.isEmpty()) # Deve imprimir: True.
print("Tentando remover de um deque vazio:")
deque.deleteFirst() # Deve imprimir mensagem de erro.