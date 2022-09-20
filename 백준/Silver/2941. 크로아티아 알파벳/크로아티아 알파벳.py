c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
st = input()

for i in c:
    st = st.replace(i, '*')
print(len(st))