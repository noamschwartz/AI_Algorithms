from ways import load_map_from_csv
import random
import csv

if __name__ == '__main__':
    #load map
    roads = load_map_from_csv()
    file = "problemss.csv"
    pair = []
    #get 100 problems
    for i in range(100):
        #get first junction
        start = roads[random.randint(0, len(roads))]
        curr = start
        #get only between 10 to 50 in distance
        for j in range(random.randint(10, 50)):
            links = list(getattr(curr, "links"))
            next = links[random.randint(0, len(links) - 1)].target
            curr = roads[next]
        pair.append([start.index, ' ' + str(curr.index)])
    #finally write to the file
    with open(file, 'w+', newline='') as problems_file:
        writer = csv.writer(problems_file)
        writer.writerows(pair)
    problems_file.close()
