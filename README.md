# is-meaning-similar

A simple HTTP server to check if two phrases have similar meanings using a multilingual sentence transformer model. Also with [example Anki integration.](/anki-template.html)

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

The server will start on `http://localhost:35026` by default.

### API

Prefix the phrases with `zh:` for Chinese, or `ja:` for Japanese to specify the language. If no prefix is provided, the app will attempt to detect the language automatically.

- **Endpoint:** `GET /?p1=<phrase1>&p2=<phrase2>`
- **Response:**
  ```json
  {
    "similarity": 0.85,
    "is_similar": true
  }
  ```

### Anki Integration

Use the provided [anki-template.html](/anki-template.html) as a custom card template. It sends the user's input to the server and colors the input box based on similarity.

### Website demo

Just run the server and open <http://localhost:35026/> in your browser to see the demo interface.

## Configuration

You can override defaults with environment variables:

- `PORT`: Server port (default: 35026)
- `PARAPHRASE_MODEL`: Sentence transformer model (default: paraphrase-multilingual-MiniLM-L12-v2)
- `PARAPHRASE_IS_SIMILAR`: Similarity threshold for "similar" (default: 0.7)
- `PARAPHRASE_IS_DIFFERENT`: Similarity threshold for "different" (default: 0.5)

### Recommended Models

| Model                                   | Size    | Notes                           |
| --------------------------------------- | ------- | ------------------------------- |
| `paraphrase-multilingual-MiniLM-L12-v2` | \~120MB | Works well across 50+ languages |
| `distiluse-base-multilingual-cased-v2`  | \~230MB | Higher quality, slower          |
| `sentence-transformers/LaBSE`           | \~1.2GB | Very accurate, by Google        |

## Typical Cosine Scores (for same meaning)

| Pair     | Score (Expected) |
| -------- | ---------------- |
| JP vs ZH | \~0.7–0.9        |
| JP vs EN | \~0.6–0.85       |
| ZH vs EN | \~0.75–0.95      |
