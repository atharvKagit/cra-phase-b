"""Metrics helpers for CRA Semgrep review-quality testing."""


def average(values):
    total = sum(values)
    return total / len(values)
