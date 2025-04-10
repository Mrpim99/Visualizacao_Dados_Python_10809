import pandas as pd
import matplotlib.pyplot as plot

# Exploração inicial 
file_path = "C:\\Users\\10293\\Documents\\Visualizacao_Dados_Python_10809\\Visualizacao_Dados_Python_10809\\02 uber_reviews_without_reviewid.csv"
df = pd.read_csv(file_path)
print(df.info())
print(df.head())


# Limepza de dados, coluna com dados NaN
df_cleaned = df.drop(columns=["userImage"])

#Substituir valores -- no caso os vazios

df_cleaned.fillna({"reviewCreatedVersion": "Desconhecido"}, inplace=True)
df_cleaned.fillna({"appVersion": "Desconhecido"}, inplace=True)

#

df_cleaned["score"].value_counts()

#Medidas estatísticas

df_cleaned["thumbsUpCount"].describe()

#Converter para formato data

df_cleaned["at"] = pd.to_datetime(df_cleaned["at"])

#

df_cleaned["at"].dt.date.value_counts().sort_index().head

#

df_cleaned[["replyContent","repliedAt"]].dropna().head()

#Correlações

df_cleaned[["score","thumbsUpCount"]].corr()

#Visualização dos dados, definição de gráfico, título

df_cleaned["score"].value_counts().plot(kind="bar", title="Distribuição de Avaliação")
plot.show()   

#Guardar ficheiro

df_cleaned.to_csv("C:\\Users\\10293\\Documents\\Visualizacao_Dados_Python_10809\\Visualizacao_Dados_Python_10809\\02 uber_reviews_cleaned.csv")
