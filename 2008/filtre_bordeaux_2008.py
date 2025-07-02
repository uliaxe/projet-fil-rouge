import pandas as pd
import os

# 📁 Chemins des fichiers 2008
chemin_carac = "donnee_accident/Donnee_2008/caracteristiques-2008.csv"
chemin_lieux = "donnee_accident/Donnee_2008/lieux-2008.csv"

# ✅ Vérification des fichiers
if not os.path.exists(chemin_carac) or not os.path.exists(chemin_lieux):
    print("❌ Fichier(s) introuvable(s). Vérifie les chemins.")
    exit()

print("📂 Traitement des données 2008 en cours...")

# 📊 Lecture des CSV
try:
    carac = pd.read_csv(chemin_carac, sep=",", encoding="latin1")
    lieux = pd.read_csv(chemin_lieux, sep=",", encoding="latin1")
except Exception as e:
    print(f"❌ Erreur lors de la lecture : {e}")
    exit()

# 🔗 Fusion sur Num_Acc
try:
    df = pd.merge(carac, lieux, on="Num_Acc", how="left")
except KeyError as e:
    print(f"❌ Problème lors de la fusion : {e}")
    exit()

# 🧹 Nettoyage et filtrage Bordeaux + CUB (dep 033 et 330)
df["dep"] = df["dep"].astype(str).str.zfill(3)
df_bordeaux = df[df["dep"].isin(["033", "330"])].copy()

# 🌍 Conversion des coordonnées
try:
    df_bordeaux["lat"] = df_bordeaux["lat"].astype(float) / 100000
    df_bordeaux["long"] = df_bordeaux["long"].astype(float) / 100000
except Exception as e:
    print(f"⚠️ Erreur lors de la conversion des coordonnées : {e}")

# 💾 Export
output_file = "accidents_bordeaux_2008.csv"
df_bordeaux.to_csv(output_file, index=False, encoding="utf-8")

# ✅ Résumé
print(f"✅ Export terminé : {len(df_bordeaux)} accidents à Bordeaux + CUB sauvegardés dans '{output_file}'")
