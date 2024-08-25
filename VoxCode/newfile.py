import numpy as np

# Criar uma matriz 10x10 de tuplas (inicialmente vazias)
def texto_para_binario(texto):
    return ' '.join(format(ord(c), '08b') for c in texto)
    
array_2d = np.empty((21, 21,3), dtype=object)

x, y = 0, 0
for array in range(array_2d.shape[0] * array_2d.shape[1]):
	array_2d[x, y] = (0, 256, 0)  # Definindo a cor verde em RGB
	
	x +=1
	if x==array_2d.shape[1]:
		x=0
		y+=1
print(texto_para_binario('ola'))
print(array_2d)