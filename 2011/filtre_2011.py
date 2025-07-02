import pandas as pd
import os

# 📁 Chemins fichiers 2011
chemin_carac = "donnee_accident/Donnee_2011/caracteristiques-2011.csv"
chemin_lieux = "donnee_accident/Donnee_2011/lieux-2011.csv"

if not os.path.exists(chemin_carac) or not os.path.exists(chemin_lieux):
    print("❌ Fichier(s) introuvable(s). Vérifie les chemins.")
    exit()

print("📂 Traitement 2011 en cours...")

try:
    carac = pd.read_csv(chemin_carac, sep=",", encoding="latin1")
    lieux = pd.read_csv(chemin_lieux, sep=",", encoding="latin1")
except Exception as e:
    print(f"❌ Erreur lors de la lecture des fichiers : {e}")
    exit()

try:
    df = pd.merge(carac, lieux, on="Num_Acc", how="left")
except KeyError as e:
    print(f"❌ Problème lors de la fusion : {e}")
    exit()

df["dep"] = df["dep"].astype(str).str.zfill(3)
df_bordeaux = df[df["dep"].isin(["033", "330"])].copy()

try:
    df_bordeaux["lat"] = df_bordeaux["lat"].astype(float) / 100000
    df_bordeaux["long"] = df_bordeaux["long"].astype(float) / 100000
except Exception as e:
    print(f"⚠️ Erreur lors de la conversion des coordonnées : {e}")

output_file = "accidents_bordeaux_2011.csv"
df_bordeaux.to_csv(output_file, index=False, encoding="utf-8")

print(f"✅ Export terminé : {len(df_bordeaux)} accidents à Bordeaux + CUB sauvegardés dans '{output_file}'")
