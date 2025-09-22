import pandas as pd

data = {
    "Département": ["Informatique", "Informatique", "Mathematiques", "Physique"],
    "Centre": ["Centre A", "Centre A", "Centre B", "Centre C"],
    "Filiere": ["Développement", "Développement", "Statistiques", "Astrophysique"],
    "Niveau": ["Licence", "Master", "Licence", "Master"]
}

df = pd.DataFrame(data)
df.to_excel("test_import.xlsx", index=False)
print("Fichier créé : test_import.xlsx")