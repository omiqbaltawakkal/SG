class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}
    return self
 
  def add_node(self, value):
    self.nodes.add(value)
    return self
 
  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
    return self
 
 
def dijsktra(Graph, initial):
  visited = {initial: 0}
  path = {}
 
  nodes = set(Graph.nodes)
 
  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node
 
    if min_node is None:
      break
 
    nodes.remove(min_node)
    current_weight = visited[min_node]
 
    for edge in Graph.edges[min_node]:
      try:
        weight = current_weight + graph.distance[(min_node, edge)]
      except:
        continue
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node
 
  return visited, path

g=Graph()
g.add_node('A')
g.add_node('B')
g.add_node('C')

g.add_edge('A','B',7)
g.add_edge('A','C',8)
g.add_edge('B','C',2)

print Graph()
#print dijsktra(g,'A','C')
