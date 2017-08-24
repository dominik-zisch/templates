#!/usr/bin/python

# Version:      0.1
# Last changed: 01/01/17

import sys
import signal
import time


# ============================================================================//
# ----------------------------------------------------------------------// Class

class ClassTemplate():

    def __init__( self, arg ):
        self.arg = arg

    def start( self ):
        print("Starting Class Template.")

    def stop( self ):
        print("Stopping Class Template.")

    def do_something( self, topic, msg ):
        print("Doing something.")

# ----------------------------------------------------------------------// Class
# ----------------------------------------------------------------------------//



# ============================================================================//
# -------------------------------------------------------------// Signal handler

# -----------------------------------------------/
# ---/ catch Ctrl+C to end program
def signal_handler( signal, frame ):
    global running
    running = False

# -------------------------------------------------------------// Signal handler
# ----------------------------------------------------------------------------//



# ============================================================================//
# ---------------------------------------------------------// Main program logic

def main():

    # add signal handler for SIGINT
    signal.signal( signal.SIGINT, signal_handler )

    # init stuff
    pass

    # main program loop
    running = True
    while ( running ):
        pass
        time.sleep( 0.1)

    # cleanup
    print( 'Closing program!' )
    sys.exit( 0 )


if __name__ == '__main__':
    main()

# ---------------------------------------------------------// Main program logic
# ----------------------------------------------------------------------------//
