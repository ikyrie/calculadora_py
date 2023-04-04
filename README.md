# Projeto Calculadora em terminal com Python3

## Tecnologias utilizadas:

- Python3 🐍
- Standard Python library **unittest** for testing

## O que é

Uma calculadora feita em Python3 que tem as seguintes funcionalidades:

- Soma;
- Subtração;
- Multiplicação;
- Divisão

A calculadora roda no terminal e recebe input (entrada) do usuário para executar suas funcionalidades.

![imagem da aplicação rodando e os testes sendo executados](https://user-images.githubusercontent.com/22684176/229898988-6a46042f-59fc-4413-8018-0b9e779cdba7.gif)

Primeiro é pedido no terminal que a pessoa digite o primeiro valor. Os valores devem ser **inteiros**.

Depois a pessoa deve selecionar a operação passando uma *string* ou um texto com uma das seguintes opções: `+ - * /` respectivamente.

Por último a pessoa digita o segundo valor seguindo a mesma regra do primeiro.

Por fim, o resultado será exibido na última linha do terminal, antes do final da execução do programa.

> O resultado pode ser um *float* ou um *int*.

O programa foi testado utilizando a biblioteca padrão do próprio Python3 -> **unittest**.

As entradas do usuário também são tratadas e validadas antes da execução final da operação.

## Como rodar?

Para rodar a aplicação é necessário ter pelo menos a versão 3.10.0 do Python (versão que foi produzido o programa).

Execute o programa com o seguinte comando em seu terminal favorito:

```shell
python3 calculadora.py
```

Para rodar os testes, execute o seguinte comando:

```shell
python3 test.py -v
```

> Utilizamos o argumento `-v` para melhorar a verbosiadade dos testes em execução.

## Objetivos deste projeto

Este projeto foi montado como o intúito de aprender Python3. Algumas coisas que eu queria exercitar com este projeto:

- Classes;
- Testes;
- Métodos;
- Básico da linguagem;
- Boas práticas;
