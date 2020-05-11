
def uso(func):
    def call_f(*args, **kwargs):
        print('A função {} foi usada'.format(func.__name__))
        func(*args, **kwargs)
    return call_f

class Operacoes:
    resultado_anterior = 0

    @uso
    def soma(self,a,b):
        resultado_anterior = a+b
        return resultado_anterior
        
    @uso
    def subtracao(self,a,b):
        resultado_anterior = a-b
        return resultado_anterior

    @uso
    def multiplicacao(self,a,b):
        resultado_anterior = a*b
        return resultado_anterior
    
    @uso
    def divisao(self, a,b):
        resultado_anterior = a/b
        return resultado_anterior
    
calculo = Operacoes()
calculo.soma(1,1)
calculo.subtracao(5,3)
calculo.multiplicacao(1,3)
calculo.divisao(4,2)