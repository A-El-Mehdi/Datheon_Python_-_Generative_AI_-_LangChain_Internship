import json
from pathlib import Path
from extractor import extract

output_file = Path("output.json")

if output_file.exists():
    results = json.loads(output_file.read_text(encoding="utf-8"))
else:
    results = []

done = {r["file"] for r in results}

for file in sorted(Path("samples").glob("*.txt")):
    if file.name in done:
        print("DÉJÀ FAIT :", file.name)
        continue
    text = file.read_text(encoding="utf-8")
    try:
        invoice = extract(text)
        results.append({"file": file.name, "data": invoice.model_dump()})
        print("OK :", file.name)
    except Exception as e:
        print("ERREUR :", file.name, type(e).__name__, "-", str(e)[:150])
    results.sort(key=lambda r: r["file"])
    output_file.write_text(
        json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8"
    )

print("Résultats écrits dans output.json")
