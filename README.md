# COMP1117 1B — Tutorial Material

Teaching assistant materials for **COMP1117: Computer Programming** at the University of Hong Kong.
This repository holds all tutorial notebooks, example scripts, and supporting assets used in tutorial sessions.

---

## Course Overview

COMP1117 is an introductory Python programming course. Tutorials progress from basic syntax through data structures, recursion, and file I/O. Each session is delivered as a Jupyter notebook with embedded examples and exercises.

---

## Repository Structure

```
COMP1117/
├── Examples/          Standalone demos and module import examples
├── Tutorial1/         Python basics — variables, I/O, arithmetic
├── Tutorial2/         Type hints and function definitions
├── Tutorial3/         Conditionals (if / elif / else)
├── Tutorial4/         Loops and iteration
├── Tutorial5/         Functions and recursion
├── Tutorial6/         Data structures — lists, tuples, sets, dicts
├── Tutorial7/         String manipulation and Unix-style utilities
├── Tutorial8/         Recursive visualization with turtle graphics
├── Tutorial9/         File I/O — text, JSON, CSV
└── Tutorial10/        Built-in functions and advanced indexing
```

---

## Tutorial Breakdown

### Tutorial 1 — Python Basics
**Notebook:** `Tutorial1/T1.ipynb`

Introduces the Python environment and core syntax.
- Hello World, print statements, and variable assignment
- Basic arithmetic and string formatting
- Simple programs: triangle area, time conversion, distance calculation

**Scripts:** `distance.py`, `distance_2.py`, `time_conversion.py`, `repeat.py`, `file.py`

---

### Tutorial 2 — Type Hints & Functions
**Notebook:** `Tutorial2/T2.ipynb`

Covers how to write well-annotated Python functions.
- Function definition, parameters, and return values
- Python type hint syntax (`int`, `str`, `float`, `list`, etc.)
- Practical examples with complex numbers

**Scripts:** `hinting.py`, `complex_hinted.py`

---

### Tutorial 3 — Control Flow
**Notebook:** `Tutorial3/T3.ipynb`

Decision-making in Python.
- `if`, `elif`, `else` branches
- Comparison and logical operators
- Practical exercises on conditional logic

---

### Tutorial 4 — Loops
**Notebook:** `Tutorial4/T4.ipynb`

Iteration patterns in Python.
- `for` loops and `range()`
- `while` loops and loop control (`break`, `continue`)
- Nested loops and accumulator patterns

---

### Tutorial 5 — Functions & Recursion
**Notebook:** `Tutorial5/T5.ipynb`

Deep dive into functions and the call stack.
- Defining and calling functions
- Recursive thinking: base case vs. recursive case
- Classic examples: Fibonacci sequence, factorial
- Timing utility decorator

**Scripts:** `time_util.py`

---

### Tutorial 6 — Data Structures
**Notebook:** `Tutorial6/T6.ipynb`

Python's built-in collection types.
- Lists and list comprehensions
- Tuples and immutability
- Sets and set operations
- Dictionaries: creation, access, iteration

---

### Tutorial 7 — Strings & Unix Utilities
**Notebook:** `Tutorial7/T7.ipynb`  
**Supplementary notes:** `Tutorial7/Tutorial7_notes.pdf`

Working with text and simulating shell tools in Python.
- String methods: `split`, `join`, `strip`, `replace`, `find`, etc.
- Implementing Unix-like commands (`ls`, `mkdir`, `touch`, filter) in Python
- Refactored command dispatch with `process_command_unix` and custom `UnsupportedCommandException`
- One-liner vs. multi-line implementations with `&&` chaining

**Scripts:** `oneline_unix.py`, `mutiline_unix.py`, `time_util.py`

---

### Tutorial 8 — Recursive Visualization
**Notebook:** `Tutorial8/T8.ipynb`

Applying recursion to produce visual output with turtle graphics.
- Drawing recursive patterns and fractals
- Sierpinski triangle construction (`serpinski(length, level)`)
- Understanding recursion depth and base cases visually

**Scripts:** `triangle.py`

---

### Tutorial 9 — File I/O & Data Formats
**Notebook:** `Tutorial9/T9.ipynb`

Reading from and writing to persistent storage.
- Text file I/O (`open`, `read`, `write`, `with` statement)
- JSON parsing and serialization (`json` module)
- CSV reading and writing (`csv` module)
- Mutual recursion example: `sum_digit_utils.py`

**Sample data:** `data/comp1117.txt`, `data/config.json`, `data/username.csv`  
**Scripts:** `sum_digit_utils.py`

---

### Tutorial 10 — Built-ins & Indexing
**Notebook:** `Tutorial10/T10.ipynb`

Leveraging Python's standard library and advanced slicing.
- Commonly used built-in functions: `len`, `range`, `zip`, `enumerate`, `map`, `filter`, `sorted`
- List and string slicing with step values
- Practice problems and visual reference sheets

**Scripts:** `10_1.py`

---

## Examples

`Examples/` contains standalone scripts demonstrating module structure and imports:
- `cal.py` — calendar utilities (uses NumPy)
- `tools.py` — simple helper function showing how to import from a local module
- `ModuleA/` — example Python package layout

---

## How to Use

### Prerequisites
- Python 3.8+
- Jupyter Notebook or JupyterLab
- Dependencies: `numpy` (used in `Examples/cal.py`)

### Running a tutorial
```bash
cd Tutorial1
jupyter notebook T1.ipynb
```

Or launch JupyterLab from the repository root:
```bash
jupyter lab
```

### Running standalone scripts
```bash
python Tutorial5/time_util.py
python Tutorial8/triangle.py   # requires a display for turtle graphics
```

---

## Notes for Next Year's TA

- Each `T{n}.ipynb` notebook is self-contained and can be presented directly during tutorial sessions.
- The `assets/` subfolder in each tutorial holds images referenced inline in the notebook — keep them co-located.
- `Tutorial7/Tutorial7_notes.pdf` provides extra reference material for the string/Unix session; distribute or project as needed.
- `__pycache__/` folders are gitignored and safe to delete before sharing with students.
- Root-level `multiline_unix.py`, `oneline_unix.py`, and `triangles.py` mirror the final versions in their respective tutorial folders and are kept here for convenience.
- Consider adding `requirements.txt` if more third-party packages are introduced in future years.

---

## Contributors

- **Yang Haozhe (Thomas)** — Teaching Assistant, COMP1117 2025 Fall
- **Claude Code** (Anthropic) — Documentation and code cleanup
