import argparse
import string
import random

__version__ = '1.0.0'

def gerar_senha(tamanho, incluir_digitos, incluir_maiusculas, incluir_especiais):
    caracteres = string.ascii_lowercase
    if incluir_digitos:
        caracteres += string.digits
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_especiais:
        caracteres += string.punctuation

    senha = ''.join([random.choice(caracteres) for _ in range(tamanho)])
    return senha

def main():
    parser = argparse.ArgumentParser(description='Gerador de senha forte')

    parser.add_argument(
        '-l', '--length',
        type=int,
        default=12,
        help='Tamanho da senha (padrão: 12 caracteres)'
    )
    parser.add_argument(
        '-d', '--digits',
        action='store_true',
        help='Incluir dígitos na senha'
    )
    parser.add_argument(
        '-u', '--uppercase',
        action='store_true',
        help='Incluir letras maiúsculas na senha'
    ),
    parser.add_argument(
        '-s', '--specials',
        action='store_true',
        help='Incluir caracteres especiais na senha'
    )

    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')

    args = parser.parse_args()

    senha = gerar_senha(
        tamanho=args.length,
        incluir_digitos=args.digits,
        incluir_maiusculas=args.uppercase,
        incluir_especiais=args.specials
    )

    print(senha)

if __name__ == '__main__':
    main()