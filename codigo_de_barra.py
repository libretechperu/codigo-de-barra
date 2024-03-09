import barcode
from barcode.writer import ImageWriter

def generar_codigo(numero, formato='code39', salida='codigo'):
    codigo = barcode.get_barcode_class(formato)
    codigo_de_barras = codigo(numero, writer=ImageWriter())
    archivo_salida = salida + '.png'
    codigo_de_barras.save(archivo_salida)
    print(f'Se ha generado el código de barras y se ha guardado en {archivo_salida}')

# ---------------------------------------
#  NUMERO A CONVERTIR
# ---------------------------------------
    
numero_a_convertir = '40181700982'

# ----------------------------------------
#  GENERANDO CODIGO DE BARRA
# ----------------------------------------

generar_codigo(numero_a_convertir)
