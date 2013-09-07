from lookup import *

g = Graph('a', 'grap.txt')
a = g.get_node('0')
b = g.get_node('1')
c = g.get_node('2')
d = g.get_node('3')
e = g.get_node('4')
g.output()

def out(x):
    print("\n".join(map(str, x)))
    print()

#out(g.graph_search(a, "NEIGHBOURS WHO HAVE LABEL John"))
#out(g.graph_search(a, "NEIGHBOURS WHO HAVE LABEL Greg"))

#out(g.graph_search(a, "NEIGHBOURS WHO HAVE NEIGHBOUR LABEL son"))
#out(g.graph_search(a, "NEIGHBOURS WHO HAVE NEIGHBOUR LABEL wife"))

#out(g.graph_search(a, "NEIGHBOURS WHO HAVE EXACTLY 4 NEIGHBOURS"))
#out(g.graph_search(a, "NEIGHBOURS WHO HAVE EXACTLY 0 NEIGHBOURS"))
#out(g.graph_search(a, "NEIGHBOURS WHO HAVE EXACTLY 3 NEIGHBOURS"))
#out(g.graph_search(a, "NEIGHBOURS WHO HAVE MORE THAN 3 NEIGHBOURS"))
#out(g.graph_search(a, "NEIGHBOURS WHO HAVE MORE THAN 0 NEIGHBOURS"))
#out(g.graph_search(a, "NEIGHBOURS WHO HAVE MORE THAN -1 NEIGHBOURS"))
#out(g.graph_search(a, "NEIGHBOURS WHO HAVE LESS THAN 0 NEIGHBOURS"))
#out(g.graph_search(a, "NEIGHBOURS WHO HAVE LESS THAN 1 NEIGHBOURS"))
#out(g.graph_search(a, "NEIGHBOURS WHO HAVE LESS THAN 2 NEIGHBOURS"))

#out(g.graph_search(a, "NEIGHBOURS WHO HAVE LESS THAN 3 NEIGHBOURS WITH LABEL son"))
#out(g.graph_search(a, "NEIGHBOURS WHO HAVE MORE THAN 1 NEIGHBOURS WITH LABEL son"))

#out(g.graph_search(a, "NEIGHBOURS WHO HAVE NEIGHBOUR LABEL son AND MORE THAN 3 NEIGHBOURS"))

#out(g.graph_search(c, "NEIGHBOURS WHO HAVE ( EXACTLY 1 NEIGHBOURS WITH LABEL father OR LABEL Bob ) AND LESS THAN 4 NEIGHBOURS"))

out(g.graph_search(c, "PEOPLE WHO HAVE ( MORE THAN 3 NEIGHBOURS )"))
#out(g.graph_search(e, "PEOPLE WHO HAVE LESS THAN 1 NEIGHBOURS WITH LABEL father AND 2 DEGREES OF SEPARATION FROM ME"))
