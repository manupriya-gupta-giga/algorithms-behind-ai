"""Small, synthetic algorithm examples. Python 3.10+, standard library only."""
from bisect import bisect_left
from collections import deque
from dataclasses import dataclass
from itertools import combinations


@dataclass(frozen=True)
class Item:
    name: str
    weight: int
    value: int


def validate_items(items, capacity):
    if type(capacity) is not int or capacity < 0:
        raise ValueError("capacity must be a nonnegative integer")
    if len({i.name for i in items}) != len(items):
        raise ValueError("item names must be unique")
    for i in items:
        if type(i.weight) is not int or i.weight <= 0:
            raise ValueError("item weights must be positive integers")
        if type(i.value) is not int or i.value < 0:
            raise ValueError("item values must be nonnegative integers")


def greedy_knapsack(items, capacity):
    """Value/weight heuristic. Not a correct general 0/1 knapsack solver."""
    items = tuple(items)
    validate_items(items, capacity)
    selected = []
    remaining = capacity
    for item in sorted(items, key=lambda i: i.value / i.weight, reverse=True):
        if item.weight <= remaining:
            selected.append(item)
            remaining -= item.weight
    return tuple(selected)


def exact_knapsack(items, capacity):
    """Exhaustive tiny-instance reference, O(n * 2**n). First best tie wins."""
    items = tuple(items)
    validate_items(items, capacity)
    if len(items) > 20:
        raise ValueError("reference solver supports at most 20 items")
    best, best_value = (), 0
    for count in range(len(items) + 1):
        for candidate in combinations(items, count):
            if sum(i.weight for i in candidate) <= capacity:
                value = sum(i.value for i in candidate)
                if value > best_value:
                    best, best_value = candidate, value
    return best


def shortest_hops(graph, start, goal):
    """Return a minimum-edge path, or None. Nodes must be hashable.

    Adjacency lists describe outgoing edges; neighbors need not be keys.
    Equal-length ties follow adjacency order. Weights are not supported.
    """
    queue = deque([start])
    parent = {start: None}
    while queue:
        node = queue.popleft()
        if node == goal:
            path = [node]
            while node != start:
                node = parent[node]
                path.append(node)
            return list(reversed(path))
        for neighbor in graph.get(node, ()):
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
    return None


def first_match(sorted_values, target):
    """First matching index or None. Sorted-data validation costs O(n)."""
    if any(a > b for a, b in zip(sorted_values, sorted_values[1:])):
        raise ValueError("binary search requires ascending sorted data")
    index = bisect_left(sorted_values, target)
    if index < len(sorted_values) and sorted_values[index] == target:
        return index
    return None


def main():
    items = [Item("A", 6, 12), Item("B", 5, 9), Item("C", 5, 9)]
    print("1. Fixed budget: capacity 10; A=(6,12), B=(5,9), C=(5,9)")
    for label, solver in [("Greedy heuristic", greedy_knapsack), ("Exact reference", exact_knapsack)]:
        chosen = solver(items, 10)
        print(f"   {label}: {[i.name for i in chosen]}, value {sum(i.value for i in chosen)}")
    graph = {"Home": ["Library", "Cafe"], "Library": ["Campus"], "Cafe": ["Park"], "Park": ["Campus"]}
    print("2. Fewest hops:", shortest_hops(graph, "Home", "Campus"))
    print("   Edge travel times are absent, so this does not establish fastest travel.")
    print("3. First 20 in [10,20,20,40]:", first_match([10, 20, 20, 40], 20))
    print("   Zero-based index. Try unsorted input and observe the rejected assumption.")
    print("Next: predict, run, change one input, and explain a failure in EXERCISES.md.")


if __name__ == "__main__":
    main()
