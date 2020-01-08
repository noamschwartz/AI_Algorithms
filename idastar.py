import math
import ways
import ways.info as info
from node import Node
from ways import compute_distance

#returns the speed ranges
def get_speed_ranges():
    return info.SPEED_RANGES

#the heuristic function
def h(source, target):
    h =  convert_to_time(110,compute_distance(source.lat, source.lon, target.lat,target.lon))
    return h

#returns the time
def convert_to_time(speed_in_kmh, distance_in_km):
    return (distance_in_km / speed_in_kmh) * 60

#get the distance between two nodes
def get_link(node1, node2):
    #find the link with source of node 1 and target of node 2
    links = node1.links
    #iterate over the links and find the link with target of node 2
    for link in links:
        if link.target == get_node_index(node2):
            return link
        else:
            continue
#this adds the node to the path
def add_to_path(path, node):
    path.append(get_node_index(node))

#this runs a dfs. (psuedocode taken fro tutorial 3 slide 26)
def dfs_f(roads, current, target, f_limit, g, path):
   global new_limit
   new_f = g + h(current,target)
   #check of the limit is greater then tje previous one
   if new_f > f_limit:
       new_limit = min(new_limit, new_f)
       return None
   #if reached the goal state return
   if get_node_index(current) == get_node_index(target):
       return path ,g
   successors = get_successors(roads, current)
   #go through all of the successors
   for succ in successors:
       add_to_path(path, succ)
       link = get_link(current, succ)
       cost = get_cost(link.distance, road_speed(link.highway_type))
       total_cost =  cost + g
       sol = dfs_f(roads, succ, target, f_limit, total_cost, path)
       if(sol):
          return sol
       path.remove(get_node_index(succ))
   return None

#this returns the nodes index
def get_node_index(node):
    return node.index

#this returns the road speed allowed
def road_speed(road_type):
    return ways.info.SPEED_RANGES[road_type][1]

#this returns the cost calculated by distance/speed
def get_cost(distance, speed):
    return distance/speed

#returns all of the successors of a node
def get_successors(roads, current):
    successors = []
    for link in current.links:
        succ = Node(roads[getattr(link, "target")])
        successors.append(succ)
    return successors

#returns the source node info
def get_source_node(roads, source):
    return Node(roads[source])

#returns the target nodes info
def get_target_node(roads, target):
    return Node(roads[target])

#runs the ida main algorithm (psuedo code from tutorial 3 slide 25)
def run_ida(source, target, roads):
    resources_are_available = True
    global new_limit
    source = get_source_node(roads, source)
    target = get_target_node(roads, target)
    new_limit = h(source, target)
    path = [get_node_index(source)]
    while(resources_are_available):
        f_limit = new_limit
        #needs to be a global variable
        new_limit = math.inf
        sol = dfs_f(roads, source, target, f_limit, 0, path)
        if sol:
            return sol[0]
