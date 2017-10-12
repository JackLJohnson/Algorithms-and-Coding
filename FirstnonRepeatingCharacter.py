def firstNotRepeatingCharacter(s):
    store = set()
    track = {}
    if len(s)==0:
        return None
    else:
        for x in s:
            if x not in store:
                store.add(x)
            else:
                if x not in track:
                    track[x]=1
                else:
                    track[x]+=1
    res = list(store-set(track.keys()))
    val = [s.index(x) for x in res]
    if len(res)!=0:
        idx=(min(val))
        return s[idx]
    else:
        return "_"
