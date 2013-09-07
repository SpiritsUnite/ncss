from lookup import *

g = Graph('a', 'graph.txt')
a = g.get_node('3')
g.output()

def out(x):
    print("\n".join(map(str, x)))
    print()

out(g.graph_search(a, "NEIGHBOURS WHO HAVE LABEL e"))
out(g.graph_search(a, "NEIGHBOURS WHO HAVE LABEL f"))

out(g.graph_search(a, "NEIGHBOURS WHO HAVE NEIGHBOUR LABEL connects"))
out(g.graph_search(a, "NEIGHBOURS WHO HAVE NEIGHBOUR LABEL aoeu"))

out(g.graph_search(a, "NEIGHBOURS WHO HAVE EXACTLY 1 NEIGHBOURS"))
out(g.graph_search(a, "NEIGHBOURS WHO HAVE EXACTLY 0 NEIGHBOURS"))
out(g.graph_search(a, "NEIGHBOURS WHO HAVE EXACTLY 2 NEIGHBOURS"))
out(g.graph_search(a, "NEIGHBOURS WHO HAVE MORE THAN 1 NEIGHBOURS"))
out(g.graph_search(a, "NEIGHBOURS WHO HAVE MORE THAN 0 NEIGHBOURS"))
out(g.graph_search(a, "NEIGHBOURS WHO HAVE MORE THAN -1 NEIGHBOURS"))
out(g.graph_search(a, "NEIGHBOURS WHO HAVE LESS THAN 0 NEIGHBOURS"))
out(g.graph_search(a, "NEIGHBOURS WHO HAVE LESS THAN 1 NEIGHBOURS"))
out(g.graph_search(a, "NEIGHBOURS WHO HAVE LESS THAN 2 NEIGHBOURS"))

out(g.graph_search(a, "NEIGHBOURS WHO HAVE LESS THAN 1 NEIGHBOURS WITH LABEL connects"))
out(g.graph_search(a, "NEIGHBOURS WHO HAVE LESS THAN 1 NEIGHBOURS WITH LABEL conects"))
out(g.graph_search(a, "NEIGHBOURS WHO HAVE MORE THAN 0 NEIGHBOURS WITH LABEL conects"))
out(g.graph_search(a, "NEIGHBOURS WHO HAVE MORE THAN 0 NEIGHBOURS WITH LABEL connects"))

out(g.graph_search(a, "NEIGHBOURS WHO HAVE NEIGHBOUR LABEL connects AND MORE THAN 0 NEIGHBOURS"))
