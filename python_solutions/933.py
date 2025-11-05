# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

 

# Example 1:

# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]

# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

class RecentCounter:

    def __init__(self):
        self.recent_requests = []
    def ping(self, t: int) -> int:
        # Smart thing to do is when adding, remove the requests from start, so that it is easier to find the latest ones.
        # Append
        self.recent_requests.append(t)
        #if t -3000 > request, delete it from the list
        while self.recent_requests and self.recent_requests[0] < t - 3000:
            self.recent_requests.pop(0)
        return len(self.recent_requests)    



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
if __name__ == "__main__":
    sol = RecentCounter()

    # [[],[642],[1849],[4921],[5936],[5957]]
    print(sol.ping(642))     # requests = [1], range is [-2999,1], return 1
    print(sol.ping(1849))   # requests = [1, 100], range is [-2900,100], return 2
    print(sol.ping(4921))  # requests = [1, 100, 3001], range is [1,3001], return 3
    print(sol.ping(5936))  # requests = [1, 100, 3001, 3002], range is [2,3002], return 3   
    print(sol.ping(5957))  # requests = [1, 100, 3001, 3002], range is [2,3002], return 3