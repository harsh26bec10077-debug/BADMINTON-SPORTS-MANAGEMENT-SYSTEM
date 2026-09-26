# Badminton Sports Management System

## About the Project

The Badminton Sports Management System is a simple Python-based project made for managing badminton players and matches.

The main purpose of this project is to make basic badminton management easier by storing player information, scheduling matches, recording match results and keeping track of player statistics.

This project was developed as part of the **Introduction to Problem Solving and Programming** course.

## Features

### 1. Player Management

The Player Management section allows the user to:

* Add a new player
* Store player details
* Display all registered players
* Search for a player using Player ID
* Keep track of matches played, wins and losses

The player details stored by the program include:

* Player ID
* Player Name
* Gender
* Department/Branch
* Matches Played
* Wins
* Losses

### 2. Match Management

The Match Management section allows the user to:

* Schedule a new match
* Display all scheduled matches
* Record match results
* Search for a match
* Cancel a scheduled match

Each match contains information such as:

* Match ID
* Player 1
* Player 2
* Match Date
* Match Time
* Match Status
* Game Scores
* Winner

### 3. Best of 3 Match System

The match result is recorded using a best-of-3 game format.

* Scores for Game 1 are entered first.
* Scores for Game 2 are entered next.
* If both players have won one game each, Game 3 is played.
* The player who wins more games is declared the winner.

After the result is recorded, the player's match statistics are updated.

## Technologies Used

* **Programming Language:** Python
* **Data Structures:** Dictionary and List
* **Development Environment:** Python IDLE / VS Code
* **Version Control:** Git and GitHub

## Project Structure

```text
Badminton-Sports-Management-System/
│
├── badminton_sports_management.py
└── README.md
```

## How the Program Works

When the program starts, the main menu is displayed.

```text
======================================
     BADMINTON SPORTS MANAGEMENT
======================================
1. Player Management
2. Match Management
3. Exit
```

The user can select either Player Management or Match Management.

### Player Management Menu

```text
===== PLAYER MANAGEMENT =====
1. Add Player
2. Display Players
3. Search Player
4. Back to Main Menu
```

### Match Management Menu

```text
===== MATCH MANAGEMENT =====
1. Schedule Match
2. Display All Matches
3. Record Match Result
4. Search Match
5. Cancel Match
6. Back to Main Menu
```

## Data Storage

The project uses Python dictionaries and lists to store information while the program is running.

A dictionary named `players` stores player information.

```python
players = {}
```

A list named `matches` stores match information.

```python
matches = []
```

A match counter is also used to give each scheduled match a unique Match ID.

```python
match_counter = 1
```

## Example

Suppose two players are registered:

```text
Player 1: Rahul
Player 2: Aman
```

A match can then be scheduled between them.

For example:

```text
Match ID: 1
Player 1: Rahul
Player 2: Aman
Date: 25-09-2026
Time: 5:00 PM
Status: scheduled
```

After the match, the scores can be entered for each game.

```text
Game 1: 21 - 18
Game 2: 17 - 21
Game 3: 21 - 16
```

The program then determines the winner based on the number of games won and updates the player statistics.

## Advantages

* Simple and easy to use
* Easy to understand for beginners
* Uses basic Python concepts
* Reduces the need to maintain match details manually
* Keeps player and match information organized
* Demonstrates the use of functions, lists, dictionaries, loops and conditional statements

## Limitations

* Data is stored only while the program is running.
* There is no database connection.
* The program currently works through the command line.
* There is no graphical user interface.
* Player and match information is not saved permanently in a file.

## Future Scope

The project can be improved in the future by adding:

* Permanent data storage using files or a database
* A graphical user interface
* Player ranking system
* Tournament management
* More detailed match statistics
* Login system for administrators
* Automatic report generation

## Concepts Used

This project helped in understanding and applying basic Python programming concepts such as:

* Variables
* Input and output
* Dictionaries
* Lists
* Functions
* `if-else` statements
* `for` loops
* `while` loops
* Searching
* Basic data management

## Conclusion

The Badminton Sports Management System is a basic Python project designed to manage badminton players and matches.

The project demonstrates how programming concepts can be used to solve a simple real-world management problem. It also provides practice with functions, dictionaries, lists, loops and conditional statements.

## Author

**Name:** Harsh Pal
**Course:** Introduction to Problem Solving and Programming
**Branch:** Electronics and Communication Engineering
**University:** VIT Bhopal University
