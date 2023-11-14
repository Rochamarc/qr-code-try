import qrcode

def gerar_qr_code(link, nome_arquivo):
    # Cria um objeto QRCode
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,)

    # Adiciona os dados ao QRCode
    qr.add_data(link)
    qr.make(fit=True)

    # Cria uma imagem QRCode
    img = qr.make_image(fill_color="black", back_color="white")

    # Salva a imagem como um arquivo PNG
    img.save(nome_arquivo)

if __name__ == "__main__":
    # Solicita o link do usuário
    link = input("Digite o link para o QR code: ")
    
    # Define o nome do arquivo de saída
    nome_arquivo = input("Digite o nome do arquivo de saída (sem extensão): ") + ".png"

    # Gera o QR code e salva como PNG
    gerar_qr_code(link, nome_arquivo)

    print(f"O QR code foi gerado e salvo como {nome_arquivo}.")
