import itertools
def permutations(string):
    final_list = []
    for perm in list(itertools.permutations(string)):
        final_list.append("".join(perm))
    return list(set(final_list))

print(permutations("aabb"))