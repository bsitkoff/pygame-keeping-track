## Backgrounds

<iframe width="560" height="315"
  src="https://www.youtube.com/embed/37LVhP15zGw?si=hRxEFHTLXModXLB_"
  title="YouTube video player"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen
></iframe>

---

Right now your game has a solid color background from `screen.fill()`. You can replace that with an image using `screen.blit()`.

### How it works

```python
def draw():
    screen.blit('background', (0, 0))
```

- The image file goes in your `images/` folder, just like sprites
- `'background'` is the filename without `.png`
- `(0, 0)` is the top-left corner — this draws the image across the whole window
- **Draw it first** in `draw()`, before any Actors — otherwise it will cover them up

Your background image should be **800x600 px** to match your game window (`WIDTH` and `HEIGHT`).

---

### Try it

1. Find or create a background image (800x600 px)
2. Save it as a `.png` in your `images/` folder
3. Replace `screen.fill(...)` with `screen.blit('yourfilename', (0, 0))` in your `draw()` function
4. Run your game with `python3 tryit.py`

You can use **[Canva](https://www.canva.com/)** to create a simple background, or search for free game backgrounds online.
