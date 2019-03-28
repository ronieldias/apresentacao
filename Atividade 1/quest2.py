"""
	2. Crie um programa em que permita baixar, via HTTP e usando o método GET, 
	um arquivo de imagem (escolha um tipo apenas - jpg ou gif...): 
		• Passe como parâmetro o "endereço WEB" completo até o arquivo; 
		• Salve o corpo da resposta como um arquivo atentando para o tipo.
"""
from requests import *

def main():
    imagem = get("https://www.altoastral.com.br/wp-content/uploads/2016/10/ilusao-otica-beau-deeley-3d-vortex-750x500.jpg").content
    open('imagem.jpg', 'wb').write(imagem)

if __name__ == '__main__':
    main()