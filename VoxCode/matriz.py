from PIL import Image

def texto_para_binario(texto):
    return ''.join(format(ord(c), '08b') for c in texto)

texto = "Olá,Mundo!"

# Conversão do texto em binário
binario = texto_para_binario(texto)
print("Texto em binário:", binario)

# Inicializa as matrizes RGB
tamanho_original = 8
r = [[None] * tamanho_original for _ in range(tamanho_original)]
g = [[None] * tamanho_original for _ in range(tamanho_original)]
b = [[None] * tamanho_original for _ in range(tamanho_original)]

x = 0
y = 0

# Preenchendo as matrizes RGB com valores baseados no binário
for b_val in binario:
    if b_val == '0':
        valor = 0
    elif b_val == '1':
        valor = 255

    if x % 3 == 0:
        r[y][x //3] = valor
    elif x % 3 == 1:
        g[y][x //3] = valor
    elif x % 3 == 2:
        b[y][x //3] = valor

    x += 1
    if  x//3 >= tamanho_original:
        x = 0
        y += 1
        if y >= tamanho_original:
            break


# Crie uma nova imagem RGB
bloco_tamanho = 8*2
image = Image.new("RGB", (tamanho_original * bloco_tamanho, tamanho_original * bloco_tamanho), color="gray")
print(image.size)
# Preencha a imagem com os blocos de cores
for i in range(tamanho_original):
    for j in range(tamanho_original):
        r_val = r[i][j] if r[i][j] is not None else 128
        g_val = g[i][j] if g[i][j] is not None else 128
        b_val = b[i][j] if b[i][j] is not None else 128
        cor = (r_val, g_val, b_val)
        for x in range(j * bloco_tamanho, (j + 1) * bloco_tamanho):
                    for y in range(i * bloco_tamanho, (i + 1) * bloco_tamanho):
                    	image.putpixel((x, y), cor)

# Salve a imagem
image.save("output_image.png")

# Exiba a imagem (opcional)
image.show()