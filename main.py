import os
from tkinter import Tk, filedialog
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Configure o caminho do executável do Tesseract, se necessário
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_image_to_text():
    """
    Realiza OCR em uma imagem selecionada pelo usuário, imprime o texto extraído e salva o resultado na área de trabalho.
    """
    try:
        # Abre a janela de seleção de arquivo
        Tk().withdraw()  # Oculta a janela principal do Tkinter
        image_path = filedialog.askopenfilename(
            title="Selecione a imagem",
            filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp *.tiff *.tif")]
        )

        if not image_path:
            print("Nenhuma imagem foi selecionada.")
            return

        # Extrai o texto da imagem
        img = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(img, lang='por')  # Idioma 'por' para português

        # Define o caminho para salvar o texto na área de trabalho
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        output_file = os.path.join(desktop_path, "texto_extraido.txt")

        # Salva o texto extraído em um arquivo
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(extracted_text)

        # Exibe o texto extraído
        print("Texto extraído da imagem:")
        print("\033[94m" + extracted_text + "\033[0m")
        print(f"\nO texto foi salvo em: {output_file}")

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")


if __name__ == "__main__":
    ocr_image_to_text()
