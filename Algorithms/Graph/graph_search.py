""""

探索スタート地点を「探索候補スタック」に積む
while スタックが空っぽになるまで
    スタックから次の探索地点を1つ取り出す（pop）
    「探索済みリスト」に取り出した地点を格納（ここが現在地点）
　　現在地点から、次に行こうと思えば行けるポイントを全部探し出す
    for 地点 in 次に行こうと思えば行けるポイント
        if その地点は既に「探索済みリスト」にある？
            探索済みなので「探索候補スタック」には入れない（continue）
        if その地点は既に「探索候補スタック」にある？（閉路があるなら可能性あり、木なら可能性なし）
            探索予定なので「探索候補スタック」には入れない（continue）
        未探索かつ候補にも入っていない地点なので「探索候補スタック」に追加する（append）
print 探索済み地点

"""

from collections import deque

class Graph(object):
    graph = {}
    visited = {}
    route = []

    def __init__(self, g):
        self.graph = g

    def clear_params(self):
        self.visited = {}
        self.route = []

    def get_bfs_route(self, nodes, e_node):
        route = [e_node]
        parent = nodes[e_node]
        while parent!=-1:
            route.append(parent)
            parent = nodes[parent]
        return route[::-1]


    def bfs(self, s_node, e_node):
        self.visited = {s_node: -1}

        search_que = deque()
        search_que.append(s_node)

        count = 0

        while len(search_que)>0 or count > 100 :
            count += 1

            search_now = search_que.popleft()
            # debug
            #print(search_now)

            # stop search if reached goal
            if search_now == e_node:
                return self.get_bfs_route(self.visited, search_now)

            # search children
            for node in graph[search_now]:
                # already visited node?
                if node in self.visited:
                    continue
                else:
                    self.visited[node] = search_now

                # already in search list?
                if node in search_que:
                    continue
                else:
                    search_que.append(node)

        return []

    # post order dfs
    def dfs_stack(self, s_node, e_node):
        self.visited = {s_node: -1}

        search_stack = [s_node]

        while len(search_stack)>0:
            search_now = search_stack.pop()

            # stop search if reached goal
            if search_now == e_node:
                return self.get_bfs_route(self.visited, search_now)

            # add child to search_stack if never searched or visited
            children = self.graph[search_now]
            for child in children:
                if child in self.visited:
                    continue
                else:
                    self.visited[child] = search_now

                if child in search_stack:
                    continue
                else:
                    search_stack.append(child)

        return []

    # pre-order dfs
    def dfs_recursion(self, s_node, e_node, init=False):

        if init:
            self.visited = {s_node: -1}
            self.route = []

        if s_node == e_node:
            self.route = self.get_bfs_route(self.visited, s_node)
            return

        children = self.graph[s_node]
        if len(children)==0:
            return
        for child in children:
            if child in self.visited:
                continue
            else:
                self.visited[child] = s_node

            self.dfs_recursion(child, e_node)

        return





if __name__ =='__main__':

    n1 = [2, 4, 5]
    n2 = [3, 4, 6]
    n3 = [1, 2, 4]
    n4 = [1, 6]
    n5 = [2, 7]
    n6 = [3, 5]
    n7 = [2, 6]
    n8 = [9, 5]
    n9 = [8]

    graph = {1: n1, 2: n2, 3: n3, 4: n4, 5: n5, 6: n6, 7: n7, 8: n8, 9: n9}

    g = Graph(graph)

    #g.dfs_recursion(8, 5, True)
    #print('result:', g.route)


    for i in range(9):
        for j in range(9):
            s = i+1
            e = j+1
            print('\n==========================================================')
            print('BFS--- start:', s, ' end:', e, ' route:', g.bfs(s, e))
            print('DFS_stack --- start:', s, ' end:', e, ' route:', g.dfs_stack(s, e))
            g.dfs_recursion(s, e, True)
            print('DFS_recursion::: start:', s, ' end:', e, ' route:', g.route)


