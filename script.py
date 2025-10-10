import pandas as pd

final_df = pd.DataFrame()
for year in range(2014, 2022):
  df_accident = pd.read_csv(f"./Tieliikenneonnettomuudet_{year}/tieliikenneonnettomuudet_{year}_onnettomuus.csv", encoding = "latin-1",sep = ";")
  df_vehicle = pd.read_csv(f"./Tieliikenneonnettomuudet_{year}/tieliikenneonnettomuudet_{year}_osallinen.csv", encoding = "latin-1",sep = ";")
  df_comb = pd.merge(df_accident, df_vehicle, on='Onnett_id', how='inner')
  df_clean_accident = df_comb.sort_values("Onnett_id")[["Onnett_id", "Vuosi", "Kk", "Vkpv", "X", "Y", "Ajoneuvmas", "Vakavuus"]]
  df_clean_accident.rename(columns={
      'Onnett_id': 'id',
      'Vuosi': 'year',
      'Kk': 'month',
      'Vkpv': 'day_of_week',
      "X": "x",
      "Y": "y",
      "Ajoneuvmas": "vehicle_mass",
      "Vakavuus": "Seriousness"
  }, inplace=True)
  final_df = pd.concat([final_df, df_clean_accident], ignore_index=True)
final_df.to_csv("data.csv")
