import os
import tensorflow_hub as hub
import numpy as np
import pandas as pd

module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
print("starting loading")

model = hub.load(module_url)

print(f'module {module_url} loaded')

df_articles = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'df_articles.csv'))


def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))


def search_articles(search_query):
    search_vector = model([search_query])[0]
    df_articles['Relevance'] = df_articles['Summary'].map(lambda x: cosine(search_vector, model([x])[0]))

    result = df_articles.nlargest(5, 'Relevance')
    return result
