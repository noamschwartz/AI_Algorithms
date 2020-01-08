
#do NOT import ways. This should be done from other files
#simply import your modules and call the appropriate functions
from ucs import run_ucs
from astar import run_astar
from idastar import run_ida
from ways import load_map_from_csv


def find_ucs_rout(source, target, roads):
    return run_ucs(source,target, roads)

def find_astar_route(source, target, roads):
    return run_astar(source, target, roads)

def find_idastar_route(source, target, roads):
    return run_ida(source, target, roads)

def dispatch(argv):
    from sys import argv
    source, target = int(argv[2]), int(argv[3])
    if argv[1] == 'ucs':
        roads = load_map_from_csv()
        path = find_ucs_rout(source, target, roads)
    elif argv[1] == 'astar':
        roads = load_map_from_csv()
        path = find_astar_route(source, target,roads)
    elif argv[1] == 'idastar':
        roads = load_map_from_csv()
        path = find_idastar_route(source, target, roads)
    if path is not None:
        print(' '.join(str(j) for j in path))
    else:
        return 0


if __name__ == '__main__':
    from sys import argv
    dispatch(argv)
