from barcode import EAN13
from barcode.writer import ImageWriter

import pyqrcode
from pyqrcode import QRCode

# Funções ###################################################################################################
# Gera o código de barras e salva no caminho desejado #
def GeraCode(vTipo, vConteudoCode, vDir, vFileName ):

    if vTipo == 'bar-code':
        
        if len(vConteudoCode) < 12:
            return 'Erro menos de 12 caracteres'

        # Monta Código de Barras
        with open(r''+vDir + vFileName, 'wb') as f:
            EAN13(vConteudoCode, writer=ImageWriter()).write(f)

    elif vTipo == 'qrcode': 
        # Monta o QRCode #
        url = pyqrcode.create(vConteudoCode)

        # Salva o QRCode gerado no local desejado #
        url.png(r''+vDir + vFileName, scale=8)
    else:
        print('Não encontrado')

    open(r''+vDir + vFileName,'r')

#End Funções ###########################################################################################

vDir = r"C:\Users\Henrique\Desktop\Programming\Python\bar-code-generator-main\ "
vTipoCodigo = int(input('Informe o Tipo de código: \n1 - Código de Barras \n2 - QR Code \nResposta: '))



if vTipoCodigo == 1 or vTipoCodigo == 2 : 
    
    if vTipoCodigo == 1:
        vTipo = 'bar-code'
        vBarCode = input('Informe o Código: ')
    else:
        vTipo = 'qrcode' 
        vBarCode = input('Informe a URL: ')

    vFileName  = input('Informe o nome do arquivo: ')+'.png'
    vValidacao = True

else:
    print('Tipo Inválido')  
    vValidacao = False

if vValidacao == True:
    GeraCode(vTipo, vBarCode, vDir, vFileName)