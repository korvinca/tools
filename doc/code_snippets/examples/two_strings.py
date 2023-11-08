template = "bcde"
data = "bcssbttacadcde"
#output = "bbcccddessttaa"
m_data = {}

for l in template:
    count = 0
    for d in data:
        if d == l:
            count += 1
            m_data[d] = count

for i in data:
    if i not in template:
        if i in m_data:
            m_data[i] = m_data[i] + 1
        else:
            m_data[i] = 1

print(str(m_data))

for k in m_data:
    print(k * m_data[k], end = "")
print()