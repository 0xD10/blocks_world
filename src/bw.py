#!/usr/bin/python3
import sys
import parser
import a_star_search, best_first_search
import depth_first_search, breadth_first_search

def main():
  data = parser.parser(sys.argv[2])
  objects = data.get_objects()
  init_state = data.get_initial_state()
  goal_state = data.get_goal_state()
  print(f"Init state = {init_state}")
  print(f"Goal state = {goal_state}\n")
  if sys.argv[1]=="depth": 
    dfs_path = list()
    moves = depth_first_search.main(init_state, goal_state, dfs_path, None)
    dfs_path = dfs_path[::-1]
    file_out = open(f"{sys.argv[3]}", "w")
    if len(moves)==0:
      print(f"No solution found!")
    else:
      for i in range(len(moves)):
        file_out.write(f"{moves[i]}\n")
    file_out.close()
  elif sys.argv[1]=="breadth":
    solution_path = breadth_first_search.main(init_state, goal_state)
    if solution_path:
      file_out = open(f"{sys.argv[3]}", "w")
      for i in range(1, len(solution_path)):
        file_out.write(f"{solution_path[i][1]}\n")
      file_out.close()
    else:
      print("No solution found!")
  elif sys.argv[1]=="astar":
    solution_path = a_star_search.main(init_state, goal_state)
    if solution_path:
      file_out = open(f"{sys.argv[3]}", "w")
      for i in range(1, len(solution_path)):
        file_out.write(f"{solution_path[i][1]}\n")
      file_out.close()
    else:
      print("No solution found!")
  elif sys.argv[1]=="best":
    solution_path = best_first_search.main(init_state, goal_state)
    if solution_path:
      file_out = open(f"{sys.argv[3]}", "w")
      for i in range(1, len(solution_path)):
        file_out.write(f"{solution_path[i][1]}\n")
      file_out.close()
    else:
      print("No solution found!")
  else:
    syntax_error()

def syntax_error():
  print("Usage ./bw.py <algorithm> <problem_file> <output_file_name>")
  print("[Algorithms available]\ndepth\nbreadth\nastar\nbest\n")
  exit(-1)

if __name__=='__main__':
  main()