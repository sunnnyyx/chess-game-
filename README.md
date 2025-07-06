# ♟️ Chess: Python Chess Game

**Chess** is a fully interactive chess game built with **Python** and **Pygame**, featuring elegant drag-and-drop mechanics, sound effects, theme switching, and a clean, object-oriented architecture. It's a great showcase project for learning Python game development and building real-world OOP applications.

---

## 📸 Demo

![Game Screenshot](screenshot/demo.png)

---

## 🚀 Features

- 🎯 Intuitive drag-and-drop piece movement  
- 🎨 Dynamic theme switching (`T` key)  
- 🔊 Realistic move and capture sounds  
- ♟️ Highlighted valid moves and last move tracking  
- 🔁 Game reset functionality (`R` key)  
- 🧠 Modular, clean object-oriented codebase  

---

## 📂 Project Structure

<pre> ```python-chess-/
│
├── logos-and-songs/ # Images and sounds
│ ├── images/ # Chess piece textures
│ └── sounds/ # move.wav, capture.wav
│
├── screenshot/ # Game screenshots
│ └── demo.png
│
├── app.py # Main launcher script
├── chess_game.py # Core game logic
├── chess_board.py # Board representation
├── drag_manager.py # Piece dragging functionality
├── config.py # Theme, sound, and settings
├── theme.py # UI themes
├── color.py # Color pairings for themes
├── const.py # Constants for the board
├── sound.py # Sound player class
├── piece.py # Piece definitions
├── square.py # Tile logic ``` </pre>


---

## 🕹️ Controls

| Action            | Key / Input      |
|-------------------|------------------|
| Move piece        | Drag with mouse  |
| Switch theme      | Press `T`        |
| Reset game        | Press `R`        |
| Quit game         | Close window     |

---

## 🔧 Installation

### 🛠 Prerequisites
- Python 3.8 or above
- `pygame` library

### 📦 Install Dependencies

```bash
pip install pygame

