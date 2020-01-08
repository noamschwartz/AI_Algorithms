'accessible using "import ways.draw"'
from ways import info, graph

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError('Please install matplotlib:  http://matplotlib.org/users/installing.html#windows')

plt.axis('equal')


def plot_path(roads, path, color='g'):
    '''path is a list of junction-ids - keys in the dictionary.
    e.g. [0, 33, 54, 60]
    Don't forget plt.show()'''
    flons, tolons, flats, tolats = [] ,[] ,[] ,[]
    for s, t in zip(path[:-1], path[1:]):
        ps, pt = roads[s], roads[t]
        flons.append(ps.lon)
        tolons.append(pt.lon)
        flats.append(ps.lat)
        tolats.append(pt.lat)
    plt.plot(flons, flats, tolons, tolats, color)
    plt.show()

def set_no_axis():
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)


def draw_links(roads, count=1000, types=list(range(len(info.ROAD_TYPES)))):
    lons, lats = [], []
    for link in roads.iterlinks():
        if link.highway_type not in types: ## not sure why we don't just do link.highway_type < # of types...
            continue
        src = roads[link.source]
        dst = roads[link.target]
        lons.append([src.lon, dst.lon])
        lats.append([src.lat, dst.lat])
    plt.plot(lons, lats, str(1 - 1.0 / (types[0] + 1)), zorder=14 - types[0])


if __name__ == '__main__':
    def _draw_stuff():
        # plt.figure(num=1, figsize=(6, 15))
        # set_no_axis()
        roads = graph.load_map_from_csv()#count=10001)
        # draw_links(roads)
        plot_path(roads, [526042, 526043, 526037, 526038, 526039, 526035, 526036, 532733], color='g')
        plot_path(roads, [699810, 575295, 25986 ,25987, 25988, 25989 ,25990 ,25991, 25992, 25993, 25994, 25995, 25996, 25997, 25998, 479318, 479319, 479320, 479321, 528129, 528130], color='b')
        plot_path(roads, [606508, 750874, 936428, 706481, 706482, 706483, 706484, 706485, 706486, 706487, 605954, 706488, 706489, 706490, 29232], color='y')
        plot_path(roads, [863616, 863617, 863618, 863619, 863620, 863621, 863622, 863623, 863624, 863625, 863626, 863627, 863628, 863629, 863630, 654126, 654127, 654128, 654129] , color='r')
        plot_path(roads,[  944324, 944325, 944326, 810808, 810809, 944336, 944335, 944334, 944333  ], color='b')
        plot_path(roads, [ 873438, 873465, 873466, 873467, 873468 ,873469, 873470 ,873471 ,871938, 871954 ,535091, 871943 ,871944, 690, 871945, 540702 ,537833 ,540703, 540704, 540705, 540706  ], color='g')
        plot_path(roads, [ 12348, 12349 ,12350, 12351 ,12352, 12353, 12354 ,612786, 612787 ,612788, 612789 ,612790, 19514 ,612791, 555744, 612792 ,612793, 612794 ,612795, 612796 ,612797     ], color='y')
        plot_path(roads, [529462, 529463, 529464, 529465, 529466 ,529467 ,529468, 529469 ,529470, 529471, 529472, 529473, 529474 ,529475, 529476, 529477, 530468, 530469, 530470, 530471, 530472      ], color='b')
        plot_path(roads, [  659021, 659022 ,659023, 659024, 659025 ,659026, 659027    ], color='r')
        plot_path(roads, [ 342487, 342488 ,342489 ,342490 ,342491, 342492, 342493    ], color='r')


        plt.show()

    _draw_stuff()




