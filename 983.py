class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1] + 1
        spend = [float("inf")] * (last_day)
        spend[0] = 0
        day_num = 1

        for day in days:
            while day_num != day:
                spend[day_num] = spend[day_num - 1]
                day_num += 1
            assert (day_num == day)
            week_ago = max(0, day_num - 7)
            month_ago = max(0, day_num - 30)
            spend[day_num] = min(spend[day_num - 1] + costs[0], spend[week_ago] + costs[1], spend[month_ago] + costs[2])
            day_num += 1
        
        return spend[-1]
