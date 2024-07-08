import curses

from contextlib import chdir
from curses import wrapper
from pathlib import Path

class HSMain:
  def __init__(self):
    # Store curses window object.
    self.stdscr = curses.initscr()
    self.stdscr.resize(8, 96)
    # Initialise default colour set.
    curses.start_color()
    
    # Initialise curses.
    wrapper(self.main)
  
  def main(self, stdscr):
    operating = True
    screen_max_y, screen_max_x = self.stdscr.getmaxyx()
    
    if curses.has_colors():
      self.initpalette()
      self.stdscr.bkgd(' ', curses.color_pair(7))
      self.drawmenu(stdscr)
      
      c_pos_y, c_pos_x = self.stdscr.getyx()

      with chdir(Path(__file__).parent.absolute()):
        while operating:
          # Pause for user input.
          c = self.waiting()
        
        self.finish()
    else:
      self.finish()
  
  def waiting(self) -> int:
    """
    Halt code execution and wait for user input.
    
    Returns:
      (int): Integer represenation of the user's keypress
    """
    return self.stdscr.getch()
  
  def finish(self):
    """
    Perform any clearup before program exit.
    """
    return
  
  def initpalette(self):
    """
    Set colour palette for the terminal.
    """
    # Light BG colours.
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
    # Dark BG colours.
    curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(9, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    
  def drawmenu(self, stdscr):
    stdscr.addstr(0, 0, 'Load audio file', curses.color_pair(7))
    stdscr.addstr(6, 0, '(c) Jon Herbst, 2024', curses.color_pair(8))
    stdscr.addstr(7, 0, 'HERBALSYNTH vocal synthesiser, version 0.1.0', curses.color_pair(8))

HSMain()
