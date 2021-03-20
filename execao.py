def dividir42PorX(x):
    try:
       return 42/x
    except ZeroDivisionError:
        print("Mano, tu é burro? Não da pra dividir por 0 wtf")


print (dividir42PorX(2))
print (dividir42PorX(4))
print(dividir42PorX(23))
print (dividir42PorX(0))