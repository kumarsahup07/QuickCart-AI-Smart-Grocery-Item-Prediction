import json
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
# Also check parent directory for .env
load_dotenv(Path(__file__).resolve().parents[1] / ".env")


class OpenAIEmbeddingModel:
    def __init__(self, model: str = "text-embedding-3-small", cache_file: str | None = None):
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key) if api_key else None
        self.model = model
        possible_cache_paths = [
            Path(cache_file) if cache_file else None,
            Path(__file__).resolve().parent / "embeddings_cache.json",
            Path(__file__).resolve().parents[1] / "embeddings_cache.json",
            Path.cwd() / "embeddings_cache.json",
            Path.cwd() / "src" / "embeddings_cache.json",
        ]
        self.cache_path = next(
            (p for p in possible_cache_paths if p and p.exists()),
            Path(__file__).resolve().parent / "embeddings_cache.json",
        )
        self.cache: dict[str, list[float]] = {}
        if self.cache_path and self.cache_path.exists():
            try:
                self.cache = json.loads(self.cache_path.read_text(encoding="utf-8"))
            except Exception:
                self.cache = {}

    def embed(self, text: str) -> list[float]:
        text_clean = text.strip()
        if text_clean in self.cache:
            return self.cache[text_clean]

        if not self.client:
            api_key = os.getenv("OPENAI_API_KEY")
            if api_key:
                self.client = OpenAI(api_key=api_key)

        if not self.client:
            raise ValueError(
                "OPENAI_API_KEY is not set. Please provide a valid OPENAI_API_KEY in your .env file."
            )

        response = self.client.embeddings.create(
            input=text_clean,
            model=self.model,
        )
        embedding = response.data[0].embedding
        self.cache[text_clean] = embedding
        self._save_cache()
        return embedding

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        if not self.client:
            api_key = os.getenv("OPENAI_API_KEY")
            if api_key:
                self.client = OpenAI(api_key=api_key)

        missing_texts = [t.strip() for t in texts if t.strip() not in self.cache]

        if missing_texts and self.client:
            chunk_size = 100
            for i in range(0, len(missing_texts), chunk_size):
                chunk = missing_texts[i : i + chunk_size]
                try:
                    response = self.client.embeddings.create(
                        input=chunk,
                        model=self.model,
                    )
                    for item in response.data:
                        self.cache[chunk[item.index]] = item.embedding
                    self._save_cache()
                except Exception as e:
                    print(f"[OpenAIEmbeddingModel] Warning: Batch embedding error for chunk {i//chunk_size + 1}: {e}")

        # Return list preserving order and length
        results: list[list[float]] = []
        for t in texts:
            clean = t.strip()
            if clean in self.cache:
                results.append(self.cache[clean])
            else:
                # Fallback zero vector
                results.append([0.0] * 1536)
        return results

    def _save_cache(self):
        try:
            self.cache_path.write_text(json.dumps(self.cache, indent=2), encoding="utf-8")
        except Exception:
            pass

