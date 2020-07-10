# dijakstra's algorithm to find shortest path.

def dijaktra(l,start, goal):
    unseenNodes= l
    shortest_distance={}
    predecessor= {}
    infinity= 99999999
    path=[]

    for node in unseenNodes:
        shortest_distance[node]=infinity
    shortest_distance[start]=0
    
    while unseenNodes:
        minNode= None
        for node in unseenNodes:
            if minNode is None:
                minNode= node
            
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode=node

        for childNode, weight in l[minNode].items():
            if shortest_distance[minNode] + weight < shortest_distance[childNode]:
                shortest_distance[childNode]= shortest_distance[minNode] + weight 
                predecessor[childNode]= minNode
        
        unseenNodes.pop(minNode)

    currentNode= goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode= predecessor[currentNode]
        except KeyError:
            print("Path doesnot exit")
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        return (f"shortest distance: {shortest_distance[goal]} and path:{path}")
    return path


            



l={'a':{'b':1,'c':3},'b':{'c':5,'d':2},'c':{'d':1,'e':3},'d':{'e':3},'e':{}}
print(dijaktra(l,'a','d'))