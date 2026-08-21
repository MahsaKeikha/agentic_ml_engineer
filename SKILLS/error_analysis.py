from collections import Counter
from typing import Iterable, Dict

def error_analysis(labels: Iterable[str]) -> Dict[str, object]:
    counts = Counter(labels)
    return {"error_counts": dict(counts), "largest_error_group": counts.most_common(1)[0][0] if counts else None}
