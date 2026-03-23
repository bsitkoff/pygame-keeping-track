## Create Your Own


<iframe width="720" height="600"
  src="https://app.screencastify.com/watch/Go1lW5r9wscm4wIJ2Zcs/embed"
  title="Game States in PyGame Zero"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen
></iframe>
  
---

Build a complete game with states in `tryit.py`.

---

### Using Your Own Sprites

*Need a custom image? Here's the workflow — or rewatch the video from Lesson 1.*

1. Find a PNG image you want to use and save it to your download folder
2. Open **[Canva Image Resizer](https://www.canva.com/features/image-resizer/)**, upload your image, resize it to **80x80 px**, and download as PNG
3. Upload the file to your `images/` folder in Codio
4. Update the `Actor('name')` in your code to match the filename (no `.png`)

---

### Requirements

Build a game in `tryit.py` that:

1. Has a **start screen** that waits for a keypress before the game begins
2. Has a **playing state** with a moving player, at least one enemy, and a collectible
3. **Tracks and displays a score** while playing
4. Has a **game over screen** that shows the score and lets you restart
5. Uses **your own sprites**

{Check It!|assessment}(llm-based-auto-rubric-4016486497)

---

Optional challenge: can you add a high score that persists across restarts?

<details><summary>Hint: how do you save data between runs?</summary>

You can use `open()` to save and load from a text file. Here's an example that saves and reads a fruit name:

```python
# Writing to a file
f = open("fruits.txt", "w")
f.write("mango")
f.close()

# Reading from a file
f = open("fruits.txt", "r")
name = f.read()
f.close()
print(name)  # mango
```

To make this work for a high score, you'll need to figure out:
- How to convert between strings and integers (`str()`, `int()`)
- When to save the file (after a new high score?)
- What to do the very first time, when the file doesn't exist yet (`try`/`except`)

</details>
