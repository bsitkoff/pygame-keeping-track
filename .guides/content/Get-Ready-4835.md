## Get Ready

---

Most games need to keep track of things — your score, whether you've won or lost, which screen to show. In PyGame Zero, we do that with **variables at the top of the file**. But there's a catch.

Look at this code snippet:

```python
score = 0

def update():
    if player.colliderect(cookie):
        score += 1
```

**What do you think happens when you run this?** Does it work? Why or why not?

{Check It!|assessment}(free-text-auto-764560074)
