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
    print(response.status_code)
    print(response.headers['content-type'])
    print(len(response.text), 'bytes')
    print(response.text)

if __name__ == '__main__':
    main()