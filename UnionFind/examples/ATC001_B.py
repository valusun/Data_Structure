class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parents = [None] * n
        self.ranks = [0] * n

    def union(self, x: int, y: int) -> None:
        """要素xが属する木と要素yが属する木の結合を行う"""
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.ranks[x_root] < self.ranks[y_root]:
            self.parents[x_root] = y_root
        else:
            self.parents[y_root] = x_root
            if self.ranks[x_root] == self.ranks[y_root]:
                self.ranks[x_root] += 1

    def find(self, x: int) -> int:
        """その要素が属する木の根の要素番号を返す"""
        if self.parents[x] is None:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def is_same(self, x: int, y: int) -> bool:
        """要素xと要素yが同じ木に属している場合`True`を返す"""
        return self.find(x) == self.find(y)

    def get_roots(self):
        """根の要素番号を返す"""
        return [idx for idx in self.parents if idx is None]

    def get_members(self, x: int):
        """要素xに属している木の要素番号を返す"""
        r = self.find(x)
        return [idx for idx in self.parents if self.find(idx) == r]

    def get_size(self, x: int) -> int:
        """要素xが属している木のサイズを返す"""
        return len(self.get_members(x))

    def __len__(self) -> int:
        """要素数を返す"""
        return self.n


def main():
    N, Q = map(int, input().split())
    UF = UnionFind(N)
    for _ in range(Q):
        p, a, b = map(int, input().split())
        if p == 0:
            UF.union(a, b)
        else:
            print("Yes" if UF.is_same(a, b) else "No")


if __name__ == "__main__":
    main()
