from generar import *
def main():
    lista=[]
    lista.append('00.000.000-0')
    lista.append('11.111.111-1')
    lista.append('22.222.222-2')
    lista.append('33.333.333-3')
    lista.append('44.444.444-4')
    lista.append('55.555.555-5')
    lista.append('66.666.666-6')
    lista.append('77.777.777-7')
    lista.append('99.999.999-9')

    for i in lista:
        miPdf=GenerarPdf(i)
        miPdf.__generar__()


if __name__ == "__main__":
    main()
