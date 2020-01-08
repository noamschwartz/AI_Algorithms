import ways
from collections import namedtuple
from pqdict import pqdict
Node = namedtuple('Node', ['junction', 'prev', 'distance'])

#build the path from the target to the beginnig in reverse order
def build_path(target):
    current = target
    nodes = list()
    while current is not None:
        nodes.append(current.junction.index)
        current = current.prev
    nodes.reverse()
    return nodes

#get the speed allowed in the road (upper bound)
def road_speed(road_type):
    # Returns the average speed for the road type.
    return ways.info.SPEED_RANGES[road_type][1]

#update the distance in the closed list
def update_distance_in_closed(open, closed,junctions, link, current, cost, succ ):
    temp = Node(get_target(junctions, link), current, cost)
    del closed[get_succ_index(succ)]
    add_to_open(open, temp)

#make the pq a min heap
def min(first, second):
    return first.distance < second.distance

#get the index of a speficic node
def get_node_index(node):
    return node.junction.index

#ge tthe cost of the link.
def get_cost(distance, speed):
    return distance/speed

#add a node to the closed list
def add_to_close(closed, index, node_to_Add):
    closed[index] = node_to_Add

#add a node to the open pq
def add_to_open(open,node):
    open.additem(node.junction.index, node)

#get a single node from the top of the pq
def pop_node(open):
    return open.popitem()[1]

#get the target node
def get_target(junctions,link):
    return junctions[link.target]

#update the distance in the open pq
def update_node_distance(open, junctions, link, current, cost, succ ):
    temp = Node(get_target(junctions, link), current, cost)
    open.updateitem(get_succ_index(succ), temp)

#get the index of a successer
def get_succ_index(succ):
    return succ.index

def run_ucs(source, target, roads):
    junctions = roads.junctions()
    source_node_info = junctions[source]
    closed = dict()
    open = pqdict(precedes= min)
    #add first node with parent of null and distance 0
    open.additem(source, Node(source_node_info, None, 0))
    while open is not None:
        current = pop_node(open)
        add_to_close(closed, get_node_index(current), current)
        #if final node reached
        if get_node_index(current) == target:
            return build_path(current)
        #ireate over all links
        links = current.junction.links
        for link in links:
            succ = get_target(junctions,link)
            cost = get_cost(link.distance, road_speed(link.highway_type)) + current.distance
            if get_succ_index(succ) in open.keys():
                if open[get_succ_index(succ)].distance > cost:
                    update_node_distance(open, junctions, link, current, cost, succ)
                continue
            if get_succ_index(succ) in closed:
                if closed[get_succ_index(succ)].distance > cost:
                    update_distance_in_closed(open, closed, junctions, link, current, cost, succ)
                continue
            add_to_open(open,Node(get_target(junctions,link), current, cost))
    return None
