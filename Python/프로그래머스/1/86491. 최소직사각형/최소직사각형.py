def solution(sizes):
    wmax, hmax = 0, 0
    for w, h in sizes:
        wmax = max(wmax, max(w, h))
        hmax = max(hmax, min(w, h))
    return wmax * hmax