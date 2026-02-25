## Change It

> 📹 **Watch:** Displaying Text on Screen
> *Record in Screencastify — show screen.draw.text(), positioning, fontsize, color options*
> *Objective: I can display a score or message using screen.draw.text().*
> **[ADD VIDEO URL WHEN RECORDED]**

---

## 1: Change the Score Display

Find `screen.draw.text(f"Score: {score}", ...)` in `draw()`. Try:
- Moving it to a different corner
- Changing the `fontsize`
- Changing the `color` — try `"yellow"`, `"cyan"`, or an RGB tuple like `(255, 100, 0)`

## 2: Add a High Score

At the top of the file, add `high_score = 0`. In the game over state, update it:

```python
if score > high_score:
    high_score = score
```

Display it on the game over screen.

## 3: Modify the Start Screen

The start screen currently says "DODGE AND COLLECT". Change the text and styling. What information does a player actually need before they start?

## 4: Change the Win/Lose Condition

What if the game ended when you reach 10 points instead of touching the alien? Try changing the losing condition or adding a winning condition.

---

> *[TODO: insert free-text-auto assessment — "What did you change? Describe what your game does now."]*
