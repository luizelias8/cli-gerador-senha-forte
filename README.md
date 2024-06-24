# Gerador de senha forte

Este é um simples script em Python que gera senhas fortes com base nas opções fornecidas pelo usuário. Ele permite a inclusão de dígitos, letras maiúsculas e caracteres especiais na senha gerada.

## Funcionalidades

- **Tamanho personalizável**: Você pode especificar o comprimento da senha desejada.
- **Inclusão de dígitos**: O script permite adicionar dígitos (0-9) à senha.
- **Letras maiúsculas**: A opção de incluir letras maiúsculas está disponível.
- **Caracteres especiais**: Caracteres especiais como @, #, $, etc. podem ser incluídos para aumentar a segurança da senha.

## Requisitos

- Python 3.x

## Como Usar

Clone o repositório e navegue até o diretório do projeto:

    ```
    git clone https://github.com/luizelias8/cli-gerador-senha-forte.git
    cd cli-gerador-senha-forte
    ```

## Executando o Script

Você pode executar o script diretamente a partir do terminal com diferentes opções:

- **Tamanho da senha**: Use a opção -l ou --length para especificar o comprimento da senha. O valor padrão é 12.
- **Incluir dígitos**: Use a opção -d ou --digits para incluir dígitos na senha.
- **Incluir letras maiúsculas**: Use a opção -u ou --uppercase para incluir letras maiúsculas na senha.
- **Incluir caracteres especiais**: Use a opção -s ou --specials para incluir caracteres especiais na senha.
- **Versão**: Use a opção -v ou --version para exibir a versão do script.

## Exemplos

1. Gerar uma senha de 16 caracteres incluindo dígitos e letras maiúsculas:
    ```
    python cli_gerador_senha_forte.py -l 16 -d -u
    ```

2. Gerar uma senha padrão de 12 caracteres incluindo todos os tipos de caracteres:
    ```
    python cli_gerador_senha_forte.py -d -u -s
    ```

3. Gerar uma senha de 8 caracteres sem caracteres especiais:
    ```
    python cli_gerador_senha_forte.py -l 8 -d -u
    ```

## Detalhes do Código

O código é estruturado da seguinte forma:

- Função `gerar_senha`: Gera uma senha com base nos parâmetros fornecidos.
- Função `main`: Processa os argumentos da linha de comando e chama a função gerar_senha com os parâmetros fornecidos.

## Contribuição

Contribuições são bem-vindas!

## Autor

- [Luiz Elias](https://github.com/luizelias8)