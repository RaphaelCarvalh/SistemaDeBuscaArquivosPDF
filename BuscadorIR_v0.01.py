import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
import os
from PIL import Image
import numpy as np
import cv2
import shutil
import tkinter as tk
from tkinter import filedialog

# Defina o caminho do executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\paTesseract\tesseract.exe'

# Função para extrair texto de PDFs textuais usando PyMuPDF
def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        # print(f"Texto extraído de {os.path.basename(pdf_path)} com sucesso.")
        return text
    except Exception as e:
        # print(f"Erro ao extrair texto de {os.path.basename(pdf_path)}: {e}")
        return ""

# Função para pré-processar imagens para OCR
def preprocess_image_for_ocr(image):
    # Converter para escala de cinza
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    # Remover ruído
    gray = cv2.medianBlur(gray, 3)
    # Aplicar binarização
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # Aumentar contraste
    binary = cv2.adaptiveThreshold(binary, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    # Redimensionar para melhorar a precisão
    height, width = binary.shape
    binary = cv2.resize(binary, (width * 2, height * 2), interpolation=cv2.INTER_LINEAR)
    return Image.fromarray(binary)

# Função para rotacionar a imagem para a orientação correta
def correct_orientation(image):
    return image  # Implemente a lógica de rotação conforme necessário

# Função para extrair texto de PDFs digitalizados usando OCR
def extract_text_from_scanned_pdf(pdf_path, temp_folder, search_text):
    try:
        # Ajustar o caminho do poppler
        poppler_path = r"C:\Program Files\poppler-0.68.0\bin"
        images = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)
        text = ""
        custom_oem_psm_config = r'--oem 3 --psm 6'  # Configurações do Tesseract
        for idx, image in enumerate(images):
            processed_image = preprocess_image_for_ocr(image)
            # Rotacionar a imagem para a orientação correta
            processed_image = correct_orientation(np.array(processed_image))
            processed_image = Image.fromarray(processed_image)
            image_path = os.path.join(temp_folder, f'processed_image_{idx}.png')
            processed_image.save(image_path)
            extracted_text = pytesseract.image_to_string(processed_image, config=custom_oem_psm_config)
            text += extracted_text + "\n"  # Adicionar quebra de linha para separar páginas
            # print(f"Texto extraído da página {idx+1} de {os.path.basename(pdf_path)} com sucesso.")
            # print(f"Texto extraído da página {extracted_text}")

        return text
    except Exception as e:
        # print(f"Erro ao extrair texto de {os.path.basename(pdf_path)}: {e}")
        return ""

# Função para abrir um explorador de arquivos e permitir ao usuário escolher a pasta com os PDFs
def choose_folder():
    input("Pressione Enter para escolher a pasta com os arquivos PDF...")
    root = tk.Tk()
    root.withdraw()  # Esconder a janela principal

    folder_selected = filedialog.askdirectory(title="Selecione a pasta com os arquivos PDF")
    return folder_selected

# Apresentação inicial ao usuário
def apresentacao():
    print("Bem-vindo ao buscador de frases em arquivos PDF.")
    print("Termos buscados:")
    search_phrases = [
        "lsencao do imposto de renda",
        "lsenção do imposto de renda",
        "Isenção de imposto de renda",
        "Isenção do imposto de renda"
    ]
    for term in search_phrases:
        print(f"- {term}")

# Função para realizar a busca nos arquivos PDF
def search_pdfs(pdf_folder_path):
    results = []
    temp_folder = os.path.join(pdf_folder_path, 'temp')
    os.makedirs(temp_folder, exist_ok=True)

    search_phrases = [
        "lsencao do imposto de renda",
        "lsenção do imposto de renda",
        "Isenção de imposto de renda",
        "Isenção do imposto de renda"
    ]

    # Iterar sobre as frases de busca
    for search_text in search_phrases:
        print(f"\nBuscando pela frase: {search_text}")
        # Iterar sobre os PDFs na pasta especificada
        for pdf_file in os.listdir(pdf_folder_path):
            if pdf_file.endswith(".pdf"):
                pdf_path = os.path.join(pdf_folder_path, pdf_file)
                print(f"Processando arquivo: {pdf_path}")

                # Primeiro, tentamos extrair o texto diretamente
                try:
                    extracted_text = extract_text_from_pdf(pdf_path)
                except Exception as e:
                    print(f"Erro ao extrair texto do PDF: {e}")
                    extracted_text = ""

                # Se não encontrar, tentamos OCR
                if search_text.lower() not in extracted_text.lower():
                    try:
                        extracted_text = extract_text_from_scanned_pdf(pdf_path, temp_folder, search_text)
                    except Exception as e:
                        print(f"Erro ao extrair texto de {os.path.basename(pdf_path)} usando OCR: {e}")
                        extracted_text = ""

                # Resultado da busca
                search_result = search_text.lower() in extracted_text.lower()
                if search_result:
                    print(f"***********************************Texto encontrado em: {pdf_file}")
                    results.append(pdf_file)

    # Remover a pasta temporária
    shutil.rmtree(temp_folder)

    return results

# Função para exibir os resultados e permitir ao usuário decidir o próximo passo
def show_results(results):
    if results:
        print("\nResultados encontrados:")
        for idx, result in enumerate(results, 1):
            print(f"{idx}. {result}")
    else:
        print("\nNenhum resultado encontrado.")

    # Solicitar ao usuário que decida o próximo passo
    while True:
        choice = input("\nPressione 'Enter' para fechar ou 'B' para buscar novamente: ").strip().lower()
        if choice == "":
            break
        elif choice == "b":
            return True
        else:
            print("Opção inválida. Por favor, escolha 'Enter' ou 'B'.")

    return False

# Função principal que organiza a execução do programa
def main():
    apresentacao()
    while True:
        pdf_folder_path = choose_folder()
        if not pdf_folder_path:
            break

        results = search_pdfs(pdf_folder_path)
        if not show_results(results):
            break

if __name__ == "__main__":
    main()
