## Plan: Draw Garden Scene

TL;DR - Implement a simple Pygame script that opens a window and renders a brown house on a green lawn, a tree bearing red apples, and scattered flowers in the grass. This exercise mirrors previous Pygame work but focuses on static drawing rather than gameplay.

**Steps**
1. Add new file `MiniGame/draw_garden.py` as a standalone script.
2. Initialize Pygame, set up window size (e.g. 800x600) and caption.
3. Define basic colors (brown, green, red, yellow, etc.).
4. In the main loop draw:
   - Fill background with sky color (light blue) and draw a green rectangle for grass across bottom.
   - Draw house: brown rectangle for walls, triangle or polygon for roof.
   - Draw tree: brown rect or polygon for trunk, green circle for foliage, and smaller red circles for apples placed within foliage.
   - Draw several small flowers on the grass as colored circles with lines for stems.
5. Handle event loop, allow quitting with window close.
6. Keep loop running at a fixed frame rate though scene static (e.g. 30 FPS).
7. Optionally structure drawing into functions such as `draw_house`, `draw_tree`, `draw_flowers` for readability.
8. Test by running script and verifying all elements appear correctly sized and colored.

**Relevant files**
- `MiniGame/minigame_sound.py` and other Pygame examples for window management and drawing calls.

**Verification**
1. Execute `python MiniGame/draw_garden.py` and confirm the window shows a brown house, grass, tree with apples, and flowers.
2. Close window with quit event; no errors in console.

**Decisions**
- Use Pygame for drawing due to existing familiarity in the repo.
- Scene is static; no interactivity required.
- Approximate positions and sizes are fine; focus is on meeting description.

**Further Considerations**
1. Could extend later with simple animations or interactivity if desired.
