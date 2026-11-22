# climbing_game
Welcome to glorious Mount Peaks! You wish to climb it to prove your peakness to the world. Only a slight problem of the constant avalanches and sharp red rocks blocking your way. As you delve into climbing the mountain, you see that those spikes have blocked seemingly every single pathway, and your only way up is to jump quite perfectly on the edges of those platforms...

# Goal
The goal of this game is to climb to the top of the two levels. You do this by jumping and parkour!

# Movement
The movement system uses the arrow keys to move, with left and right moving their respective directions, and up making you jump.

# Obstacles
The obstacles are snowballs and spikes. The snowballs fall from a random position in the sky, simulating avalanches. In contrast, the spikes spawn on the top of the occasional platform, creating an extra level of difficulty in figuring out a path that doesn't hit a spike. 

Getting hit by an obstacle or falling off the mountain will result in the immediate loss of the game, and you will have to restart at the beginning of level 1. To restart, press 'r'.

# Other Features
The scrolling feature has been added to this game, so that instead of the player moving on the screen, the screen moves to follow the player (most of the time, until they reach level boundaries). This is only a y-scroll, no x-scrolling here.

The spikes randomly generate on about 1/5 of the platforms.

A good amount of the coding time was spent improving memory efficiency, so only the things that are visible to the player are actually tracked, so things like snowballs offscreen or platforms offscreen aren't tracked, therefore saving memory.

# Closing Notes
Thanks for reviewing! This is my 4th pygame project ever, and 4th for Terra. I definitely learned a good amount this week, though not as much as last week, I think.
