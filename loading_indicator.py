#!/usr/local/bin/python3
#
# loading_indicator.py - demonstrates a loading indicator via a bar. 
# usage: ./loading_indicator.py - will run sample code to demonstrate bar loading as Python counts to a million in a commandline interface
# requires the write and flush functions from sys.stdout to facilitate flushing to buffer

from sys import stdout

def loading_bar(count, total, status='Loading'):
    """Presents loading bar to STDOUT [##########--------------------]33.3% ... Loading
    
    Args:
    count  -- current count from the total. Used to calculate loading percentage.
    total  -- maximum possible count. Used to calculate loading percentage
    status -- shows status name next to loading bar. Default 'Loading'.
    """
    if count == total:
        status = "Complete"

    BAR_FILLER = '#'            # what to fill progress bar with (ie '#', '=', etc.)
    BAR_UNFILLED = '-'          # yet to be filled space
    MAX_BAR_LEN = 60            # maximum size of bar at 100%

    # CALCULATIONS
    filled_len = int(round(MAX_BAR_LEN * count / float(total)))                 # how long the BAR_FILLER should be
    percents = round(100.0 * count / float(total), 1)                           # what the current % the loading bar is at
    bar = BAR_FILLER * filled_len + BAR_UNFILLED * (MAX_BAR_LEN - filled_len)   # creates the entire bar

    # Write to STDOUT as program runs
    stdout.write('[{}]{}{} ... {}\r'.format(bar, percents, '%', status))
    stdout.flush()


# Demo - loading screen indicates when Python is done looping through range(1_000_000)
if __name__ == "__main__":
    MAX_LOOPS = 1_000_000

    for i in range(MAX_LOOPS+1):
        loading_bar(i,MAX_LOOPS)
