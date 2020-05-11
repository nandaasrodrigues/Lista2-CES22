
class Departamento:
    def __init__(self):
        self.vendas_mes = 0;
    
    def vendas(self, venda):
        self.vendas_mes += venda

    def get_vendas_mes(self):
        return self.vendas_mes
        
    def get_receita(self, fechamento = False):
        if(fechamento):
            receita = self.vendas_mes
            self.vendas_mes = 0
            return receita
        else:
            return self.vendas_mes

class Funcionario:
    def __init__(self, nome, rg, salario_base, departamento):
        self.nome = nome
        self.rg = rg
        self.salario_base = salario_base
        self.departamento = departamento


class Vendedor(Funcionario):

    def __init__(self, nome, rg, salario_base, departamento):
        super().__init__(nome, rg, salario_base, departamento)
        self.vendas_mes = 0

    def vendas(self, venda):
        self.vendas_mes += venda
        self.departamento.vendas(venda)

    def get_vendas_mes(self):
        return self.vendas_mes

    def get_salario(self, fechamento = 'False'):
        salario = self.salario_base + self.vendas_mes*.1
        if(fechamento):
            self.vendas_mes = 0
        return salario

class Gestor(Funcionario):
    def __init__(self, nome, rg, salario_base, senha, departamento):
        super().__init__(nome, rg, salario_base,departamento)
        self.senha = senha
    
    def get_salario(self):
        return self.salario_base + .1*self.departamento.get_receita()
    

laticinios = Departamento()
func1 = Vendedor('joao', 123, 1000, laticinios)
gestor = Gestor('ricardo', 165, 10000, 5894, laticinios)

func1.vendas(1000)
func1.vendas(521)
func1.vendas(895)
print(laticinios.get_receita())
print(func1.get_salario())
print(gestor.get_salario())

