from dataclasses import dataclass
from typing import Iterable, List

@dataclass
class MetricCalculator:
    def accuracy(self, y_true: Iterable[object], y_pred: Iterable[object]) -> float:
        truth: List[object] = list(y_true); pred: List[object] = list(y_pred)
        if not truth or len(truth) != len(pred):
            return 0.0
        return sum(1 for a, b in zip(truth, pred) if a == b) / len(truth)
