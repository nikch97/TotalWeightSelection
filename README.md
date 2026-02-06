# Project Selection Using Max-Flow / Min-Cut

This project solves a **project selection problem with precedence constraints** using a **maximum flow / minimum cut** approach. Each project has a profit or cost, and some projects depend on others.

---

## What the Program Does

- Represents projects as nodes in a flow network.
- Assigns profits (positive weights) and costs (negative weights).
- Enforces project dependencies using infinite-capacity edges.
- Computes the **maximum achievable total weight** using max-flow.
- Visualizes the flow network using NetworkX and Matplotlib.

---

## Requirements

```bash
pip install PyMaxFlow networkx matplotlib
````

(Use `!pip install PyMaxFlow` in Google Colab.)

---

## How to Run

```bash
python main.py
```

The input is defined directly in the code.

---

## Output

* Prints the maximum total profit.
* Displays a graph showing the flow network and capacities.

---

## Notes

* Positive project weights represent profits.
* Negative weights represent costs.
* Precedence constraints ensure dependent projects are selected together.

---

## Libraries Used

* PyMaxFlow
* NetworkX
* Matplotlib


