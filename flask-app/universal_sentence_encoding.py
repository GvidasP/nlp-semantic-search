import os
import tensorflow_hub as hub
import numpy as np
import pandas as pd

# module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
module_path = r"C:\Users\gvida\Desktop\studies\naturalios_kalbos_apdorojimas\1uzduotis\app\flask-app\universal-sentence-encoder"
print("starting loading")

model = hub.load(module_path)

print('module loaded')

df_articles = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'df_articles.csv'))
df_articles_wsj = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'df_articles_wsj.csv'))

df_articles['Abstract'] = df_articles['Tag'].astype(str) + ', ' + df_articles['Headline'].astype(str) + ', ' + df_articles['Summary'].astype(str)
df_articles_wsj['Abstract'] = df_articles_wsj['Tag'].astype(str) + ', ' + df_articles_wsj['Headline'].astype(str) + ', ' + df_articles_wsj['Summary'].astype(str)


def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))


# Find articles by search_query
def search_articles(search_query):
    search_vector = model([search_query])[0]

    df_articles['Relevance'] = df_articles['Abstract'].map(lambda x: cosine(search_vector, model([x])[0]))

    result = df_articles.nlargest(5, 'Relevance')
    return result


# Find similar article from Financial Times (index) in Wall Street Journal
def find_similar_articles(article_index):
    search_vector = model([df_articles.iloc[article_index]['Abstract']])[0]
    df_articles_wsj['Relevance'] = df_articles_wsj['Abstract'].map(lambda x: cosine(search_vector, model([x])[0]))

    result = df_articles_wsj.nlargest(5, 'Relevance')
    return result
