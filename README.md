# Py_Projects

🚦 Smart Traffic Management Simulation
----
<img width="452" height="338" alt="image" src="https://github.com/user-attachments/assets/19268de8-a378-4c38-8fa1-5761cf5db294" />


Today, I completed my first practical AI project: a **Smart Traffic Management Simulation** using Python and Pygame.

While studying Intelligent Agents, I wanted to understand how an agent perceives its environment, makes decisions, and takes actions in a practical scenario.

### 🔍 What I Built
- A 2D four-way traffic intersection simulation.
- Random vehicle generation and movement.
- Simulated sensors to count vehicles on each road.
- A rule-based agent to identify the busiest road.
- Traffic signal updates based on the agent's decision.

### 🧠 AI Concepts Applied
- Intelligent Agents
- Agent–Environment Interaction
- Sensors and Actuators
- PEAS Representation
- Rule-Based Decision Making
- Rational Agent Concepts

### 💻 What I Learned
This project helped me understand that an AI agent does not always need Machine Learning to make decisions.

A rule-based agent can make decisions using predefined conditions and logic.

I also learned how Python concepts such as lists, dictionaries, functions, loops, and conditional statements can be combined to implement an agent's decision-making process.

**My biggest takeaway:** Reading AI theory helps us understand the concepts, but implementing them helps us understand how they actually work.

This is a basic educational simulation, not a real-world traffic control system. It is just the beginning of my journey into practical AI.

Looking forward to exploring more AI concepts and building the next project!

#ArtificialIntelligence #Python #Pygame #IntelligentAgents #AIProjects #LearningByBuilding #ComputerScience








<img width="554" height="353" alt="image" src="https://github.com/user-attachments/assets/07940b42-795b-4bab-bccc-376d0626082d" />


###project2: Path_Finding ALgorithm implementation
# AI Search Algorithm Visualizer

An interactive AI Search Algorithm Visualizer built with **Python and Pygame**. This project demonstrates how different uninformed and informed search algorithms explore a graph, visit nodes, and find a path from the Start Node to the Goal Node.

## Project Overview

The visualizer uses a Bubble Tree structure to demonstrate search algorithms through animation.

Each node changes color based on its current search state, making it easier to understand how different algorithms work.

## Search Algorithms Implemented

### Uninformed Search
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Uniform-Cost Search (UCS)
- Depth-Limited Search (DLS)
- Iterative Deepening DFS (IDDFS)
- Bidirectional Search

### Informed Search
- Greedy Best-First Search
- A* Search
- Iterative Deepening A* (IDA*)
- Beam Search
- Recursive Best-First Search (RBFS)

## Visualization Features

- Animated Bubble Tree
- Start and Goal Node representation
- Visited Node visualization
- Frontier visualization
- Final path highlighting
- Edge cost and heuristic values
- Algorithm selection using keyboard shortcuts
- Pause, resume, and restart controls

## Color Representation

| Color | Meaning |
|---|---|
| 🔴 Red | Current Node |
| 🔵 Blue | Visited Node |
| 🟠 Orange | Frontier Node |
| 🟢 Green | Final Path |
| Gray | Unvisited Node |

## Controls

| Key | Action |
|---|---|
| 1 | BFS |
| 2 | DFS |
| 3 | UCS |
| 4 | DLS |
| 5 | IDDFS |
| 6 | Bidirectional Search |
| 7 | Greedy Best-First |
| 8 | A* Search |
| 9 | IDA* |
| 0 | Beam Search |
| H | RBFS |
| SPACE | Pause / Resume |
| R | Restart |
| ESC | Exit |

## Technologies Used

- Python
- Pygame
- Collections (Queue and Deque)
- Heapq (Priority Queue)

## What I Learned

Through this project, I learned:

- How graph-based search algorithms work.
- The difference between uninformed and informed search.
- How Queue, Stack, and Priority Queue affect search behavior.
- How pathfinding algorithms use parent tracking.
- How path cost and heuristic values guide search decisions.
- How to visualize AI algorithms using Pygame.



## Learning Outcome

This project helped me understand the internal working of classical AI search algorithms through visual simulation rather than only studying their theoretical concepts.

---

**Project:** AI Search Algorithm Visualizer  
**Language:** Python  
**Visualization:** Pygame



###
<img width="607" height="739" alt="image" src="https://github.com/user-attachments/assets/f6fb9a63-519c-497b-aca0-0b29b20d46a8" />
<img width="619" height="736" alt="image" src="https://github.com/user-attachments/assets/8c9f0667-98bb-4a49-b9b9-9b72b6e5b995" />


# 🎮 Intelligent Tic-Tac-Toe AI

An AI-powered Tic-Tac-Toe game built with **Python** and **Pygame**, where a human player competes against an intelligent AI agent using the **Minimax Algorithm**.

## 🚀 Project Overview

This project demonstrates how Artificial Intelligence can make decisions by exploring possible future game states.

Unlike a random AI, the Minimax-based agent evaluates possible moves and selects the best available move to maximize its chance of winning.

## ✨ Features

- Human vs AI gameplay
- Intelligent AI using Minimax Algorithm
- AI blocks the player's winning moves
- AI finds its own winning opportunities
- Winner and draw detection
- Restart game using `R`
- Exit game using `ESC`
- Interactive Pygame interface

## 🧠 AI Algorithm: Minimax

Minimax is a decision-making algorithm used in two-player, turn-based games.

The algorithm explores possible future moves and chooses the optimal move.

### Scoring System

| Game Outcome | Score |
|---|---:|
| AI Wins | +1 |
| Draw | 0 |
| Human Wins | -1 |

- **MAX Player:** AI (`O`) tries to maximize the score.
- **MIN Player:** Human (`X`) tries to minimize the score.

The AI evaluates possible game states recursively before selecting its move.

## 🛠️ Technologies Used

- Python
- Pygame
- Minimax Algorithm
- Recursion
- Game Tree Search

## 🎮 Controls

| Control | Action |
|---|---|
| Mouse Click | Place X |
| R | Restart Game |
| ESC | Exit Game |



## 📚 What I Learned

Through this project, I learned:

- How Minimax works in a two-player game
- MAX and MIN decision-making
- Recursive game-tree exploration
- Evaluating possible future states
- Implementing an intelligent game agent
- Integrating AI logic with a Pygame interface

## 🔮 Future Improvements

- Alpha-Beta Pruning
- Difficulty levels
- Game score tracking
- Improved UI and animations

---

**Project 03 — AI Project Series**

*Building intelligent agents through Python and Artificial Intelligence.*
