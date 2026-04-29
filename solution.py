class Solution:
    def countSeniors(self, details):
        sc = 0
        for p in details:
            if int(p[11:13]) > 60: sc += 1
        
        return sc
