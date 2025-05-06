from typing import List


class Solution:
    def format_str(self, strs: List[str], mx_len):
        ans = [""]
        for s in strs:
            if len(ans[-1]) + len(s) <= mx_len:
                if ans[-1] == "":
                    ans[-1] += s
                else:
                    ans[-1] += " " + s
            else:
                ans.append(s)
        return ans


print(Solution().format_str(
["IsAudioBuffer", "GetTimestamp", "SetTimestamp", "GetSampleRate", "GetSampleSize", "GetNumberOfChannels",
"GetNumberOfSamples", "GetDataBuffer", "GetChannel"], 70
))