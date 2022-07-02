"""
  queue
  A queue class allowing push, pop, peek, and q_size commands is created. The
  main use of this class for the compliance project will be to store commands
  and messages that need to be processed. This class will be used on both the
  front and back ends.
"""

class FixedSizeQueue:
    """A queue data struct that uses the methods push(v), pop(), and peek() to
    store and access data. Push(v) adds the value v to the back of the line,
    pop() removes and returns the value at the first of the line, and peek()
    returns a copy of the value at the first of the line without removing it.
    The method q_room_left() returns the available spaces for data."""
    
    def __init__(self, size=10):
        self._size = size   #max population for queue
        self._q = [None]*self._size  #init slots to None
        #front of line is also back of line when empty
        self._front = 0
        self._back  = 0
        self._available = self._size #keeps track of available open slots
        
    def push(self, v):
        "pushes the value v onto the back of the line if there is room."
        if self._available != 0:
            self._q[self._back] = v
            self._available -= 1
            self._back = (self._back+1) % self._size
        else:
            print("Queue is full!")
            
    def pop(self):
        """Returns the value from the head of the line and removes it from
        the queue."""
        if self._available != self._size:
            v = self._q[self._front]
            self._q[self._front] = None
            self._available += 1
            self._front = (self._front +1) % self._size
            return v
        else:
            print("Queue is empty!")
            return None
        
    def peek(self):
        """ Returns the value at the head of the line without removing it from
        the queue."""
        if self._available != self._size:
            return (self._q[self._front])
        else:
            print("Queue is empty!")
            return None
            
            
    def room_left( self ):
        """Returns the number of available spaces for data in the queue."""
        return (self._available)
    
        
if __name__ == "__main__":
    size = input("Queue size: ")
    q = FixedSizeQueue(int(size))
    print(f"Created queue name q of size {size}")
    print(dir(FixedSizeQueue))
    
    
    
