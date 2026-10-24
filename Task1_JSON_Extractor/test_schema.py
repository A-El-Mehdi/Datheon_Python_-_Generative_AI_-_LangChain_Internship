from schema import Invoice

# Cas 1 : des données correctes
bonne = Invoice(
    invoice_number="778",
    date="2025-09-12",
    vendor="Dupont & Fils",
    total=342.9,
    currency="EUR",
)
print("Accepté :", bonne)

# Cas 2 : un total qui n'est pas un nombre
try:
    Invoice(
        invoice_number="778",
        date="2025-09-12",
        vendor="Dupont & Fils",
        total="beaucoup",
        currency="EUR",
    )
except Exception as e:
    print("Refusé :", e)