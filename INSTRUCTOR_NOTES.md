# Instructor guide

Audience: algorithms students with no assumed AI background. Basic Python is useful, but prediction and discussion can be done without a computer.

## Suggested 60 minutes

| Minutes | Activity |
| --- | --- |
| 0-5 | Introduce AI-assisted coding as a source of suggestions that need checking; introduce objectives and assumptions. |
| 5-7 | Personal context: Manupriya's 2.5 years building high-frequency trading systems at Goldman Sachs, then Forward Deployed Engineering at Giga. Keep examples public and conceptual. No employer code, customers, strategies, performance claims, or confidential architecture. |
| 7-27 | Knapsack: predict greedy, enumerate tiny combinations, find the counterexample, change the budget. |
| 27-37 | BFS: minimum hops versus minimum travel time; discuss cycles and unreachable goals. |
| 37-45 | Binary search: ordering, duplicates, and preprocessing costs. |
| 45-55 | Pairs audit a synthetic claim, propose a test, and explain the violated assumption. Optional AI use only if independently available and allowed by class policy. |
| 55-60 | Questions and the review checklist. |

## Setup and fallback

Send the README and exercises ahead of class. Run `python3 workshop.py` and `python3 -m unittest -v`. Students can use local Python or the optional notebook. The notebook contains the same algorithm definitions and does not need imports from this repository. If a student cannot execute code, share the terminal results and use the paper exercises. No paid AI access is needed. API credits are undecided and no sponsorship is implied.

## Teaching boundaries

- Use synthetic examples only. Do not upload Gurman's graded assignment or private student material to an AI service.
- The exhaustive knapsack solver is a tiny-instance reference, not a production recommendation. Discuss dynamic programming as an extension: for integer capacity W, a conventional table takes O(nW) time, which is pseudo-polynomial, not polynomial in the bit length of W.
- BFS runs in O(V+E) for reachable vertices and edges when neighbor iteration is linear. It does not minimize arbitrary edge weights.
- Binary search's sorted-input check deliberately makes this wrapper O(n). Explain how validating once changes the cost of repeated lookups.
- Suggested AI claims are constructed prompts for discussion, not results of a model evaluation.
- Do not promise that passing tests proves correctness. Ask students to state the precise claim each test supports.

## Logistics still to confirm with organizer

Meeting notes indicate November 19, 11 AM-noon over Zoom. The organizer needs to confirm the timezone and send the class invitation. Do not infer the class meeting URL from the earlier planning-call room.
