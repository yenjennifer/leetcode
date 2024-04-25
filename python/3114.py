s = "?2:2?"

k = ''

if s[0] == '?':
    if s[1]!='?' and int(s[1]) >=2:
        k+='0'
    else:
        k+='1'
else:
    k+=s[0]

if s[1] == '?':

    if k[0] == '0':
        k+='9'
    elif k[0] == '1':
        k+='1'
else:
    k += s[1]

k+=':'
if s[3] == '?':
    k+='5'
else:
    k+=s[3]
if s[4] == '?':
    k+='9'
else:
    k+= s[4]

print(k)