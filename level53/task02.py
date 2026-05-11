def linear_search(items, target):
    for item in items:
        if item == target:
            return True
    return False