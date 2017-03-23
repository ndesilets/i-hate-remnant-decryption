# i-hate-remnant-decryption

Are you too stupid to play Remnant Decryption in Mass Effect: Andromeda? Don't worry, so am I!

## Requirements
1. python 2.7
2. numpy

## Instructions
1. Assign each of the 5 possible glyphs a number
  * Recommended: glyph after first click on empty tile = 1, glyph after second click = 2, etc...
2. `python main.py [grid size]`
  * Example: for a 5x5 grid, `python main.py 5`
3. Input each row of glyphs (as the numbers you assigned previously)
4. Voila

As long as you ensure that your assigned numbers match their respective glyphs when inputting the values into the script and also in-game it *should* work.

## Disclaimer
This has only been tested on a Windows 10 machine using a 32-bit version of Python 2.7. 
It is possible to exceed the 2GB memory limit using this script for certain input grids. 
In my experience these types of input grids were made up and likely impossible to solve to begin with. 

I have only tested this script on one 5x5 grid in the game and it worked.
It is entirely possible this script is completely wrong and won't work for anything else.

I am not responsible if your computer explodes or begins growing arms and legs.

## Side note
There are certainly faster and more efficient ways to find a solution for this sudoku-like game. 
A runtime within 4 seconds on a 5x5 grid single-threaded is good enough for me :) 

## Changelog

03/23/17:
- Added shape constraints for 5x5 grid (derp)

---

## Example

### Assigning numbers to glyphs
![Assigning glyphs](https://github.com/ndesilets/i-hate-remnant-decryption/blob/master/img/example1.jpg)

### Inputting glyphs as numbers into row values
![Glyph input](https://github.com/ndesilets/i-hate-remnant-decryption/blob/master/img/example2.jpg)

### Using the solution
![Solution example](https://github.com/ndesilets/i-hate-remnant-decryption/blob/master/img/example3.jpg)
