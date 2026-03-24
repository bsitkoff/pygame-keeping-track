## Change It

> **Watch:** Displaying Text on Screen

<iframe width="720" height="600"
  src="https://app.screencastify.com/watch/U5PJMMq3tgvq1FnmXMgJ/embed"
  title="Text Display in Pygame Zero"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen
></iframe>
  
---

### 1: Change the Score Display

Find `screen.draw.text(f"Score: {score}", ...)` in `draw()`. Try:
- Moving it to a different corner
- Changing the `fontsize`
- Changing the `color` — try `"yellow"`, `"cyan"`, or an RGB tuple like `(255, 100, 0)`

### 2: Add a High Score

Can you track the highest score across games? You'll need a new global variable at the top of the file and some logic to update it when a game ends. Display it on the game over screen.

*Hint: Think about when to check whether the current score beat the old record.*

### 3: Modify the Start Screen

The start screen currently says "DODGE AND COLLECT". Change the text and styling. What information does a player actually need before they start?

### 4: Change the Win/Lose Condition

What if the game ended when you reach 10 points instead of touching the alien? Try changing the losing condition or adding a winning condition.

{Check It!|assessment}(free-text-auto-1209705660)
