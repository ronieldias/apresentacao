"""
	1. Crie um programa que receba uma URL e execute um método GET exibindo como saída: 
		– Status code; 
		– Cabeçalhos (response headers); 
		– Tamanho da resposta (content length); 
		– O corpo da resposta.
"""

from requests import *

def main():
    url = 'http://oglobo.globo.com/'
    response = get(url)
    info(response)


def info(response):
    print("Status code:\n", response.status_code)
    print("Cabeçalhos:\n", response.headers['content-type'])
    print("Tamanho da resposta:\n", len(response.text), 'bytes')
    print("Corpo da resposta:\n", response.text)

if __name__ == '__main__':
    main()