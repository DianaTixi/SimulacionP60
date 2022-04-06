
import random
import matplotlib.pyplot as plt
import seaborn as sb

intentos= int (input("Ingrese el numero de veces a lanzar: ")) 
dado1 = [random.randint(0,6) for _ in range(intentos)]
print(dado1)
dado2 = [random.randint(0,6) for _ in range(intentos)]
print(dado2)

lista_result=list()
for x in range(0,intentos):
    lista_result.append(dado1[x]+dado2[x])   
print('Resultado: ',lista_result)
intervalos = range(min(lista_result), max(lista_result) + 2) 

plt.hist(x=lista_result, bins=intervalos, color='#C898DF', rwidth=0.85)
plt.xlabel('Sumatoria')
plt.ylabel('Frecuencia')
plt.xticks(intervalos)
plt.title('Histograma Sumatoria de Dados')
plt.show() 
