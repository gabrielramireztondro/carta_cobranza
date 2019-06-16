from fpdf import FPDF,HTMLMixin
import plantilla_html
import csv

class MyFPDF(FPDF, HTMLMixin):
    pass

class GenerarPdf:
    def __init__(self,dna):
        self.dna=dna
        self.dict_encabezado=dict()
        self.lista_datos=[]

    def __generar__(self):

        self.read_file(self.dna)
        html=""
        html+= plantilla_html.encabezado()
        html = html.replace('p_nombre',self.dict_encabezado.get('nombre'))

        for filas in self.lista_datos:
            html+= plantilla_html.tabla()

            html = html.replace('p_tipo',filas.get('tipo_documento'))
            html = html.replace('p_numero',filas.get('numero_documento'))
            html = html.replace('p_fecha_1',filas.get('fecha_deuda'))
            html = html.replace('p_fecha_2',filas.get('fecha_vencimiento'))
            html = html.replace('p_monto',filas.get('monto'))

        html+= plantilla_html.pie()
        print('generando carta a dna {0}.....ok'.format(self.dna))
        midna=self.dna
        midna=midna.replace('.','')
        pdf=MyFPDF()
        pdf.add_page()
        pdf.write_html(html)
        pdf.output('{0}_.pdf'.format(midna),'F')

    def __exit__(self, exc_type, exc_value, traceback):
        for file in self.files:
            os.unlink(file)

    def read_file(self,dna):
        dict_encabezado=dict()
        list_datos=[]
        with open('data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = 0
            for row in csv_reader:
                if str(row[0]).strip()==dna:
                    dict_datos=dict()
                    dict_encabezado['dna']=str(row[0]).strip()
                    dict_encabezado['nombre']=str(row[1]).strip()
                    dict_datos['dna']=str(row[0]).strip()
                    dict_datos['tipo_documento']=str(row[2]).strip()
                    dict_datos['numero_documento']=str(row[3]).strip()
                    dict_datos['fecha_deuda']=str(row[4]).strip()
                    dict_datos['fecha_vencimiento']=str(row[5]).strip()
                    dict_datos['monto']=str(row[6]).strip()
                    list_datos.append(dict_datos)

            csv_file.close()
        self.dict_encabezado=dict_encabezado
        self.lista_datos=list_datos
        return True
