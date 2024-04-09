import pandas as pd

def leer_datos():
    "Esta función lee el archivo de una ruta y pasa la columna TS a Datetime"

    df = pd.read_csv("data/datos_examen.csv")
    df["TS"] = pd.to_datetime(df["TS"])
    return df

def filtrar_calcular_media(df):
    df_filtrado = df.loc[df["Tag"] == "Examen_Nimrod"]
    mean = df_filtrado["Value"].mean()
    return mean