def find_subsets(s):
    if not s:
        return [set()]
    elem = s.pop()
    subsets_without_elem = find_subsets(s)
    s.add(elem)
    subsets_with_elem = [subset | {elem} for subset in subsets_without_elem]
    return subsets_without_elem + subsets_with_elem

s = {1, 2, 3}
all_subsets = find_subsets(s)
for subset in all_subsets:
    print(subset)