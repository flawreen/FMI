import typing


def leven(str1: str, str2: str) -> int:
    m: int = len(str1)
    n: int = len(str2)

    mat = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
