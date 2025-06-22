class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        right = ['(','[','{']
        
        l = len(s)
        ok =l%2==0 and s[0] in right
        while ok and s!="":
            i=0
            while s[i+1] in right:
                i+=1

            if s[i]=='(':
                ok= s[i+1]==')'
            elif s[i]=='{':
                ok = s[i+1]=='}'
            elif s[i]=='[':
                ok = s[i+1]==']'
            else: ok = False
        if ok ==False: return ok
        s = s[:i]+s[i+2:]
        return ok


            
