# is-meaning-similar

A simple HTTP server and web interface to check if two phrases have similar meanings using a multilingual sentence transformer model.

## Features

- REST API to compare the meaning of two phrases in any language.
- Web UI template for Anki integration.
- Uses [sentence-transformers](https://www.sbert.net/) for semantic similarity.

## Requirements

- Python 3.12
- pipenv (for dependency management)

## Installation

1. Clone the repository.
2. Install dependencies:

   ```sh
   pipenv install
   ```

## Usage

### Start the Server

```sh
pipenv run python server.py
```

The server will start on [http://localhost:35026](http://localhost:35026) by default.

### API

- **Endpoint:** `GET /?p1=<phrase1>&p2=<phrase2>`
- **Response:**
  ```json
  {
    "similarity": 0.85,
    "is_similar": true
  }
  ```

### Anki Integration

Use the provided [anki-template.html](anki-template.html) as a custom card template. It sends the user's input to the server and colors the input box based on similarity.

## Files

- [`server.py`](server.py): HTTP server implementation.
- [`is_meaning_similar.py`](is_meaning_similar.py): Semantic similarity logic.
- [`anki-template.html`](anki-template.html): Anki card template for web integration.

## Configuration

You can override defaults with environment variables:

- `PORT`: Server port (default: 35026)
- `PARAPHRASE_MODEL`: Sentence transformer model (default: paraphrase-multilingual-MiniLM-L12-v2)
- `PARAPHRASE_IS_SIMILAR`: Similarity threshold for "similar" (default: 0.7)
- `PARAPHRASE_IS_DIFFERENT`: Similarity threshold for "different" (default: 0.5)

### 🔹 Recommended Models

| Model                                   | Size    | Notes                           |
| --------------------------------------- | ------- | ------------------------------- |
| `paraphrase-multilingual-MiniLM-L12-v2` | \~120MB | Works well across 50+ languages |
| `distiluse-base-multilingual-cased-v2`  | \~230MB | Higher quality, slower          |
| `sentence-transformers/LaBSE`           | \~1.2GB | Very accurate, by Google        |

📌 These can compare:

* Japanese ↔ Chinese
* Japanese ↔ English
* Chinese ↔ English

## ✅ Typical Cosine Scores (for same meaning)

| Pair     | Score (Expected) |
| -------- | ---------------- |
| JP vs ZH | \~0.7–0.9        |
| JP vs EN | \~0.6–0.85       |
| ZH vs EN | \~0.75–0.95      |
