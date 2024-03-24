import os
import numpy
import pickle
from numpy import dot
from numpy.linalg import norm


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(CURRENT_DIR + "/word_to_vector_trsf.pkl", "rb") as pk:
    word_to_vector = pickle.load(pk)


def cosine_similarity_1(vec_a, vec_b):
    numerator = sum([vec_a[i] * vec_b[i] for i in range(len(vec_a))])
    denominator = (norm(vec_a) * norm(vec_b))
    result = numerator / denominator

    if result < 0.5:
        print ("farther")
    else:
        print ("closer")

    return numerator / denominator

def cosine_similarity_2(vec_a, vec_b):
    numerator = sum([vec_a[i] * vec_b[i] for i in range(len(vec_a))])
    denominator = (sum([vec_a[i] ** 2 for i in range(len(vec_a))]) ** 0.5 * sum([vec_b[i] ** 2 for i in range(len(vec_b))]) ** 0.5)
    return numerator / denominator


def similar_words(word="tree", top_k=10):
    return sorted(
        word_to_vector.keys(),
        key=lambda x: -cosine_similarity_2(word_to_vector[x], word_to_vector[word])
    )[:top_k]


print(cosine_similarity_1(word_to_vector["plant"], word_to_vector["grow"]))
print(cosine_similarity_1(word_to_vector["minute"], word_to_vector["plant"]))
print(cosine_similarity_1(word_to_vector["plant"], word_to_vector["tree"]))

similar_words_result = similar_words("tree", top_k=10)
print("\n")
print(similar_words_result)
