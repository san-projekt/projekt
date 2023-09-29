import pandas as pd
import numpy as np

def generate_xlsx_for_gephi():
    # Prepare df
    df = pd.read_excel("data/Liste_Raumsonden.xlsx")
    df = df.rename(columns={"Name der Sonde":  "ID", "Missonsname/": "Missionsname"})

    # Generate Knoten df
    unique_raumsonden = df["Missionsziele"].unique()

    new_rows = {
        "Nation oder": [np.nan] * len(unique_raumsonden),
        "ID": unique_raumsonden,
        "Typ": ["Himmelskörper"] * len(unique_raumsonden),
        "Missionsname": [np.nan] * len(unique_raumsonden),
        "Von": [np.nan] * len(unique_raumsonden),
        "Bis": [np.nan] * len(unique_raumsonden),
        "Status": [np.nan] * len(unique_raumsonden),
        "Missionsziele": [np.nan] * len(unique_raumsonden)
    }
    new_df = pd.DataFrame(new_rows)

    df_knoten = pd.concat([df, new_df], ignore_index=True)

    # Generate Kanten df
    df_kanten = df[["ID", "Missionsziele"]]
    df_kanten = df_kanten.rename(columns={"ID": "Source", "Missionsziele": "Target"})

    # Write to excel
    with pd.ExcelWriter("data/ready_for_gephi.xlsx") as writer:
        df_knoten.to_excel(writer, sheet_name="Knoten", index=False)
        df_kanten.to_excel(writer, sheet_name="Kanten", index=False)