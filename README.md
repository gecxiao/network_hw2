# Network HW2-3

The hw for CSCI3390

## Getting Started
In the main.py, at the very bottom, there is a line
```
fh = open("test.edgelist.txt", 'rb')
```
Modify the text file to change the input.

The following functions are the implementation of the required functions:
```
bfs(G,s), ford_fulkerson_bfs(G, s, t)
```
The comment of the corresbonding lines gives explanation of which line inputs the psedocode.

## Running the tests
We assume '1' as the source and '2' as the sink. Call the function and print it will give the path. For example,
```
f=bfs(G, '1')
print(f)
```
Or if you want to see maxflow with BFS:
```
f=ford_fulkerson_bfs(G, '1', '2')
print(f)
```
Similarly, for the maxflow with dijkastra:
```
f=ford_fulkerson_dijkstra(G, '1', '2')
print(f)
```

## Benchmark result
In the run time png folder, there is a pdf file named Benchmarking Analysis that includes 8 figures with 4 different graphs: complete graph, star graph, barbell graph, and cycle graph.
The x-axis is the input size, and the y axis is the running time for two algorithms. The runtime of the maxflow algorithm with bfs and dijkstra varies with different graphs. According to the generated results, the runtime of the maxflow algorithm with bfs sometimes exceeds the one with dijkstra but sometimes don't. That's probably because complete graph is more complicated and we also assign random weights to nodes in graphs, which will affect the performance of dijkstra as seen by the graph that the runtime of algorithm with dijkstra tends to be unstable. But under all the other graphs (i.e. barbell, cycle, star graphs), maxflow algorithm implemented with dijkstra typically runs faster than the one with bfs.
The more detailed data can be found in the ```running time.xlsx``` file.
## Authors

* **Suichong (Kyle) Chen** 
* **Chengxiao (Gary) Ge** 
* **Yindong Sun** 

