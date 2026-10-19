import networkx
import matplotlib.pyplot

G = networkx.Graph()

print("Добавьте вершины (пустая строка - закончить):")
while True:
    v = input("Вершина: ").strip()
    if v == "":
        break
    G.add_node(v)

print("Добавьте рёбра в формате 'A B' (пустая строка - закончить):")
while True:
    r = input("Ребро: ").split()
    if not r:
        break
    if len(r) != 2:
        print("Нужно ввести две вершины через пробел")
        continue
    a, b = r
    if a not in G or b not in G:
        print("Такой вершины нет, сначала добавьте её")
        continue
    G.add_edge(a, b)

print("Вершины:", list(G))
print("Рёбра:", list(G.edges))
print("Количество вершин:", G.number_of_nodes())
print("Количество рёбер:", G.number_of_edges())
print("Степени вершин:", dict(G.degree))

networkx.draw(G, with_labels=True)
matplotlib.pyplot.show()
