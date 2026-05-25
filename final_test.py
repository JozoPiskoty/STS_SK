from scipy.stats import pearsonr, spearmanr, kendalltau

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

import numpy as np

from api_utils import get_sentence_lemmas
from api_utils import build_tree_from_concepts

from similarity import compute_similarity

from dataset_utils import load_dataset
from dataset_utils import stratified_split


dataset = load_dataset("sick_sk.txt")

train_data, test_data = stratified_split(dataset)

human_scores = []
model_scores = []

for i, (veta1, veta2, skore) in enumerate(test_data):

    print(f"{i}/{len(test_data)}")

    lemmas1 = get_sentence_lemmas(veta1)
    lemmas2 = get_sentence_lemmas(veta2)

    root = build_tree_from_concepts(
        list(set(lemmas1 + lemmas2))
    )

    sim = compute_similarity(
        lemmas1,
        lemmas2,
        root,
        matching="one_to_many",
        word_agg="max",
        sentence_agg="avg",
        direction="symmetric",
        similarity_type="wupalmer",
        power="power7",
        index_weight_type=None,
        power_scope="local"
    )

    model_scores.append(sim)
    human_scores.append(skore)

scaled_model_scores = [1 + s * 4 for s in model_scores]

pearson = pearsonr(human_scores, model_scores)[0]
spearman = spearmanr(human_scores, model_scores)[0]
kendall = kendalltau(human_scores, model_scores)[0]

mae = mean_absolute_error(human_scores, scaled_model_scores)

mse = mean_squared_error(human_scores, scaled_model_scores)
rmse = np.sqrt(mse)

mape = np.mean(
    np.abs(
        (np.array(human_scores) - np.array(scaled_model_scores))
        / np.array(human_scores)
    )
) * 100

r2 = r2_score(human_scores, scaled_model_scores)

print("Pearson:", pearson)
print("Spearman:", spearman)
print("Kendall Tau:", kendall)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("MAPE:", mape)

print("R2:", r2)
