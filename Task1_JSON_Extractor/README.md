# Task 1 : Structured LLM Prompt Pipeline & JSON Extractor

Script Python qui extrait des données structurées (facture) à partir de texte libre
avec l'API Google Gemini, puis valide le résultat avec Pydantic.

## Fonctionnement

1. `main.py` lit chaque fichier `.txt` du dossier `samples/`.
2. `extractor.py` envoie le texte à Gemini avec un prompt paramétré et un exemple (few-shot).
3. La réponse JSON est validée par le schéma `Invoice` (`schema.py`).
4. En cas d'erreur serveur ou de coupure réseau, la requête est retentée (3 essais maximum).
5. Les résultats sont écrits dans `output.json`.

## Installation

```
pip install -r requirements.txt
```

## Clé API

Créer une clé sur Google AI Studio, puis la stocker dans une variable d'environnement
(Windows) :

```
setx GEMINI_API_KEY "votre_cle"
```

Redémarrer ensuite le terminal. La clé n'est jamais écrite dans le code.

## Lancer

```
python main.py
```

## Exemple

Entrée :

```
Facture N°778 du 12/09/2025, Dupont & Fils, total 342.90 EUR
```

Sortie :

```json
{
  "invoice_number": "778",
  "date": "2025-09-12",
  "vendor": "Dupont & Fils",
  "total": 342.9,
  "currency": "EUR"
}
```

## Limites connues

- L'offre gratuite de Gemini limite le nombre de requêtes par jour (erreur 429).
- Le numéro de facture et la date sont facultatifs (`null` s'ils sont absents du texte) ; le vendeur, le total et la devise restent obligatoires.