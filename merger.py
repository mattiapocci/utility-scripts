import sys
import os
from PIL import Image
from PyPDF2 import PdfMerger

def convert_to_pdf(input_file):
    """Converte un'immagine in PDF temporaneo, restituisce il path del PDF."""
    if input_file.lower().endswith(".pdf"):
        return input_file  # già PDF, non serve conversione

    try:
        img = Image.open(input_file)
        # Conversione in RGB per evitare errori con PNG trasparenti o simili
        img = img.convert("RGB")
        pdf_temp = input_file + ".temp.pdf"
        img.save(pdf_temp)
        return pdf_temp
    except Exception as e:
        print(f"❌ Errore nella conversione di {input_file}: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Uso: python unisci_pdf.py file1 [file2 ...]")
        sys.exit(1)

    input_files = sys.argv[1:]

    # Chiedi all'utente il nome dell'output
    output_name = input("Inserisci il nome del file PDF di output (senza estensione): ").strip()
    if not output_name:
        output_name = "output"
    output_path = output_name + ".pdf"

    merger = PdfMerger()
    temp_files = []

    for file in input_files:
        pdf_path = convert_to_pdf(file)
        if pdf_path:
            merger.append(pdf_path)
            if pdf_path.endswith(".temp.pdf"):
                temp_files.append(pdf_path)

    try:
        merger.write(output_path)
        merger.close()
        print(f"✅ PDF creato con successo: {output_path}")
    except Exception as e:
        print(f"❌ Errore durante la creazione del PDF: {e}")
    finally:
        # Rimuove eventuali PDF temporanei
        for temp in temp_files:
            try:
                os.remove(temp)
            except:
                pass

if __name__ == "__main__":
    main()
