import json
from pathlib import Path
from extractor import extract

results = []

for file in sorted(Path("samples").glob("*.txt")):
    text = file.read_text(encoding="utf-8")
    try:
        invoice = extract(text)
        results.append({"file": file.name, "data": invoice.model_dump()})
        print("OK :", file.name)
    except Exception as e:
        print("ERREUR :", file.name, type(e).__name__, "-", e)

Path("output.json").write_text(
    json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8"
)
print("Résultats écrits dans output.json")