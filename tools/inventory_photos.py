# -*- coding: utf-8 -*-
"""Inventario do acervo de fotos: resolucao, orientacao, duplicatas e pastas."""
import os
import re
import sys
import json
from collections import Counter, defaultdict

from PIL import Image, ImageOps

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = r"C:\dev\deepseek\salu_producoes\melhores fotos"
EXTS = (".jpg", ".jpeg", ".png", ".webp", ".heic")

files = []
for dirpath, _dirnames, filenames in os.walk(ROOT):
    for fn in filenames:
        if fn.lower().endswith(EXTS):
            files.append(os.path.join(dirpath, fn))

print("TOTAL DE ARQUIVOS:", len(files))

records = []
errors = []
for path in files:
    try:
        with Image.open(path) as im:
            im = ImageOps.exif_transpose(im)
            w, h = im.size
            fmt = im.format
        size = os.path.getsize(path)
        records.append({
            "path": path,
            "rel": os.path.relpath(path, ROOT),
            "w": w, "h": h,
            "bytes": size,
            "portrait": h > w,
            "square": h == w,
            "format": fmt,
        })
    except Exception as exc:  # noqa: BLE001
        errors.append((path, str(exc)))

print("LIDOS:", len(records), "| ERROS:", len(errors))
if errors:
    print("ERROS:", errors[:5])

orient = Counter("retrato" if r["portrait"] else ("quadrada" if r["square"] else "paisagem") for r in records)
print("ORIENTACAO:", dict(orient))

mb_total = sum(r["bytes"] for r in records) / (1024 * 1024)
print(f"PESO TOTAL: {mb_total:.1f} MB")

res_buckets = Counter()
for r in records:
    long_side = max(r["w"], r["h"])
    if long_side >= 3000:
        res_buckets[">=3000px (alta)"] += 1
    elif long_side >= 2000:
        res_buckets["2000-2999px (boa)"] += 1
    elif long_side >= 1200:
        res_buckets["1200-1999px (média)"] += 1
    else:
        res_buckets["<1200px (baixa)"] += 1
print("RESOLUCAO (lado maior):", dict(res_buckets))

# Pastas
folders = Counter(os.path.dirname(r["rel"]) or "(raiz)" for r in records)
print("PASTAS:", dict(folders))

# Duplicatas por nome base (remove sufixos -2, (1), ~2, etc.)
def base_key(name):
    stem = os.path.splitext(name)[0]
    stem = re.sub(r"\s*\(\d+\)", "", stem)
    stem = re.sub(r"[-_~]\d+$", "", stem)
    return stem.lower().strip()

groups = defaultdict(list)
for r in records:
    groups[base_key(os.path.basename(r["path"]))].append(r["rel"])

dups = {k: v for k, v in groups.items() if len(v) > 1}
print("NOMES BASE UNICOS:", len(groups), "| COM DUPLICATAS:", len(dups))
print("ARQUIVOS REPETIDOS (extra):", sum(len(v) - 1 for v in dups.values()))

# duplicatas exatas (mesmo tamanho + dimensoes)
sig = defaultdict(list)
for r in records:
    sig[(r["w"], r["h"], r["bytes"])].append(r["rel"])
exact = {k: v for k, v in sig.items() if len(v) > 1}
print("GRUPOS IDENTICOS (mesmo byte):", len(exact))

print("\n===== RESUMO JSON =====")
summary = {
    "total": len(records),
    "orientacao": dict(orient),
    "peso_total_mb": round(mb_total, 1),
    "resolucao": dict(res_buckets),
    "pastas": dict(folders),
    "nomes_base_unicos": len(groups),
    "grupos_com_duplicata": len(dups),
    "arquivos_repetidos_extra": sum(len(v) - 1 for v in dups.values()),
    "grupos_identicos": len(exact),
    "menores": sorted([{"rel": r["rel"], "w": r["w"], "h": r["h"]} for r in records], key=lambda x: x["w"] * x["h"])[:5],
}
print(json.dumps(summary, ensure_ascii=False, indent=2))
