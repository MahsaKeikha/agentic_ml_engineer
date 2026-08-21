from dataclasses import dataclass
from hashlib import sha256

@dataclass
class ArtifactHasher:
    def hash_text(self, value: str) -> str:
        return sha256(value.encode("utf-8")).hexdigest()
