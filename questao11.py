#lista de argumentos 
def func_lista(*args):
    for arg in args:
        print('tipo: {0}   dado: {1}'.format(type(arg), arg))

def func_dic(**kwargs):
    for chave, valor in kwargs.items():
        print('chave: {0}   valor: {1}'.format(chave,valor))


func_lista(7, 'huh', [1,8])
func_dic(turma = 'comp', materia = 'ces22', professor = 'yano')