import pandas as pd

def bissecao(f, a, b, erro):    
    tolerancia = 10**(-erro)
    xn = a
    xn_menos_1 = b
    adicionar_valores = []
    e = float('inf') # infinito apenas para iniciar o loop
    n = 0

    if f(a)*f(b) < 0:
        while(e > tolerancia):
            xn = (a+b)/2
            e = abs(xn - xn_menos_1)
            f_xn = f(xn)
           
            if n == 0:
                adicionar_valores.append([n, a, b, xn, f_xn, float('inf')])
            else:
                adicionar_valores.append([n, a, b, xn, f_xn, e])

            if f_xn == 0:
                print("A raiz é: ", xn)
                break
            else:
                if f(a)*f_xn < 0:
                    b = xn
                else:
                    a = xn
            n += 1
            xn_menos_1 = xn 
        print("A raiz aproximada é: ", xn)
        return adicionar_valores
    else:
        print("Não existe raiz no intervalo dado")


funcao_escrita = input("Digite a função: ")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
erro = float(input("Digite o n da tolerância assim E<10^-n : "))
f = lambda x: eval(funcao_escrita)

print("\n\n******** ******** ******* ******* ******* ******* ***** \n")
iteracao = bissecao(f,a,b,erro)
print("\n******** ******** ******* ******* ******* ******* ***** \n\n\n")

def criando_tabela(iteracao):
    print(" + + + + Tabela de iterações + + + + \n")
    nome_cols = [ 'n','a', 'b', 'xn', 'f(xn)', 'E']
    tabela = pd.DataFrame(iteracao, columns=nome_cols)
    tabela_final = tabela.set_index('n')
    print(tabela)

if iteracao != None:
    criando_tabela(iteracao)