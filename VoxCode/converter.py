from PIL import Image

# Abre a imagem
img = Image.open('output_image.png')
largura, altura = img.size
byts = []
tamanho_bloco = 20

# Itera sobre a imagem em blocos de 20x20 pixels
for a in range(0, altura, tamanho_bloco):  # Itera sobre a altura da imagem
    for l in range(0, largura, tamanho_bloco):  # Itera sobre a largura da imagem
        
        # Inicializa valores de cor média para o bloco
        r_total, g_total, b_total = 0, 0, 0
        
        # Contador de pixels no bloco
        contador_pixels = 0
        
        # Itera sobre os pixels no bloco 20x20
        for y in range(a, min(a + tamanho_bloco, altura)):
            for x in range(l, min(l + tamanho_bloco, largura)):
                pixel = img.getpixel((x, y))
                if pixel != (128, 128, 128):  # Considera apenas pixels que não são a cor de fundo
                    r, g, b = pixel
                    r_total += r
                    g_total += g
                    b_total += b
                    contador_pixels += 1
        
        # Calcula a média das cores no bloco
        if contador_pixels > 0:
            r_medio = r_total // contador_pixels
            g_medio = g_total // contador_pixels
            b_medio = b_total // contador_pixels
            print('r: ', r_medio)
            print('g: ', g_medio)
            print('b: ', b_medio)
            # Adiciona os bytes com base na cor média
            if r_medio != 128:
            	byts.append('1' if r_medio >= 100 else '0')
            if g_medio != 128:
            	byts.append('1' if g_medio >= 100 else '0')
            if b_medio != 128:
            	byts.append('1' if b_medio >= 100 else '0')

print('#'*20)
print(img.getpixel((largura-1, altura-1)))
print(img.getpixel((0, 0)))
#print(''.join(byts))

def binario_para_ascii(binario):
    # Adiciona padding se a string binária não for múltipla de 8
    if len(binario) % 8 != 0:
        binario = binario.zfill(len(binario) + (8 - len(binario) % 8))
    
    # Divide a string binária em blocos de 8 bits
    bytes_binarios = [binario[i:i+8] for i in range(0, len(binario), 8)]
    print("Bytes binários:", bytes_binarios)
    
    # Converte cada bloco binário para decimal e, em seguida, para o caractere ASCII correspondente
    caracteres = [chr(int(b, 2)) for b in bytes_binarios]
    
    return ''.join(caracteres)

# Exemplo
codigo_binario = ''.join(byts)
#print(codigo_binario)
print("Texto traduzido:", binario_para_ascii(codigo_binario))