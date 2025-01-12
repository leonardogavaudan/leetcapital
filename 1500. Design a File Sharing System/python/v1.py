import heapq
from collections import defaultdict
from typing import List


class FileSharing:
    def __init__(self, m: int):
        self.user_id_heap = list(range(1, 10**4 + 1))
        heapq.heapify(self.user_id_heap)
        self.user_id_to_chunk = defaultdict(set)
        self.user_id_to_chunk_unprocessed = defaultdict(list)
        self.chunk_to_user_id = defaultdict(set)

    def join(self, ownedChunks: List[int]) -> int:
        new_user_id = heapq.heappop(self.user_id_heap)
        self.user_id_to_chunk_unprocessed[new_user_id] = ownedChunks
        return new_user_id

    def leave(self, userID: int) -> None:
        self.user_id_to_chunk_unprocessed[userID] = []
        for chunk in self.user_id_to_chunk[userID]:
            self.chunk_to_user_id[chunk].remove(userID)
        self.user_id_to_chunk[userID] = set()
        heapq.heappush(self.user_id_heap, userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        for user_id, unprocessed_chunk_ids in self.user_id_to_chunk_unprocessed.items():
            self.user_id_to_chunk[user_id] = set(unprocessed_chunk_ids)
            for unprocessed_chunk_id in unprocessed_chunk_ids:
                self.chunk_to_user_id[unprocessed_chunk_id].add(user_id)
        self.user_id_to_chunk_unprocessed = defaultdict(set)

        res = sorted(list(self.chunk_to_user_id[chunkID]))
        if res:
            self.user_id_to_chunk[userID].add(chunkID)
            self.chunk_to_user_id[chunkID].add(userID)
        return res
