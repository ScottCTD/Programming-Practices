# 1396. Design Underground System
# Medium
# An underground railway system is keeping track of customer travel times between different
# stations. They are using this data to calculate the average time it takes to travel from one
# station to another.
#
# Implement the UndergroundSystem class:
#
# void checkIn(int id, string stationName, int t)
# A customer with a card ID equal to id, checks in at the station stationName at time t.
# A customer can only be checked into one place at a time.
# void checkOut(int id, string stationName, int t)
# A customer with a card ID equal to id, checks out from the station stationName at time t.
# double getAverageTime(string startStation, string endStation)
# Returns the average time it takes to travel from startStation to endStation.
# The average time is computed from all the previous traveling times from startStation to
# endStation that happened directly, meaning a check in at startStation followed by a check out
# from endStation.
# The time it takes to travel from startStation to endStation may be different from the time it
# takes to travel from endStation to startStation.
# There will be at least one customer that has traveled from startStation to endStation before
# getAverageTime is called.
# You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks
# in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.

# 2023-05-30 20:48:47
# original
# time 67.51% space 27.44%
class UndergroundSystem:

    def __init__(self):
        self.p = {}
        self.avg = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.p:
            self.p[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.p:
            ss, st = self.p[id]
            path = (ss, stationName)
            diff = t - st
            if path in self.avg:
                self.avg[path][0] += diff
                self.avg[path][1] += 1
            else:
                self.avg[path] = [diff, 1]
            self.p.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        diff, t = self.avg[(startStation, endStation)]
        return diff / t


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)