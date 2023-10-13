from sentence_transformers import SentenceTransformer, util
import torch


def find_top_similar_sentences(queries, corpus, model_name='all-MiniLM-L6-v2', top_k=5):
    """
    Find the top similar sentences for a list of queries in a corpus.

    Args:
        queries (list): List of query sentences.
        corpus (list): List of sentences in the corpus.
        model_name (str): Name of the sentence embedding model.
        top_k (int): Number of top similar sentences to retrieve.

    Returns:
        list: A list of tuples, each containing the query sentence and a list of top similar sentences.
    """
    embedder = SentenceTransformer(model_name)
    corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)

    results = []
    for query in queries:
        query_embedding = embedder.encode(query, convert_to_tensor=True)
        cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]
        top_results = torch.topk(cos_scores, k=min(top_k, len(corpus)))
        query_results = [(corpus[idx], score.item()) for score, idx in zip(top_results[0], top_results[1])]
        results.append((query, query_results))

    return results


if __name__ == "__main__":
    # Define the corpus sentences
    corpus = [
        'A man is eating food.', 'A man is eating a piece of bread.', 'The girl is carrying a baby.', 'A man is riding a horse.', 'A woman is playing violin.', 'Two men pushed carts through the woods.', 'A man is riding a white horse on an enclosed ground.', 'A monkey is playing drums.',
        'A cheetah is running behind its prey.'
    ]

    # Define query sentences
    queries = ['A man is eating pasta.', 'Someone in a gorilla costume is playing a set of drums.', 'A cheetah chases prey on across a field.']

    # Find and print the top similar sentences for each query
    results = find_top_similar_sentences(queries, corpus)

    for query, query_results in results:
        print("\n======================\n")
        print("Query:", query)
        print("\nTop 5 most similar sentences in the corpus:")
        for sentence, score in query_results:
            print(f"{sentence} (Score: {score:.4f})")