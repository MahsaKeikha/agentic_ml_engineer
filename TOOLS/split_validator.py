from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class SplitValidator:
    def validate(self, split: Dict[str, Any]) -> Dict[str, Any]:
        train = int(split.get("train", 0)); valid = int(split.get("validation", 0)); test = int(split.get("test", 0))
        return {"train": train, "validation": valid, "test": test, "valid": train > 0 and valid > 0 and test > 0, "temporal_leakage_checked": bool(split.get("temporal_leakage_checked", False))}
