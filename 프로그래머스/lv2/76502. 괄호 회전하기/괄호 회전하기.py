def solution(s):
    answer = 0
    
    def is_parensis(s):
        st = []
        len_s = len(s)
        # print(len_s)
        paren = {'[': 1, '{': 2, '(': 3, ')': 4, '}':5, ']': 6}
        # for idx in range(1, len_s):
        #     if st:
        #         if (paren[s[idx]] > paren[s[idx - 1]]) and (paren[s[idx]] + paren[s[idx - 1]] == 7):
        #             st.pop()
        #     else:
        #         st.append(s[idx])
        
        for c in s:
            if 0 < paren[c] < 4: st.append(c)
            else:
                if not st: return False
                pre = st.pop()
                if paren[pre] + paren[c] != 7:
                    return False
                    
        # print(st)
        if st:
            return False
        return True
    
    # rotate_s
    for start in range(len(s)):
        tmp_s = str()
        # print("TC#", start)
        for i in range(start, start + len(s), 1):
            i %= len(s)
            tmp_s += s[i]
        # print(tmp_s)
        if is_parensis(tmp_s):
            answer += 1
            

    return answer