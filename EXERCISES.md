# Predict, run, challenge

Each claim below is synthetic, written for this workshop. None is attributed to a real model. Try predicting before opening the answer section.

## 1. A budget and three projects

Budget: 10 units. A costs 6 and provides value 12; B costs 5 and provides value 9; C costs 5 and provides value 9. Each can be selected once.

**Claim to audit:** "Always take the highest value per unit of cost first. This gives the best possible selection."

1. Calculate each value/cost ratio. What does greedy select?
2. List every feasible combination. Can you beat greedy?
3. Change capacity to 11. Does greedy now match the best result? Does that prove it always works?
4. Add a project with cost 0. Why does this teaching model reject it?
5. Discuss: what changes if partial projects are allowed, or B depends on A? Those are different problem definitions.

## 2. A route with fewer hops

Edges: Home -> Library -> Campus; Home -> Cafe -> Park -> Campus.

**Claim to audit:** "BFS gives the fastest route because it finds a shortest path."

1. Predict the BFS route and count its edges.
2. Suppose both Library-route edges take 10 minutes, while each Cafe-route edge takes 1 minute. Which route is faster?
3. Try an unreachable goal, a cycle, and start equal to goal.
4. Explain what input is missing and why weighted shortest-path methods require a different treatment. Do not simply label BFS wrong: identify the objective it actually solves.

## 3. A threshold lookup

Search for 20 in [10, 20, 20, 40].

**Claim to audit:** "Binary search can search any list in O(log n), so sorting and validation do not matter."

1. Predict the first matching zero-based index.
2. Try an absent value and an empty list.
3. Try [40, 10, 20]. Why reject it?
4. Separate the search step's cost from preprocessing and validation. If you repeatedly search an unchanged dataset, where should validation live?

## A reusable review habit

Before accepting suggested code, write down: inputs, objective, assumptions, one independently calculated answer, a counterexample, and a scale limit. Ask whether tests check the requirement or merely agree with the implementation. Passing these examples is evidence about these examples, not proof of universal correctness.

<details><summary>Expected results and discussion</summary>

- Knapsack at capacity 10: ratios A=2, B=C=1.8. Greedy selects A, value 12. Exact selection B+C costs 10, value 18. At capacity 11, A+B or A+C yields 21 and greedy is optimal on this input. One successful case does not prove a heuristic.
- BFS returns Home, Library, Campus, two edges. With the hypothetical times, that route costs 20 minutes; the three-edge Cafe route costs 3. Unreachable returns None; same start/goal returns a one-node path. Cycles terminate because visited nodes are tracked.
- Binary search returns index 1; absent and empty return None. Unsorted data raises ValueError. This wrapper's validation is O(n). Only the bisect search step is O(log n). Sorting first changes indices and has a separate cost.

</details>
