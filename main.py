def ordenDeSeleccion(lista):

    position=[]
    for y in range(len(lista)):
        min = lista[y]
        for x in range(len(lista)-y):
            print('\n','*'*80,'\n\niteración',x,'valor en lista',lista[x+y])
            print('se compara entre:',min,'y',lista[x+y])

            if min>=lista[x+y]:
                min=lista[x+y]
                position=int(x+y)
            print('min=', min)
        lista[y], lista[position]=lista[position],lista[y]
    return lista




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    var=ordenDeSeleccion([10,2,3,7,4,9,8,10,0])
    print(var)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
