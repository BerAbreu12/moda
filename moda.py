
# INICIALIZANDO VARIÁVEIS
controle = 0
k = 0
phi = 0
varphi = 1 
p = 0

!pip install numpy scipy
# pip show numpy 
!pip install numpy
import numpy as np

# Definição da função f(y)
def f(y):
    return ( (np.log(p) * np.log( (1 - phi) / phi) ) / ( np.log(phi) * np.log(varphi) ) ) * \
        ( ( 1 + ( ( (k * varphi) / (1 - k) ) * ( (1 - y) / y ) ) ** ( np.log( (1 - phi) / phi ) / np.log(varphi) ) ) ** (- ( np.log(p) + np.log(phi) ) / np.log(phi) ) ) * \
        ( ( ( (k * varphi) / (1 - k) ) * ( (1 - y) / y ) ) ** ( np.log( (1 - phi) / phi ) / np.log(varphi) ) ) * ( 1 / ( y * (1 - y) ) )

#LAÇO PARA FICAR REPETINDO O CÁLCULO
while controle == 0:

    # ===================================================================================================
    print("\n DEFINA OS COEFICIENTES \n")   # Coeficientes m = 0.1 b = 2

    aux = 0 #-------------------------------------------------------------------------
    while aux == 0:
        k = float(input("DIGITE UM VALOR PARA k: "))                # k = 0.3

        if 0 < k < 1:
            aux = 1
        else:
            print("\n ==> VALOR FORA DO INTERVALO (0, 1) ")
            

    aux = 0 #-------------------------------------------------------------------------
    while aux == 0:
        phi = float(input("DIGITE UM VALOR PARA phi : "))            # phi = 0.3
    
        if 0 <= phi <= 0.5:
            aux = 1
        else:
            print("\n ==> VALOR FORA DO INTERVALO (0, 0.5) ")

    aux = 0 #-------------------------------------------------------------------------
    while aux == 0:
        varphi = float(input("DIGITE UM VALOR PARA varphi : "))      # varphi = 1.5 

        if 1 < varphi:
            aux = 1
        else:
           print("\n ==> VALOR FORA DO INTERVALO, MAIOR QUE 1 ")
            

    aux = 0 #-------------------------------------------------------------------------
    while aux == 0:
        p = float(input("DIGITE UM VALOR PARA p: "))                # p = 0.5
    
        if 0 <= p <= 1:
            aux = 1
        else:
            print("\n ==> VALOR FORA DO INTERVALO [0, 1] ")
            

    # ===================================================================================================
    # Defina o domínio 
    xmin = 0.0000001
    xmax = 0.9999999
    
    # Crie uma grade de pontos x
    x_values = np.linspace(xmin, xmax, 1000)  # 1000 pontos entre xmin e xmax

    from scipy.optimize import minimize_scalar

    # Encontre o máximo da função -f(y)
    result = minimize_scalar(lambda x: -f(x), bounds=(xmin, xmax), method = 'bounded')

    print(result.x)

    controle = int(input("\n DESEJA CALCULAR NOVAMENTE? (0:sim ou 1:nao): "))
    
print("\n FIM DO PROGRAMA, VOLTE SEMPRE. \n")

