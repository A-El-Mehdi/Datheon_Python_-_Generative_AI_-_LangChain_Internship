import time
import httpx
from google import genai
from google.genai import types, errors
from schema import Invoice

client = genai.Client()

PROMPT = """Extrais les informations de la facture ci-dessous.
Réponds uniquement avec un JSON ayant ces clés : invoice_number, date, vendor, total, currency.
La date doit être au format AAAA-MM-JJ. Le total doit être un nombre.
La devise doit être un code ISO à 3 lettres (par exemple EUR, USD).
Si une information est absente du texte, mets null pour cette clé.

Exemple :
Texte : "Facture N°A12 du 3 mars 2024, Acme SARL, montant 120,50 EUR"
JSON : {{"invoice_number": "A12", "date": "2024-03-03", "vendor": "Acme SARL", "total": 120.5, "currency": "EUR"}}

Texte : "{text}"
JSON :"""


def extract(text, max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=PROMPT.format(text=text),
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    temperature=0,
                ),
            )
            return Invoice.model_validate_json(response.text)
        except (errors.ServerError, httpx.TransportError) as e:
            print(f"Essai {attempt}/{max_attempts} échoué : {type(e).__name__}")
            if attempt == max_attempts:
                raise
            time.sleep(2 * attempt)


if __name__ == "__main__":
    texte = "Facture N°778 du 12/09/2025, Dupont & Fils, total 342.90 EUR"
    facture = extract(texte)
    print(facture)
    print("Le total est :", facture.total)