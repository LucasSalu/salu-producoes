# -*- coding: utf-8 -*-
"""Extrai texto/metadados do catalogo de pacotes (PDF) para planejamento do site."""
import os
import sys
import json
import importlib

PDF = r"C:\dev\deepseek\salu_producoes\Pacotes Oficial Casamento 2026 (1).pdf"

print("PDF:", PDF)
print("Existe:", os.path.exists(PDF))
if os.path.exists(PDF):
    print("Tamanho (bytes):", os.path.getsize(PDF))

mods = {}
for name in ("pypdf", "PyPDF2", "pdfplumber", "fitz"):
    try:
        importlib.import_module(name)
        mods[name] = "OK"
    except Exception as exc:  # noqa: BLE001
        mods[name] = f"FALHOU: {exc.__class__.__name__}"
print("Bibliotecas:", json.dumps(mods, ensure_ascii=False, indent=2))

if not os.path.exists(PDF):
    sys.exit(1)

extracted = None

# 1) PyMuPDF (fitz) costuma ser o mais robusto
try:
    import fitz  # type: ignore

    doc = fitz.open(PDF)
    print("Paginas (fitz):", doc.page_count)
    parts = []
    for i, page in enumerate(doc):
        parts.append(f"\n===== PAGINA {i + 1} =====\n")
        parts.append(page.get_text("text"))
    extracted = "".join(parts)
except Exception as exc:  # noqa: BLE001
    print("fitz indisponivel:", exc)

# 2) pypdf
if extracted is None:
    try:
        from pypdf import PdfReader  # type: ignore

        reader = PdfReader(PDF)
        print("Paginas (pypdf):", len(reader.pages))
        parts = []
        for i, page in enumerate(reader.pages):
            parts.append(f"\n===== PAGINA {i + 1} =====\n")
            parts.append(page.extract_text() or "")
        extracted = "".join(parts)
    except Exception as exc:  # noqa: BLE001
        print("pypdf indisponivel:", exc)

# 3) pdfplumber
if extracted is None:
    try:
        import pdfplumber  # type: ignore

        with pdfplumber.open(PDF) as pdf:
            print("Paginas (pdfplumber):", len(pdf.pages))
            parts = []
            for i, page in enumerate(pdf.pages):
                parts.append(f"\n===== PAGINA {i + 1} =====\n")
                parts.append(page.extract_text() or "")
            extracted = "".join(parts)
    except Exception as exc:  # noqa: BLE001
        print("pdfplumber indisponivel:", exc)

if extracted:
    print("Caracteres:", len(extracted))
    print("\n===== TEXTO COMPLETO =====\n")
    print(extracted)
else:
    print("\nNENHUMA BIBLIOTECA DE PDF DISPONIVEL. Ser necessario renderizar as paginas em imagem.")
