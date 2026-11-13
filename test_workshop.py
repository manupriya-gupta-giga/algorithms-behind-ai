import unittest
from workshop import Item, exact_knapsack, greedy_knapsack, shortest_hops, first_match


class WorkshopTests(unittest.TestCase):
    def test_greedy_counterexample(self):
        items = [Item("A", 6, 12), Item("B", 5, 9), Item("C", 5, 9)]
        self.assertEqual([i.name for i in greedy_knapsack(items, 10)], ["A"])
        self.assertEqual([i.name for i in exact_knapsack(items, 10)], ["B", "C"])
        self.assertEqual(sum(i.value for i in exact_knapsack(items, 11)), 21)

    def test_empty_and_no_fit(self):
        self.assertEqual(exact_knapsack([], 10), ())
        self.assertEqual(exact_knapsack([Item("A", 2, 7)], 0), ())
        self.assertEqual(greedy_knapsack([Item("A", 2, 7)], 1), ())

    def test_invalid_knapsack_inputs(self):
        for solver in (exact_knapsack, greedy_knapsack):
            for items, cap in [([Item("A", 0, 1)], 1), ([Item("A", 1, -1)], 1), ([], -1), ([], 1.5), ([Item("A", 1, 1), Item("A", 2, 2)], 3)]:
                with self.assertRaises(ValueError):
                    solver(items, cap)
        with self.assertRaises(ValueError):
            exact_knapsack([Item(str(i), 1, 1) for i in range(21)], 10)

    def test_minimum_hops_cycle_and_direction(self):
        graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["E"], "E": ["D"]}
        self.assertEqual(shortest_hops(graph, "A", "D"), ["A", "B", "D"])
        self.assertIsNone(shortest_hops(graph, "D", "A"))
        self.assertIsNone(shortest_hops(graph, "A", "missing"))
        self.assertEqual(shortest_hops(graph, "A", "A"), ["A"])

    def test_binary_search_boundaries(self):
        values = [10, 20, 20, 40]
        self.assertEqual(first_match(values, 20), 1)
        self.assertEqual(first_match(values, 10), 0)
        self.assertEqual(first_match(values, 40), 3)
        for target in (0, 30, 50):
            self.assertIsNone(first_match(values, target))
        self.assertIsNone(first_match([], 20))
        with self.assertRaises(ValueError):
            first_match([40, 10, 20], 20)


if __name__ == "__main__":
    unittest.main()
