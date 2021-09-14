def print_evaluation(x, y):
    print("({}, {}) = {:.2f}".format(x, y, evaluate_pair(x, y)))


def evaluate_pair(x, y):
    return ((3 * x * x) * x - 16) / (y - 1)


print_evaluation(2, 5)
print_evaluation(2, 6)
print_evaluation(2, 7)
print_evaluation(3, 5)
print_evaluation(3, 6)
print_evaluation(3, 7)
print_evaluation(4, 5)
print_evaluation(4, 6)
print_evaluation(4, 7)
