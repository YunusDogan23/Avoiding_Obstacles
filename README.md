# Avoiding Obstacles (Engelden Kaçma)

A small terminal game written in Python. You drive a car on a two-lane road and try to dodge obstacles that show up in random lanes.

- **Course:** Programming in Engineering
- **Instructor:** Assist. Prof. Dr. Ulya Bayram (@ubayram)
- **University:** Çanakkale Onsekiz Mart University
- **Faculty:** Faculty of Engineering
- **Department:** Electrical and Electronics Engineering

## Description

Engelden Kaçma ("dodging obstacles" in Turkish) is a simple text-based game that runs in the terminal. The road has two lanes, left (`sol`) and right (`sağ`), and your car starts in the left lane. In every round an obstacle appears in one of the lanes at random. You don't know where it will come from, so you have to pick a lane and hope for the best.

If you end up in the same lane as the obstacle, you crash and lose health. If you're in the other lane, you dodge it and earn points. The game keeps going until you run out of lives, then it shows how many rounds you survived and your final score.

The project was written to practice the basics of object-oriented programming in Python: classes, methods, instance variables, loops and handling user input.

## How to Play

1. Run the game (see [Running the Game](#running-the-game) below).
2. At the start of each round the game shows the round number, your lives, health and score, which lane your car is in, and a small drawing of the road:

   ```
     sol   sağ
   |     |     |
   |  A  |     |
   ```

   `A` is your car. `X` is the obstacle, and `*` means you crashed into it.

3. Choose your lane:
   - type `sol` to move to the **left** lane
   - type `sağ` (or `sag`) to move to the **right** lane
   - press **Enter** without typing anything to stay in your current lane

   If you type something else, the game asks again.

4. The obstacle shows up and the road is drawn again:
   - **Same lane as the obstacle:** you crash and lose **50 health**.
   - **Other lane:** you dodge it and get **+10 points**.

5. **Rules**
   - You have **3 lives**, and every life starts with **100 health**.
   - When your health reaches 0 you lose a life and your health is refilled.
   - When all your lives are gone, the game is over.

6. Press `Ctrl + C` any time to quit.

> Note: the in-game text is in Turkish. `sol` = left, `sağ` = right, `hak` = lives, `can` = health, `puan` = score, `tur` = round.

## Requirements

- **Python 3** (any recent version, 3.8 or newer is fine)
- **Jupyter Notebook** (optional, only if you want to run the game in a notebook)

The game itself only uses Python's built-in `random` module, so **no extra packages need to be installed** to play it from the terminal.

To install Jupyter Notebook:

```bash
pip install notebook
```

On some systems you may need `pip3` instead of `pip`:

```bash
pip3 install notebook
```

## Running the Game

**From the terminal**

```bash
git clone https://github.com/YunusDogan23/Avoiding_Obstacles.git
cd Avoiding_Obstacles
python engelden_kacma.py
```

(Use `python3` instead of `python` on macOS / Linux if needed.)

**In Jupyter Notebook**

```bash
jupyter notebook
```

Then open a new notebook in the project folder and run this in a cell:

```python
%run engelden_kacma.py
```

The game asks for your input in a text box under the cell.

## Files

| File | Description |
|------|-------------|
| `engelden_kacma.py` | The game code |
| `README.md` | This file |
| `LICENSE` | MIT License |

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
