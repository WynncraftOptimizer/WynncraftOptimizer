# WynncraftOptimizer
WynncraftOptimizer

will need to download python, i used python 3.9
will need to download kivy and kivymd here are the links:
https://kivy.org/#home
https://kivymd.readthedocs.io/en/0.104.1/index.html

not sure if you will nead to import threading, but might need to look into that.

i am using the sequential version of the code, but at the bottom of the main file is also my tries to implement a parallel version,
which worked for an earlier version, but was slower.

I recommend using sliders, but if you need to write in to the textfields, you need to press enter after so the value gets updated in the code.
Also I recommmend just using the first optimizer thing and the other further opimizations only in edge cases, because they add a lot of time.
The checks dont add more time so you can add them freely, and to get non negative values there you will have to type in to the textfields.
Also recommended to set the expected value higher then lower, if you dont want to overflood your results,
the optimizer will still find the best result for the first optimization id given the other ids and cheks, it only optimizes for it, all other are required
for the optimizer to print them in the output.
If you see a looooot of items being found you will need to stop the program and restart.
you can check the found items during the Optimization, but be patient, the ui is running on one thread, so its slow, to optimize for the optimisations sake.
After the Optimizer completed, the best item for your input will be placed in to the very first slot so you can see it immediately.
