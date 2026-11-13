# Algorithms behind AI

**From a knapsack to a real-world system**  
Manupriya Gupta, Forward Deployed Engineer at Giga

Why do algorithms still matter when AI can write code? Using the knapsack problem and everyday examples, we connect classroom ideas to real software. Compare algorithmic solutions with plausible suggestions, test assumptions and edge cases, and see why fundamentals help us catch convincing but incorrect answers. No prior AI background is needed. Basic Python is helpful.

Prepared for Professor Gurman Gill's Sonoma State algorithms class. All problems and data are synthetic. This is an independent teaching resource, not a university-sponsored project or a solution to a graded assignment.

## Start here

Python 3.10 or newer is sufficient. There are no third-party packages, API keys, paid AI accounts, or credit requirements.

```sh
git clone https://github.com/manupriya-gupta-giga/algorithms-behind-ai.git
cd algorithms-behind-ai
python3 workshop.py
python3 -m unittest -v
```

Without Git, use **Code > Download ZIP**, extract it, and run the same Python commands from that folder. The examples use tiny inputs and run locally.

For an optional browser notebook: [Open in Google Colab](https://colab.research.google.com/github/manupriya-gupta-giga/algorithms-behind-ai/blob/main/workshop.ipynb). Run the cells in order. A Google sign-in may be required; no paid tier or model API is needed. Local Python is the fallback. Hosted Colab execution has not been independently verified.

## The story

| Example | Everyday question | What can go wrong? |
| --- | --- | --- |
| 0/1 knapsack | Which independent projects fit a fixed budget? | A tempting greedy choice misses the best combination. |
| Unweighted shortest path | Which route needs the fewest hops? | Fewest hops does not mean fastest travel time. |
| Binary search | Where is a threshold in sorted data? | The method depends on an ordering assumption. |

The code does not call an AI model. The audit claims in the exercises are deliberately constructed teaching examples, not transcripts or measured model behavior. AI-assisted code should be checked against explicit requirements and independently known answers.

- [Exercises and expected results](EXERCISES.md)
- [Instructor guide and 60-minute outline](INSTRUCTOR_NOTES.md)
- [Runnable algorithms](workshop.py)
- [Tests](test_workshop.py)

## Scope and limits

Knapsack here means each item can be chosen at most once, weights and capacity are positive/nonnegative integers, values are nonnegative integers, and items have no dependencies. The exhaustive reference solver is restricted to 20 items because its work grows exponentially. BFS solves minimum-hop paths on a directed, unweighted adjacency list. Binary search returns the first matching position in sorted numeric data; its wrapper validates the ordering, making the overall wrapper O(n), even though its search step is O(log n).

These are teaching models, not production trading systems, investment guidance, or claims about employer implementations. No private employer, customer, or student data is included.

Python references: [itertools combinations](https://docs.python.org/3/library/itertools.html#itertools.combinations), [deque](https://docs.python.org/3/library/collections.html#collections.deque), [bisect](https://docs.python.org/3/library/bisect.html).
