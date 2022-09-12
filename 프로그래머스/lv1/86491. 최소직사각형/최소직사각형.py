def solution(sizes):
    sorted_sizes = []
    for size in sizes:
        sorted_sizes.append(sorted(size))
    max_w = 0
    max_h = 0
    for size in sorted_sizes:
        max_w = max(max_w, size[0])
        max_h = max(max_h, size[1])
    return max_w * max_h