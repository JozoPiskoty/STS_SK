import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu

df = pd.read_csv("pearson_results_final_final.csv", sep=";")

plt.figure(figsize=(10,6))
df.boxplot(column="pearson", by="similarity_type")
plt.title("Pearson score podľa algoritmu podobnosti")
plt.suptitle("")
plt.xlabel("Algoritmus podobnosti")
plt.ylabel("Pearson score")
plt.tight_layout()
plt.savefig("boxplot_similarity_type.png")
plt.show()

plt.figure(figsize=(10,6))
df.boxplot(column="pearson", by="word_agg")
plt.title("Pearson score podľa agregácie na úrovni slov")
plt.suptitle("")
plt.xlabel("Agregácia")
plt.ylabel("Pearson score")
plt.tight_layout()
plt.savefig("boxplot_word_agg.png")
plt.show()

plt.figure(figsize=(10,6))
df.boxplot(column="pearson", by="matching")
plt.title("Pearson score podľa spôsobu párovania slov")
plt.suptitle("")
plt.xlabel("Párovanie slov")
plt.ylabel("Pearson score")
plt.tight_layout()
plt.savefig("boxplot_matching.png")
plt.show()

wu = df[df["similarity_type"] == "wupalmer"]["pearson"]
spath = df[df["similarity_type"] == "spath"]["pearson"]
lch = df[df["similarity_type"] == "lch"]["pearson"]

wu_lch = mannwhitneyu(wu, lch)
wu_spath = mannwhitneyu(wu, spath)
spath_lch = mannwhitneyu(spath, lch)

print("Wu-Palmer vs Leacock-Chodorow")
print("U statistic:", wu_lch.statistic)
print("p-value:", wu_lch.pvalue)
print()

print("Wu-Palmer vs Shortest Path")
print("U statistic:", wu_spath.statistic)
print("p-value:", wu_spath.pvalue)
print()

print("Shortest Path vs Leacock-Chodorow")
print("U statistic:", spath_lch.statistic)
print("p-value:", spath_lch.pvalue)
print()
