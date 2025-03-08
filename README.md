# Graph Theory Connectivity Checker

This project is a Graph Theory Connectivity Checker that visualizes and checks the connectivity of graphs using BFS (Breadth-First Search) and DFS (Depth-First Search) algorithms. The application is built using CustomTkinter for the GUI and Graphviz for graph visualization.

## Features

- Visualize graphs and their connectivity
- Supports both BFS and DFS algorithms
- Load and save graphs from/to JSON files
- Step-by-step visualization of graph traversal
- Cross-platform support with CustomTkinter

## Installation

### Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)

### Steps

1. Clone the repository:

      ```bash
      git clone https://github.com/yourusername/graph-theory-connectivity-checker.git
      cd graph-theory-connectivity-checker
      ```

2. Create and activate a virtual environment:

      ```bash
      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`
      ```

3. Install the required packages:
      ```bash
      pip install -r requirements.txt
      ```

## Usage

1. Activate the virtual environment if not already activated:

      ```bash
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`
      ```

2. Run the application:
      ```bash
      python src/main/GUI/main_gui.py
      ```

## Project Structure

```
graph-theory-connectivity-checker/
│
├── src/
│   ├── main/
│   │   ├── GUI/
│   │   │   └── main_gui.py
│   │   ├── graph_undirected.py
│   │   └── main.py
│   └── ...
├── venv/
│   └── ...
├── requirements.txt
└── readme.md
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## TODO

- [ ] Add support for directed graphs
- [ ] Improve graph visualization options
- [ ] Add more graph algorithms
- [ ] Write unit tests

## Acknowledgements

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Graphviz](https://graphviz.org/)
- [Pillow](https://python-pillow.org/)
