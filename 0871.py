# Solution 1 - Greedy


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        store = []
        count = 0
        fuel = startFuel
        stations.append([target, 0])
        for i in range(len(stations)):
            while fuel < stations[i][0]:
                if not store:
                    return -1
                fuel += max(store)
                store.remove(max(store))
                count += 1
            heapq.heappush(store, stations[i][1])
        return count

#TODO: Solution 2 - Dynamic Programming


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
