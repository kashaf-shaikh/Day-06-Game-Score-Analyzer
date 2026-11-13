# Day 06 - Game Score Analyzer

This is my Day 6 project from Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp.

In this project, I created a Game Score Analyzer using Python. The program asks for the player's name and scores in different subjects. It then calculates the total score, average score and highest score. At the end, it shows a performance message based on the average.

## About the Project

The program takes the following information from the user:

- Player's name
- Number of subjects
- Score in each subject

After collecting the scores, it generates a report containing:

- All the entered scores
- Total score
- Average score
- Highest score
- Performance message

## Performance Levels

| Average Score | Performance |
|---|---|
| 90 or above | Excellent! |
| 70 or above | Good |
| 50 or above | Average |
| Below 50 | Needs Improvement |

## Example

**Input:**

```text
Enter your name:
Kashaf

How many subjects do you have?
5

Enter your score in each subject:
95
85
78
90
82
```

**Output:**

```text
============ Game Score Analyzer ===========

Player: Kashaf
Score: [95, 85, 78, 90, 82]
Total Score: 430
Average Score: 86.0
Highest Score: 95
Performance: good
```

*The output will change depending on the scores entered by the user.*

## Functions Used

| Function | Purpose |
|---|---|
| `calculate_total()` | Calculates the sum of all scores. |
| `calculate_average()` | Calculates the average score. |
| `find_highest_score()` | Finds the highest score. |
| `get_performance()` | Returns a performance message based on the average. |

## What I Learned

While making this project, I learned:

- Creating and using functions.
- Passing arguments to functions.
- Returning values using `return`.
- Working with lists.
- Adding items to a list using `append()`.
- Using `for` loops to collect scores.
- Calculating total and average values.
- Finding the highest value from a list.
- Using conditional statements.
- Using type hints in function parameters.
- Breaking a program into smaller functions.

## Technologies Used

- Python 3
- PyCharm
- Git
- GitHub

## How to Run

1. Clone or download this repository.
2. Open the project folder in PyCharm or any Python editor.
3. Open the `main.py` file.
4. Run the program.
5. Enter your name and scores.
6. Check the final performance report.

You can also run it using the terminal:

```bash
python main.py
```

## Project Structure

```text
Day-06-Game-Score-Analyzer/
│
├── main.py
│
└── README.md
```

## About My Learning

This is my sixth project in the 100 Days of Python course. In this project, I got to practise functions and lists together. I also learned how to divide a program into smaller functions to make the code easier to manage.

I will continue adding my daily projects to GitHub as I learn new Python concepts.