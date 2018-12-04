import numpy as np
import matplotlib.pyplot as plt
from collection import namedtuple


Node = namedtuple ('Node', ('feature', 'value', 'impurity', 'left', 'right'))
Leaf = namedtuple ('Leaf', ('value', 'x', 'y'))

def build_tree(x, y, depth, max_depth = np.inf):
    if depth == max_depth or criteria(y) < 1e-4:
        return Leaf(np.round(np.mean(y)), x, y)
    feature, value, impurity = find_best_split(x, y)
    (x_left, y_left), (x_right, y_right) = partition(x, y, feature, value)
    left = build_tree(x_left, y_left, depth+1, max_depth)
    right = build_tree(x_right, y_right, depth+1, max_depth)
    root = Node((feature, value, impurity, left, right))
    return root

def find_best_split(x, y):
    
    return best_feature, best_value, best_impurity

def criteria(y):
    p = np.sum(y) / y.size #потому что делим 0 и 1
    return p * (1 - p)

def impurity(y_left, y_right):
    size = y_left.size + y_right.size
    h = (y_left.size * criteria(y_left) + y_right.size * criteria(y_right)) / size
    return h

def main():
     build_tree(x, y, 0, 100)

if __name__ == '__main__':
    main()