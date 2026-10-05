class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st=[]
        c=0
        for i in s:
            if i=='(':
                st.append(c)
                c=0
            else:
                c=st.pop()+max(c*2,1)
        return c