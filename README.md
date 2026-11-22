# climbing_game
Welcome to glorious Mount Peaks! You wish to climb it to prove your peakness to the world. Only a slight problem of the constant avalanches and sharp red rocks blocking your way. As you delve into climbing the mountain, you see that those spikes have blocked seemingly every single pathway, and your only way up is to jump quite perfectly on the edges of those platforms...

<img width="411" height="494" alt="Screenshot 2026-11-22 12 51 48 PM" src="https://github.com/user-attachments/assets/abb742e8-52fe-4e21-92cd-3772d78d09d9" /><img width="411" height="494" alt="Screenshot 2026-11-22 12 54 41 PM" src="https://github.com/user-attachments/assets/9104930c-3018-483f-a1c5-86859a87a881" />
<img width="411" height="494" alt="Screenshot 2026-11-22 12 53 02 PM" src="https://github.com/user-attachments/assets/8005f7d2-ecc3-43c8-b8b0-7ec845ef357f" />
<img width="411" height="494" alt="Screenshot 2026-11-22 12 52 12 PM" src="https://github.com/user-attachments/assets/78946a22-c49c-4fd2-927d-d036b0d39350" />


# Goal
The goal of this game is to score the most points, and points are scored if you climb to the top of the two levels. You do this by jumping and parkour!

# Movement
The movement system uses the arrow keys to move, with left and right moving their respective directions, and the up key making you jump.

# Obstacles
The obstacles are snowballs and spikes. The snowballs fall from a random position in the sky, simulating avalanches. In contrast, the spikes spawn on the top of the occasional platform, creating an extra level of difficulty in figuring out a path that doesn't hit a spike. 

Getting hit by an obstacle or falling off the mountain will result in the immediate loss of the game, and you will have to restart at the beginning of level 1. To restart, press 'r'.

# Scoring System
Your score acts as a timer as well: You start with a score of 400, and incrementally the score decreases by 1, essentially timing yourself. If the score hits 0, the game ends and you lose.

# Other Features
The scrolling feature has been added to this game, so that instead of the player moving on the screen, the screen moves to follow the player (most of the time, until they reach level boundaries). This is only a y-scroll, no x-scrolling here.

The spikes randomly generate on about 1/5 of the platforms.

A good amount of the coding time was spent improving memory efficiency, so only the things that are visible to the player are actually tracked, so things like snowballs offscreen or platforms offscreen aren't tracked, therefore saving memory.

# Closing Notes
Thanks for reviewing! This is my 4th pygame project ever, and 4th for Terra. I definitely learned a good amount this week, though not as much as last week, I think.
