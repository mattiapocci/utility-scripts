# 📄 PDF Merger

`merger.py` is a simple Python script that allows you to **combine multiple files (images or PDFs) into a single PDF document**.  
Images are automatically converted to PDF before merging, and the script interactively asks for the output filename.

---

## 🚀 Features

- Accepts both **image files** (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`) and **PDF documents**
- Automatically converts images to PDF
- Merges all files **in the specified order**
- Interactively asks for the output filename
- Removes temporary files after merging
- Lightweight and dependency-minimal

---

## 🧠 Requirements

You need **Python 3.8+** and the following packages installed:

```bash
pip install Pillow PyPDF2
```
---
## 🧩 Usage
Basic syntax
```bash
python merger.py file1 file2 file3 ...
```
---
🧹 Notes

- Files are added to the output PDF in the exact order they are provided.
- Temporary files (from image conversions) are automatically removed.
- If a file cannot be read or converted, it will be skipped with an error message.
- The resulting PDF will be saved in the same directory as the script.
