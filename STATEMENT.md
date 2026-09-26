# Badminton Sports Management System

## Project Statement

The **Badminton Sports Management System** is a simple Python-based console application developed to manage badminton players and their matches.

The main purpose of this project is to make basic player and match management easier by keeping all the information organized in one program. The system allows the user to register players, view and search player details, schedule matches between players, record match results, and search for match information.

The project uses basic Python concepts such as **functions, dictionaries, lists, loops, conditional statements, user input, and menu-driven programming**.

## Problem Statement

Managing player details and match information manually can become difficult when there are multiple players and matches. Important information such as player details, match schedules, scores, winners, and player statistics needs to be maintained properly.

This project provides a simple solution by creating a Python program that can store and manage this information during program execution.

## Objectives

* To create a simple badminton management system using Python.
* To store player information such as player ID, name, gender, and department.
* To display and search registered players.
* To schedule matches between two registered players.
* To store match date and time.
* To record scores for badminton games.
* To determine the winner of a match.
* To maintain basic player statistics such as matches played, wins, and losses.
* To provide a simple menu-driven interface for the user.

## Main Features

### 1. Player Management

The player management section provides the following options:

* Add a new player
* Display all registered players
* Search for a player using their player ID

Each player record contains:

* Player ID
* Name
* Gender
* Department/Branch
* Matches played
* Wins
* Losses
* Points

### 2. Match Management

The match management section provides the following options:

* Schedule a new match
* Display all matches
* Record a match result
* Search for a match

A match record contains:

* Match ID
* Player 1
* Player 2
* Match date
* Match time
* Match status
* Game scores
* Winner

### 3. Match Result

When a match result is recorded, the program accepts the scores of the games played. If both players win one game each, a third game is recorded.

The player who wins more games is declared the winner. The program then updates the players' match statistics.

## Data Structures Used

### Dictionary

A dictionary named `players` is used to store player information.

```python
players = {}
```

The player ID is used as the key, while the player's details are stored as values.

### List

A list named `matches` is used to store match records.

```python
matches = []
```

Each match is stored as a dictionary containing the match details.

## Python Functions Used

The project is divided into different functions to make the program easier to understand and manage.

| Function            | Purpose                           |
| ------------------- | --------------------------------- |
| `add_player()`      | Adds a new player                 |
| `display_players()` | Displays all registered players   |
| `search_player()`   | Searches for a player             |
| `schedule_match()`  | Schedules a new match             |
| `display_matches()` | Displays all matches              |
| `record_match()`    | Records match scores and result   |
| `search_match()`    | Searches for a match              |
| `player_menu()`     | Handles player management options |
| `match_menu()`      | Handles match management options  |

## Working of the Program

The program starts with the main menu:

```text
==================================
   BADMINTON SPORTS MANAGEMENT
==================================
1. Player Management
2. Match Management
3. Exit
```

The user selects an option from the menu.

If **Player Management** is selected, the user can add, display, or search for players.

If **Match Management** is selected, the user can schedule a match, display matches, record a result, or search for a match.

After completing an operation, the user can return to the respective menu or go back to the main menu.

## Expected Outcome

The project provides a basic console-based system for managing badminton players and matches. It demonstrates how Python data structures and functions can be combined to create a practical application.

## Future Improvements

The project can be improved in the future by adding:

* Permanent data storage using files or a database
* A graphical user interface
* Player rankings
* Tournament management
* Doubles match support
* Automatic score validation
* Match statistics and performance analysis
* Exporting records to CSV or Excel

## Conclusion

The Badminton Sports Management System is a simple application that demonstrates the practical use of Python programming concepts. It provides basic functionality for managing players, scheduling matches, recording results, and maintaining player statistics.
