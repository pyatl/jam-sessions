Exercise for June 2015 Jam Session
==================================

Hunt the Wumpus!
===============

In this game, the goal is to wander the maze and find the Wumpus 
by process of elimination.  The player has only one arrow so he has
to make it count!

Gameplay
--------
- The maze is a grid of rooms
- The Wumpus is placed randomly in the maze in one of the rooms.
- The player is placed randomly in the maze in one of the rooms, but not the same room as the Wumpus.
- The maze may also contain hazards - 2 bats, 2 bottomless pits.
- The player moves to an adjacent room, one room at a time.
- If the player moves into an adjacent room to a hazard or Wumpus, he gets a warning message:
    - "I smell a Wumpus" for the Wumpus
    - "Bats nearby" for a bat
    - "I feel a draft" for a pit.
- If the player thinks the Wumpus is in the next room, he can choose to shoot his arrow into that room.
- If the player fires into the Wumpus room, he wins.
- If the player fires into a room that does not have the Wumpus, the Wumpus eats him.
- If the player enters the Wumpus room, the Wumpus eats him.
- If the player enters a pit room, he falls and dies.
- If the player enters a bat room, he is transported randomly to another room.

Implementation
--------------

- Phase 1: Just implement placing, finding, killing the Wumpus.

- Phase 2: Add additional traps - bats, pits.

- Phase 3: What happens if you changes the maze shape?  What could you do to improve trap detections?  What if the Wumpus or Bats could move?  Could you write an AI to play this game itself?
