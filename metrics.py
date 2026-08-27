"""CRA review test: Semgrep should flag division by len() on empty input."""


def average_scores(scores):
    total = sum(scores)
    return total / len(scores)
