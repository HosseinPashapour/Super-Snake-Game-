# Super Snake Game 🐍
### Machine Learning


## Overview
Creating a snake game using Python and **Arcade** library in which the snake goes for the apple by itself (without user involvement).  
In the meantime data is being collected and later used to construct an Artificial Neural Network model with the help of **TensorFlow** package.  
Then the trained model will be used to guide the snake to its food.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Gameplay](#gameplay)
- [Model](#ModelPerformance)


## Features

- Control the snake to eat food and grow.
- Machine learning model predicts the snake's movement direction based on the state of the game.
- Real-time collision detection with walls and food.
- Score tracking.

## Technologies Used

- Python 3.11.7
- Arcade (for game development)
- Keras (for machine learning model)
- Pandas (for data manipulation)
- NumPy (for numerical operations)

## Installation

To get started with the Super Snake game, follow these steps:

1.Clone this repository:

```bash
git clone https://github.com/HosseinPashapour/Super-Snake-Game-.git
cd super-snake
```

2.Install the required packages:

```bash
pip install arcade keras pandas numpy
```

3.Download or create the model:

- Ensure you have a trained model saved as `Snake_Model.h5` in the `Output` directory.
- You can train your model using the provided dataset (`Snake_Dataset.csv`).

## Usage

To run the ai game, execute the following command:

```bash
python Collect_Dataset.py
```

after the program closed run this command:

```bash
python train.py
```

after you seen the plot run this command:

```bash
python main_ai.py
```

or just run one of this program:

```bash
python main_keyboard.py
```

## How to install

```
pip install -r requirements.txt
```


The game window will open, and you can start playing or just chill and watch!

## Gameplay

- Use the arrow keys to control the direction of the snake.
- The objective is to eat the food (represented as meat) to score points and grow the snake.
- The game ends if the snake collides with the walls or itself.


## Results

## Snak_Manul


<img src="Output\Snak_manul.png" width="550">

## Snak_AI

<img src="Output\Snak_AI.png" width="550">




## Model Performance
<img src="Output\Train.png" width="550">




Here is a report of the model's performance:

|        | Accuracy | Loss |
| ---------- | ---- | ---
| Train      | 0.8989999890327454 | 0.24742895364761353


