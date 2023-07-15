# Python3.8.2を基準に書いているので、型記法が古いです

import heapq
from collections import Counter
from typing import Optional, Union, List


class DeletableHeapq:
    def __init__(self):
        self.elm_counter = Counter()
        self.max_pop_heapq = []  # heappopしたときに、最大値を取得するheapq
        self.min_pop_heapq = []  # heappopしたときに、最小値を取得するheapq
        self._sum = 0

    def _to_list(self, num: Union[int, List[int]]) -> List[int]:
        """リスト型に変換する"""
        return num if isinstance(num, list) else [num]

    def add(self, num: Union[int, List[int]]) -> None:
        """要素を追加する"""
        nums = self._to_list(num)
        for n in nums:
            self.elm_counter[n] += 1
            self._sum += n
            heapq.heappush(self.max_pop_heapq, -n)
            heapq.heappush(self.min_pop_heapq, n)

    def erase(self, num: Union[int, List[int]]) -> None:
        """要素を削除する"""
        nums = self._to_list(num)
        for n in nums:
            if not self.elm_counter[n]:
                raise KeyError(n)
            self.elm_counter[n] -= 1
            if self.elm_counter[n] == 0:
                del self.elm_counter[n]
            self._sum -= n

    def get_max(self) -> Optional[int]:
        """要素内に存在する値の最大値を返す

        Notes:
            - 要素がない場合は`None`を返す
        """
        if len(self.elm_counter) == 0:
            return None
        p = abs(heapq.heappop(self.max_pop_heapq))
        while p not in self.elm_counter:
            p = abs(heapq.heappop(self.max_pop_heapq))
        heapq.heappush(self.max_pop_heapq, -p)
        return p

    def get_min(self) -> Optional[int]:
        """要素内に存在する値の最小値を返す

        Notes:
            - 要素がない場合は`None`を返す
        """
        if len(self.elm_counter) == 0:
            return None
        p = heapq.heappop(self.min_pop_heapq)
        while p not in self.elm_counter:
            p = heapq.heappop(self.min_pop_heapq)
        heapq.heappush(self.min_pop_heapq, p)
        return p

    def pop_max(self) -> Optional[int]:
        """要素内の最大値を取り出す

        Notes:
            要素がない場合は`None`を返す
        """

        if (p := self.get_max()) is None:
            return None
        self.erase(p)
        return p

    def pop_min(self) -> Optional[int]:
        """要素内の最大値を取り出す

        Notes:
            要素がない場合は`None`を返す
        """
        if (p := self.get_min()) is None:
            return None
        self.erase(p)
        return p

    def get_sum(self) -> int:
        """要素内の合計値を返す"""
        return self._sum

    def __contains__(self, num):
        return num in self.elm_counter
