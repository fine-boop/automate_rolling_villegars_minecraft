# automate_rolling_villegars_minecraft
An application written in python to automate the monotonous task of rolling librarian villagers, over and over again.
I have added a demo video of my using this script, below.

[![Watch the demo](https://img.youtube.com/vi/plzCukYWmDc/0.jpg)](https://www.youtube.com/watch?v=plzCukYWmDc&t=55s)

# Usage 

So, there is actually not much you will need to do to set this script up for yourself.
All you need to do is 

  1. Turn off raw input in controls/mouse settings
  2. Equip yor axe in hotbar slot 1
  3. At least 1 lectern in hotbar slot 2

Once you have done this, ensure you are standing in the centre of the block in front of the villegar (as shown in the video), and have at least 4 ish blocks of space 
behind where your standing. 

Now you can run the script. I would reccomend running it with the `-W ignore` flag to suppress the warnings we get from the easyocr library. 
You can kill the script at any time by pressing the page_up key. 


# todo

  - Optimize the pyautogui scripting to acheive the fastest possible method
  - Add a feature where the user can put any enchants they want in a file and the script will exit if its sees any
  - Add a feature where the script can start with a hotkey instead of a wait
