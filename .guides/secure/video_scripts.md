# Keeping Track — Video Scripts

These scripts go with the three screencast videos for the "Keeping Track" practice project. Each video is 3–5 minutes. Record with Screencastify.

Demo files are in `.guides/secure/video_demos/`.

---

## Video 1: Game Variables + The `global` Keyword

**Page:** Get Ready
**Objective:** I can use `global` correctly when a function needs to change a variable.
**Demo file:** `video_demos/global_broken.py` → `video_demos/global_fixed.py`

### Script

**[Open `global_broken.py` in the editor. Don't run it yet.]**

> "In PyGame Zero, we usually create variables at the top of our file — things like `score`, or later, a variable to track whether the game is over. These are called **global variables** because they live outside of any function."

**[Highlight `score = 0` at the top.]**

> "Here we've got `score = 0` at the top, a player, and a cookie. Inside `update()`, when the player touches the cookie, we do `score += 1`. Seems simple, right? Let's run it."

**[Run the file. Move the player into the cookie. The game crashes with `UnboundLocalError`.]**

> "Boom — error. `UnboundLocalError: local variable 'score' referenced before assignment`. That's Python telling us: 'inside this function, you're trying to change `score`, but I don't see where you created it *in this function*.'"

> "Here's the thing — Python lets you **read** a global variable from inside a function, no problem. But the moment you try to **change** it with `=` or `+=`, Python assumes you meant to create a brand new local variable. And since that local variable doesn't exist yet... crash."

**[Open `global_fixed.py`. Highlight the `global score` line.]**

> "The fix is one line: `global score`. This tells Python: 'I'm not making a new variable — I mean the `score` that already exists at the top of the file.'"

**[Run `global_fixed.py`. Collect a cookie. Score goes up.]**

> "Now it works. The score goes up because Python knows we're talking about the same variable."

**[Go back to the code.]**

> "Here's the rule: **if a function only *reads* a global variable, you don't need `global`. But if a function *changes* it — assigns to it, adds to it — you need `global` at the top of that function.** You'll use this a lot in your games today, especially for `score` and for a variable called `state` that controls which screen is showing."

---

## Video 2: Displaying Text on Screen

**Page:** Change It
**Objective:** I can display a score or message using `screen.draw.text()`.
**Demo file:** `video_demos/text_demo.py`

### Script

**[Open `text_demo.py`. Run it so the window is visible.]**

> "One of the most useful things in PyGame Zero is `screen.draw.text()`. You'll use it to show the score, instructions, game over messages — basically any words on screen."

**[Point to the first line in `draw()`.]**

> "The simplest version takes three things: the text you want to show, a position, and some options. Here's `screen.draw.text("Hello!", (10, 10), fontsize=30, color="white")`. The `(10, 10)` is the top-left corner where the text starts — 10 pixels from the left, 10 from the top."

**[Point to the centered text example.]**

> "If you want text centered — like for a title screen — use `center=` instead of a regular position. `center=(WIDTH // 2, 100)` puts the middle of the text at the center of the screen horizontally, 100 pixels down. This is great for titles and game over text."

**[Point to the color examples.]**

> "For colors, you can use names like `"red"`, `"cyan"`, `"yellow"`. Or if you want a specific color, use an RGB tuple — that's three numbers from 0 to 255 for red, green, and blue. `(255, 140, 0)` gives you orange. `(180, 60, 255)` gives you purple."

**[Point to the size examples.]**

> "`fontsize` controls how big the text is. 18 is pretty small, 30 is a good default, and 50 is big — good for titles or game over screens."

**[Point to the f-string score example.]**

> "Last thing — you'll almost always want to show a variable in your text. Use an f-string: `f"Score: {score}"`. The `{score}` gets replaced with the actual number. This is how you'll display the score in your game."

> "Quick summary: `screen.draw.text()` with a position or `center=`, a `fontsize`, and a `color`. That's all you need."

---

## Video 3: Game States

**Page:** Create Your Own
**Objective:** I can use a state variable to control what draws and what updates.
**Demo file:** Use `track.py` (already in the project)

### Script

**[Open `track.py` in the editor. Run it so the start screen is visible.]**

> "Before you build your own game, let's look at how `track.py` manages three different screens with one variable. Right now you're looking at the start screen. I press Space..."

**[Press Space. The game starts.]**

> "...and now I'm playing. I can move around, collect cookies, and the alien chases me. When it catches me..."

**[Let the alien catch the player.]**

> "...game over. I see my score and I can press R to go back to the start. Three completely different screens, all controlled by one variable."

**[Scroll to the top of the code. Highlight `state = "start"`.]**

> "Here it is: `state = "start"`. This string variable is the brain of the whole game. It's always one of three values: `"start"`, `"playing"`, or `"game_over"`."

**[Scroll to `update()`. Highlight the `if state != "playing": return` check.]**

> "In `update()`, the very first thing we check is: are we playing? If not, `return` — do nothing. That means the player can't move on the start screen or the game over screen. All the movement code, the alien chasing, the collision detection — it only runs when `state` is `"playing"`."

**[Scroll to `draw()`. Highlight the three `if/elif` blocks.]**

> "In `draw()`, we have three blocks. If `state` is `"start"`, we draw the title and instructions. If it's `"playing"`, we draw the player, alien, cookie, and score. If it's `"game_over"`, we draw the final score and restart message. Only one of these runs at a time — whichever state we're in."

**[Scroll to `on_key_down()`.]**

> "And `on_key_down()` is where we actually *change* the state. Space on the start screen sets state to `"playing"` and calls `reset_game()`. R on the game over screen sets it back to `"start"`. Notice we need `global state` because we're changing it."

**[Go back to the full file view.]**

> "So the pattern is: one variable at the top, check it in `update()` and `draw()`, change it in `on_key_down()`. That's it. When you build your own game in `tryit.py`, you'll follow this same pattern. Start with the state variable, then fill in what each state looks like and does."
