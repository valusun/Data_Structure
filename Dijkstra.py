from dataclasses import dataclass, field
from heapq import heappop, heappush


@dataclass
class Dijkstra:
    vertex_cnt: int
    edge_cnt: int
    # [cost, vertex]
    graph: list[list[int]] = field(default_factory=list)
    INF: int = 10**10

    def GetShortestPaths(self, start: int) -> list[int]:
        """各辺の最短経路を求める"""

        dist = [self.INF] * self.vertex_cnt
        done = [False] * self.vertex_cnt
        cost_and_vertex = [(0, start)]
        dist[start] = 0
        while cost_and_vertex:
            cost, vertex = heappop(cost_and_vertex)
            if done[vertex]:
                continue
            for next_cost, next_vertex in self.graph[vertex]:
                all_cost = cost + next_cost
                if all_cost < dist[next_vertex]:
                    dist[next_vertex] = all_cost
                    heappush(cost_and_vertex, (all_cost, next_vertex))
            done[vertex] = True
        return dist

    # TODO: 経路復元
    # distをどう持つかが課題
    # -> __post_init__で持ってしまうと、Get~の実行時に毎回初期化処理を噛ませる必要がある
    # ていうか、そもそも最短経路と経路復元を一緒に返してしまえば良さそう
    # -> 受け取るときに要らなければ"_"で明記できるし
    # それなら関数化で良さそう...


# 最終的にはなくなる -> デバッグ用
def main():
    # https://algo-method.com/tasks/1008
    N, M = map(int, input().split())
    Graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v, c = map(int, input().split())
        Graph[u].append([c, v])
    dijkstra = Dijkstra(N, M, Graph)
    print(*dijkstra.GetShortestPaths(0), sep="\n")


if __name__ == "__main__":
    main()
