class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        ls={"]":"[", "}":"{", ")":"("}
        for i in s:
            if i in ls.values():
                st.append(i)
            elif i in ls.keys():
                if len(st)!=0 and st[-1]==ls[i]:
                    st.pop()
                else:
                    return False

        return len(st)==0
