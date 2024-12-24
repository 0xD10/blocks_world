import sys
import time
from copy import deepcopy
sys.setrecursionlimit(1000000000) 

def compare_states(current_state, goal_state):                              # This function check if two states are equal 
  return list(filter(None, current_state))==list(filter(None, goal_state))  # p.e. [[],[],[],['A','B','C']] will be equal to [['A','B','C']]

def get_children(state, visited):                    # Function to create all possible places for a certain block
  children = list()                                  # Usefull for all alg.
  moves = list()                                     # Also appends the action that happened p.e. MOVE(<block>, <moved_from>, move_to)
  temp_stack = deepcopy(state)
  for i in range(len(state)):
    if temp_stack[i]:
      temp_block = temp_stack[i].pop()
      for j in range(len(temp_stack)):
        if i!=j:
          temp_stack[j].append(temp_block)
          state_key = tuple(tuple(stack) for stack in temp_stack)
          if state_key not in visited:
            if len(temp_stack[j])==1:
              move_to = "table"
            else:
              move_to = str(temp_stack[j][-2])
            if len(temp_stack[i])==0:
              moved_from = "table"
            else:
              moved_from = str(temp_stack[i][-1])
            children.append(deepcopy(temp_stack))
            moves.append(f"Move ({str(temp_block)}, {moved_from}, {move_to})")
          temp_stack[j].pop()
      temp_stack[i].append(temp_block)
  return [children, moves]

# Depth-First-Algorithm
def dfs(current_state, goal_state, path, visited, moves, start_time, optimize):    # A classic DFS implementation with visited set and the path
  if visited==None:                                         
    visited=set()

  state_key = tuple(tuple(stack) for stack in list(filter(None, current_state)))   
  if state_key in visited:                            # Check if the currest state is visited before
    return False
  visited.add(state_key)

  if compare_states(current_state, goal_state):    # The custom equal function
    path.append(current_state)
    return True

  childrens, possible_moves = get_children(current_state, visited)
  for i in range(len(childrens)):                                          
    state_key = tuple(tuple(stack) for stack in childrens[i])            
    if int(time.time())-start_time>=60:
      TIMEOUT()
    if state_key not in visited:
      if optimize:
        childrens[i] = list(filter(None, childrens[i]))                                    
      if dfs(childrens[i], goal_state, path, visited, moves, start_time, optimize):      # Recursion call for DFS if is True 
        path.append(current_state)                                                       # we add the path and the move that happened
        moves.append(possible_moves[childrens.index(childrens[i])])
        return True
  return False

def main(current_state, goal_state, path, visited):                                       # Optimized DFS check all the possible init_states
  moves = []                                                                              # p.e. init_state = [[a,b], [], []], then the first iteration will be
  start_time = int(time.time())                                                           # [[a,b]] if we find a solution all good if not then -> [[a,b], []] so we simply
  dfs(current_state, goal_state, path, visited, moves, start_time, True)                  # filter the init_state and check for a solution with the minimum empty_stacks
  if len(moves)==0:
    for i in range(len(current_state)-len(list(filter(None, current_state)))):
      dfs(current_state[:len(list(filter(None, current_state)))+i], goal_state, path, visited, moves, start_time, False)
  return moves[::-1]

def TIMEOUT():
  print("Run-time 60secs limit!\nProgram terminated!\n")
  exit(-1)