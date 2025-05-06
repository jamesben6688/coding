class Solution:
    def replace(self, s, d):
        s = s.strip("%")
        candidates = s.split("%")
        loops = set()
        path = set()

        def replace(x):
            if x not in d:
                return x
            if x in path:
                loops.union(set(path))
                return "recursive"
            path.add(x)
            # loops.add(x)
            return replace(d[x])

        ans = ""
        for c in candidates:
            path.clear()
            if c in d:
                ans += replace(c) + " "
            elif c in loops:
                ans += "recursive "
            else:
                ans += c + " "

        return ans


print(Solution().replace(
"%FIRSTNAME% %LASTNAME%",
    {
        "FIRSTNAME" : "Bill",
        "LASTNAME" : "Gates"
    }
))

print(Solution().replace(
    "%ONE%TWO%",
    {
        "ONE" : "TWO",
        "TWO" : "THREE",
        "THREE" :"ONE"
    }
))

# print(Solution().replace("%x%a%y%", {"x": "y", "y": "z", "z": "y"}))
