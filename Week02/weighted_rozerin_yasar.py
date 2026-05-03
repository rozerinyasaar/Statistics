def weighted_srs(data, n, weights, with_replacement):
    if with_replacement:
        return random.choices(data, weights=weights, k=n)
    else:
        result = []
        while len(result) < n:
            item = random.choices(data, weights=weights, k=1)[0]
            if item not in result:
                result.append(item)
        return result
