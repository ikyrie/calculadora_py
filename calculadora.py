class Calculadora:
    def __init__(self, a, operacao, b):
        self.a = a
        self.operacao = operacao
        self.b = b

    
    @staticmethod
    def soma(a, b):
        return a + b

    @staticmethod
    def subtracao(a, b):
        return a - b

    @staticmethod
    def divisao(a, b):
        return a / b

    @staticmethod
    def multiplicacao(a, b):
        return a * b

    @staticmethod
    def imprimeResultado(resultado):
        print(resultado)

    def calcula(self):
        match self.operacao:
            case "+":
                self.imprimeResultado(self.soma(self.a, self.b))

            case "-":
                self.imprimeResultado(self.subtracao(self.a, self.b))
            
            case "/":
                self.imprimeResultado(self.divisao(self.a, self.b))

            case "*":
                self.imprimeResultado(self.multiplicacao(self.a, self.b))

def recebeValor():
    """
    Essa função pega o input do usuário e valida se o valor recebido é um inteiro.
    """
    try:
        return int(input('Digite um valor: '))
    except:
        print('Valor inválido! Tente novamente')
        return recebeValor()

def recebeOperacao():
    """
    Essa função pega o input do usuário e valida se a operação recebida é uma string e pertence ao conjunto de operações válidas
    """
    operacoesValidas = ['+', '-', '/', '*']

    try:
        inputDoUsuario =  input('Digite a operação desejada: (+)  (-)  (/)  (*) -> ')
        assert inputDoUsuario in operacoesValidas
        return inputDoUsuario
    except:
        print('Operação inválida! Tente novamente')
        return recebeOperacao()

def main():
    a = recebeValor()
    op = recebeOperacao()
    b = recebeValor()

    minhaCalculadora = Calculadora(a, op, b)
    minhaCalculadora.calcula()

if __name__ == '__main__':
    main()
