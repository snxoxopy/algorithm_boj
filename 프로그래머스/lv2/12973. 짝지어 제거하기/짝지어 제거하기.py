def solution(s):
    answer = 0
    st = []
    for c in s:
        if not st:
            st.append(c)
        else:
            if c == st[-1]:
                st.pop()
            else:
                st.append(c)
    answer = 0 if st else 1
    return answer