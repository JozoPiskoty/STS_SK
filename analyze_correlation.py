import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pearson_results_final_final.csv", sep=";")

df_encoded = pd.get_dummies(df)
corr = df_encoded.corr()
pearson_corr = corr["pearson"]
pearson_corr = pearson_corr.drop("pearson")
pearson_corr = pearson_corr.sort_values()

print(pearson_corr)

plt.figure(figsize=(12,8))

pearson_corr.plot(kind="barh")

plt.xlabel("Correlation with Pearson score")
plt.ylabel("Parameters")
plt.title("Korelácia parametrov s Pearson score")

plt.tight_layout()
plt.show() 
