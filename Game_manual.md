# Hit and Blow Game Manual

## Game Overview
Hit and Blow is a card-based guessing game implemented using only Python's standard library. Players must deduce the correct sequence of cards by making guesses and receiving feedback on hits (correct position and card) and blows (correct card but wrong position).

**Objective:** Guess the hidden correct cards in the fewest attempts.

**Developed with:** Python 3.14.0 (standard library only, no external dependencies). Inspired by Mastermind, adapted for cards.

## Rules
- **Cards:** 0-9 digits and 12 zodiac signs (mouse, cow, tiger, rabbit, dragon, snake, horse, ram, monkey, rooster, dog, boar). Total 22 unique cards.
- **Hit:** Correct card in the correct position.
- **Blow:** Correct card but in the wrong position.
- **Win Condition:** All cards are hits (e.g., 4 hits for 4-card mode).
- **Example:** If correct is [1, mouse, 2, tiger] and guess is [1, cow, tiger, 2], then 1 Hit (1), 2 Blows (tiger and 2).

## Difficulty Levels
- Select number of hand cards (total cards dealt, 4-10).
- Select number of correct cards (sequence length to guess, 3-6).
- Example: 8 cards, 4 correct → Guess 4-card sequence from 8 cards. Higher numbers increase difficulty.

## How to Play
1. **Start:** Click "START" to begin. Launches the main menu.
   <img src="./rdm_images/hitandblow_scr_rdm_01.png" width="628" alt="Start Screen">

2. **Select Difficulty:** Choose number of cards and correct sequence length. Affects game complexity.
   <img src="./rdm_images/hitandblow_scr_rdm_02.png" width="628" alt="Difficulty Selection">

3. **Guess:** Select cards by clicking, then click "JUDGE!" to submit. Feedback shows hits and blows. Repeat until win.
   <img src="./rdm_images/hitandblow_scr_rdm_03.png" width="628" alt="Gameplay">

4. **Win:** Achieve all hits. Game ends with congratulations.
   <img src="./rdm_images/hitandblow_scr_rdm_04.png" width="628" alt="Win Screen">

5. **Replay:** Choose to play again or exit. Returns to start screen.
   <img src="./rdm_images/hitandblow_scr_rdm_05.png" width="628" alt="Replay Prompt">

## Controls
- **Mouse:** Left-click cards to select/deselect. Hover for visual feedback.
- **Button:** "JUDGE!" to submit guess (requires exact number of cards selected).
- **Back:** Button to return to previous screen (difficulty or start).

## Tips
- Use hit/blow feedback to narrow down possibilities. Note positions and types carefully.
- Track attempts in the history (displayed in console; future updates may add GUI history).
- Start with common cards like digits; avoid duplicates if possible to maximize information.
- Lower difficulty (fewer cards) for beginners; increase for challenge and strategy depth.
- Experiment with permutations: If you have 1 Hit and 1 Blow, swap positions to test.

## Features
- **Pure Python:** No external libraries, ensuring portability and simplicity.
- **GUI:** Intuitive Tkinter-based interface with custom card sprites for visual appeal.
- **Adaptive Layout:** Canvas dynamically resizes based on selected card count for optimal display.
- **Error Handling:** User-friendly messages prevent invalid guesses (e.g., wrong number of cards).
- **Cross-Platform:** Tested on Windows 11; compatible with Linux/Mac via Tkinter.
- **Educational:** Teaches logic, deduction, and probability through gameplay.

## System Requirements
- Python 3.14.0 or higher (latest stable recommended).
- Tkinter (included in standard Python installations).
- OS: Windows/Linux/Mac (GUI rendering may vary by OS theme).
- No additional dependencies or hardware requirements beyond basic PC specs.

## Troubleshooting
- **Game won't start:** Ensure Python 3.14+ is installed and Tkinter is available (check with `python -c "import tkinter"`).
- **Images not loading:** Verify image files are in `./rdm_images/` folder relative to the script.
- **Invalid guess error:** Select exactly the number of correct cards before clicking "JUDGE!".
- **Performance issues:** Reduce card count for smoother gameplay on low-end devices.
- **GUI glitches:** Restart the application; Tkinter themes may differ by OS.

## FAQ
- **Q: Can I play without GUI?** A: No, the game requires Tkinter for the interface.
- **Q: Are there sound effects?** A: No, as per standard library only rule.
- **Q: How to change difficulty mid-game?** A: Restart from the difficulty screen.
- **Q: Is it multiplayer?** A: Single-player only.
- **Q: Can I modify the code?** A: Yes, but keep it standard library compliant.

## Version History
- **v1.0 (2025):** Initial release with basic Hit and Blow mechanics, GUI, and difficulty selection.

Developed by: Team [Your Team Name]  
For: Information Technology I b Final Assignment, 2025</content>
