def encabezado():
    html="""
    <!DOCTYPE html>
    <html>
    <head>
     <meta charset="UTF-8">
    <title>Carta de Cobranza</title>
    </head>
    <body>
    <p><img src="logo.png" alt="" width="120" height="120" /></p>
    <div>
    <p>CARTA DE COBRANZA</p>
    </div>
    <div>
    <p>Estimado Sr: p_nombre, seg&uacute;n nuestros registros UD presenta documentos en estado de mora.</p>
    <p>Los documentos que se&ntilde;alaremos a continuaci&oacute;n deben ser regularizados:</p>
    </div>
    <div>
    <table style="width:80%">
        <thead>
            <tr>
                <th width="20%">Tipo</th>
                <th width="20%">Nro</th>
              	<th width="20%">Fecha Deuda</th>
              	<th width="20%">Fecha Vencimiento</th>
              	<th width="20%">Monto</th>
            </tr>
        </thead>
        <tbody>
    """
    return html
def tabla():
    html="""
        <tr>
            <td width="20%">p_tipo</td>
            <td width="20%">p_numero</td>
          	<td width="20%">p_fecha_1</td>
          	<td width="20%">p_fecha_2</td>
          	<td width="20%">p_monto</td>
        </tr>
    """
    return html

def pie():
    html = """
        </tbody>
     </table>
    </div>
    <div>
        <p>Favor, acercarse a regularizar su situaci&oacute;n a nuestras oficinas</p>
        <p>En el caso que UD, haya regularizado su situaci&oacute;n, favo no tomar encuenta esta carta.</p>
    </div>
        <div>
            <p>Saluda Attentamente a UD</p>
            <p>Jonathan W.</p>
            <p>Depto de Cobranzas.</p>
            <p>Depto de Cobranzas.</p>
        </div>
    </body>
    </html>"""
    return html
