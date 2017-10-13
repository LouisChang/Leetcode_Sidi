/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        map <int,int> m;
        for (auto i:intervals){
            m[i.start]++;
            m[i.end]--;
        }
        int total, res;
        total = res = 0;
        
        for (auto j:m){
            total += j.second;
            res = max(total,res);
        }
        return res;
        }
};
