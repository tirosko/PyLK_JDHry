## Plan: Create Minigame with Small Paddle and Falling Circles

TL;DR - Create a new Pygame minigame file (minigame_AI.py) based on the existing minigame_sound.py, but with a smaller paddle (113 pixels wide, approx. 3 cm) and falling circular objects instead of squares. Keep similar mechanics: catch falling circles with paddle, score points, increasing speed, with sound effects.

**Steps**
1. Create new file [MiniGame/minigame_AI.py](MiniGame/minigame_AI.py) by copying the structure from [MiniGame/minigame_sound.py](MiniGame/minigame_sound.py).
2. Modify paddle initialization: Set paddle width to 113 pixels (instead of 120), keep height 20, position centered at bottom.
3. Change falling objects to circles: Replace block list with circle list, each circle has x, y, radius (e.g., 10), speed.
4. Update spawning: Random x position, y=0, radius=10, speed=initial.
5. Update drawing: Use pygame.draw.circle for falling objects instead of rect.
6. Update movement: Move circles down by speed each frame.
7. Update collision detection: Check if circle bottom (y + radius) >= paddle top and circle x within paddle left and right. If yes, remove circle, play sound, increase score, speed.
8. Update game over: If any circle y - radius > screen height, game over.
9. Keep sound loading and playback as in minigame_sound.py.
10. Test the game: Run the script, ensure paddle moves, circles fall, collision works, sound plays.

**Relevant files**
- [MiniGame/minigame_sound.py](MiniGame/minigame_sound.py) — Reference for code structure, sound handling, and game loop.

**Verification**
1. Run `python MiniGame/minigame_AI.py` and verify the game window opens, paddle is narrow (113px), falling circles appear and move down.
2. Test controls: Move paddle left/right with arrow keys.
3. Test collision: Catch circles, hear sound, score increases, speed increases.
4. Test game over: Let circles pass bottom, game over message appears.

**Decisions**
- Paddle width: 113 pixels (3 cm at 96 DPI).
- Circle radius: 10 pixels for visibility.
- Mechanics: Identical to existing minigame except shapes.
- File location: MiniGame/ folder.
- No additional features beyond the query.
