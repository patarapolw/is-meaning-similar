from sentence_transformers import SentenceTransformer, util

import os


def is_meaning_similar(p1: str, p2: str):
    """Check if two sentences have similar meanings using a pre-trained model.
    Prefix p1 and p2 with the language code if necessary, e.g., "zh:" for Chinese and "ja:" for Japanese.

    Args:
        p1 (str): phrase in Japanese or Chinese
        p2 (str): another phrase in any language

    Returns:
        tuple: (similarity, is_similar)
            similarity: float - cosine similarity score between the two phrases
            is_similar: bool or None - True if similar, False if different, None if inconclusive
    """

    model = SentenceTransformer(
        os.getenv("PARAPHRASE_MODEL", "paraphrase-multilingual-MiniLM-L12-v2")
    )

    emb_jp = model.encode(p1, convert_to_tensor=True)
    emb_zh = model.encode(p2, convert_to_tensor=True)

    similarity = util.cos_sim(emb_jp, emb_zh).item()
    is_similar = None
    if similarity > float(os.getenv("PARAPHRASE_IS_SIMILAR", 0.7)):
        is_similar = True
    elif similarity < float(os.getenv("PARAPHRASE_IS_DIFFERENT", 0.5)):
        is_similar = False

    return similarity, is_similar
