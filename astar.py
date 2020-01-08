from collections import namedtuple
import ways
from ways import compute_distance
from pqdict import pqdict
Node = namedtuple('Node', ['junction', 'prev', 'distance', 'heuristic', 'order', ])
#return the path backwards from the target functuon
def build_path(target):
    current = target
    nodes = list()
    while current is not None:
        nodes.append(current.junction.index)
        current = current.prev
    nodes.reverse()
    return nodes

#make the heap a min heap
def min(first, second):
    return first.order < second.order

#returns the time
def convert_to_time(speed_in_kmh, distance_in_km):
    return (distance_in_km / speed_in_kmh) * 60

#the heuristic function
def h(source, target):
    h =  convert_to_time(110,compute_distance(source.lat, source.lon, target.lat,target.lon))
    return h

#get the target
def get_target(junctions,link ):
    return junctions[link.target]

#pop a node from the priority queue
def pop_node(open):
    return open.popitem()[1]

#find the nodes index
def get_node_index(node):
    return node.junction.index

#find the road speed allowed (upper bound)
def road_speed(road_type):
    return ways.info.SPEED_RANGES[road_type][1]

#get the index of the succeser
def get_succ_index(succ):
    return succ.index

#get the cost calculated by distance divided by speed
def get_cost(distance, speed):
    return distance/speed

#update the distance in the open and closed lists
def update_distance(open, closed,succ,current,cost, heuristic_cost):
    temp = Node(succ, current, cost, heuristic_cost,
                    heuristic_cost + cost)
    del closed[get_succ_index(succ)]
    open.additem(temp.junction.index, temp)

#update the distanec on the lists
def update_node_distance(open,succ, current, cost, heuristic_cost):
    temp = Node(succ, current, cost, heuristic_cost, heuristic_cost + cost)
    open.updateitem(get_succ_index(succ), temp)

#add new node to the open pq
def add_to_open(open,succ,current ,cost, heuristic_cost ):
    open.additem(get_succ_index(succ), Node(succ, current, cost, heuristic_cost, cost + heuristic_cost))

#add a node to the closed list
def add_to_close(closed, index, node_to_Add):
    closed[index] = node_to_Add

#the main Astar algorithm
def run_astar(source, target, roads):
    junctions = roads.junctions()
    source_node_info = junctions[source]
    target_node_info = junctions[target]
    closed = dict()
    open = pqdict(precedes=min)
    heuristic = h
    # add first node with parent of null and distance 0
    open.additem(source, Node(source_node_info, None, 0,heuristic(source_node_info, target_node_info),
                              heuristic(source_node_info, target_node_info)))
    while open is not None:
        current = pop_node(open)
        add_to_close(closed, get_node_index(current), current)
        # if final node reached
        if get_node_index(current) == target:
            return build_path(current)
        links = current.junction.links
        for link in links:
            succ = get_target(junctions,link)
            cost = get_cost(link.distance, road_speed(link.highway_type)) + current.distance
            heuristic_cost = heuristic(succ, target_node_info)
            if get_succ_index(succ) in open.keys():
                if open[get_succ_index(succ)].distance > cost:
                    update_node_distance(open, succ, current, cost, heuristic_cost)
                continue
            if get_succ_index(succ) in closed:
                if closed[get_succ_index(succ)].distance > cost:
                    update_distance(open, closed, succ, current, cost, heuristic_cost)
                continue
            add_to_open(open,succ,current ,cost, heuristic_cost)
    return None



