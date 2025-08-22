# Dots and Boxes AI Agent

A reinforcement learning implementation of the classic Dots and Boxes game using Q-learning.

## Project Overview

This project implements an AI agent that learns to play Dots and Boxes through reinforcement learning. The agent uses Q-learning to develop strategies and improve its gameplay over time.

## Features

- Human vs AI gameplay
- Q-learning implementation with epsilon-greedy exploration
- Visual interface using Pygame
- Training mode for self-play learning
- Learning progress tracking

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/DotsAndBoxesAI.git
2. Install dependencies:
pip install -r requirements.txt

Usage
Play Against AI
python src/main.py

Train AI (Self-Play)
python src/train_mode.py

## Project Structure
src/ - Source code files
docs/ - Project documentation and report
resources/ - Screenshots and demo materials

## Technical Details
Algorithm: Q-learning with state representation based on board configuration
State Representation: Flattened board lines + score difference + boxes with 3 sides
Learning Parameters:
  Learning rate (α): 0.7
  Discount factor (γ): 0.95
  Exploration rate (ε): Starts at 0.3, decays over time

## Results
The AI agent demonstrates improved performance over time, learning strategies to:
  Complete boxes when opportunities arise
  Avoid setting up opportunities for the opponent
  Maximize its score through strategic moves

## Documentation
Comprehensive project documentation is available in the docs/ folder, including:
  Problem statement and background
  Agent classification and analysis
  Use case diagrams and descriptions
  Class and sequence diagrams
  Implementation details

## Future Enhancements
  Implement deep Q-learning for larger grid sizes
  Add different difficulty levels
  Implement multiplayer functionality
  Create a web-based version

## Author
Buys Enock Onkarabile - University of Johannesburg

## Additional Files to Create

1. **requirements.txt**:
pygame==2.1.2

2. **.gitignore**:
pycache/
.pyc
q_table_.pkl
learning_progress.txt

