# **Flappy Bird AI Project**

## Kutaisi International University

**Project Title:** Flappy Bird AI Project

**Students:** Luka Gogiashvili, Davit Mamrikishvili, Luka Gvanceladze, Saba Katamadze

**Subject:** INTRODUCTION TO ML&AI

# Flappy Bird AI Project

This project demonstrates the use of Machine Learning and AI to play the Flappy Bird game using the NEAT (NeuroEvolution of Augmenting Topologies) algorithm.
The AI controls the bird, learns how to play the game, and improves its performance over time.

## Project Structure

```
flappy-bird-ai/
├── config.txt
├── game/
│   ├── base.py
│   ├── bird.py
│   ├── constants.py
│   ├── main.py
│   ├── pipe.py
│   └── util.py
├── static/
│   ├── fonts/
│   └── imgs/
├── requirements.txt
└── README.md
```

### config.txt

Contains the configuration settings for the NEAT algorithm. Some key configurations include:

- **Population size:** 20 Default
- **Fitness criterion:** Maximize
- **Node and connection mutation rates:** Various rates to control the evolution of the neural network.

### game/

Contains the main game logic and classes:

- **base.py:** Contains the `Base` class to handle the floor movement.
- **bird.py:** Contains the `Bird` class representing the Flappy Bird.
- **constants.py:** Contains constants and utility functions for the game.
- **main.py:** The main entry point to run the game.
- **pipe.py:** Contains the `Pipe` class to handle pipe obstacles.
- **util.py:** Contains utility functions for the game.

### static/

Contains the static resources for the game:

- **fonts/**: Directory for font files used in the game.
- **imgs/**: Directory for image files used in the game.

## Installation

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

To run the game with AI, execute the `main.py` file:

```bash
python game/main.py
```

The AI will start learning to play the game using the NEAT algorithm. You can observe how the bird improves its performance over time.

## Game Files Description

### base.py

Handles the floor/base movement in the game.

### bird.py

Represents the Flappy Bird, including its movement, jumping, and collision detection.

### constants.py

Defines various constants and utility functions used across the game, such as window dimensions, fonts, and image loading.

### main.py

The entry point for the game. It initializes the game environment and runs the NEAT algorithm.

### pipe.py

Manages the pipe obstacles in the game, including their movement and collision detection.

### util.py

Contains utility functions, such as displaying rotated images.

## Configuration (config.txt)

Defines the settings for the NEAT algorithm, such as population size, mutation rates, and node configurations.

## Requirements

- Python 3.x
- `pygame`
- `neat-python`

Install the dependencies using:

```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the Kutaisi International University license. All rights reserved.

---

## Acknowledgements

- The NEAT Python implementation: [neat-python](https://neat-python.readthedocs.io/en/latest/)
- Flappy Bird game assets and inspiration.
