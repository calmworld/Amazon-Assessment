# Time: O(N)
# Space: O(1) [for variable character language of size M it would be O(M)]
def passwordStrength(password):
    last = {chr(97 + i): -1 for i in range(26)}
    ret = 0
    for i,ch in enumerate(password):
        left = i - last[ch]
        right = len(password) - i
        ret += left * right
        last[ch] = i
        
    return ret
  
  
  
  #
  #https://leetcode.com/discuss/interview-question/1526418/Count-strength-of-pa%20%20ssword-or-amazon
  #
