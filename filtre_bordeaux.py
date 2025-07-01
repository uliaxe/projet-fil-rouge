import pandas as pd

# Bordeaux Métropole - codes INSEE sur 3 chiffres à 5 chiffres
codes_cub = [
    "00029", "00042", "00051", "00073", "00187", "00312", "00336",
    "00348", "00350", "00394", "00436", "00450", "00498", "00519",
    "00555", "33063", "33192", "33200", "33249", "33281", "33318", 
    "33422", "33433", "33522", "33550", "33563", "33585", "33615", 
    "33627", "33644", "33673", "33762", "33991"
]

# 🔁 Lecture des fichiers 2005
try:
    carac_2005 = pd.read_csv("donnee_accident/Donnee_2005/caracteristiques-2005.csv", sep=",", encoding="latin1")
    lieux_2005 = pd.read_csv("donnee_accident/Donnee_2005/lieux-2005.csv", sep=",", encoding="latin1")
except Exception as e:
    print(f"Erreur de lecture : {e}")
    exit()

# 📌 Nettoyage et format des colonnes
carac_2005["com"] = carac_2005["com"].astype(str).str.zfill(5)
carac_2005["dep"] = carac_2005["dep"].astype(str).str.zfill(3)
lieux_2005["Num_Acc"] = lieux_2005["Num_Acc"].astype(str)

# 🎯 Filtrage CUB
df_cub = carac_2005[
    (carac_2005["dep"] == "330") & (carac_2005["com"].isin(codes_cub))
].copy()

# 🧩 Fusion avec lieux pour ne garder que les lignes correspondant à df_cub
lieux_cub = lieux_2005[lieux_2005["Num_Acc"].isin(df_cub["Num_Acc"])].copy()

print(f"✔️ 2005 : {len(df_cub)} accidents retenus pour Bordeaux + Métropole")

# 💾 Export
df_cub.to_csv("accidents_bordeaux_cub_2005.csv", index=False)
lieux_cub.to_csv("lieux_bordeaux_cub_2005.csv", index=False)
