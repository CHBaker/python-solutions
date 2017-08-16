from itertools import permutations

def question1(s, t):
    if not s or not t or type(s) is not str or type(t) is not str or len(t) > len(s):
        return False
    s = s.lower()
    t = t.lower()
    t = [''.join(p) for p in permutations(t)]
    print t
    for i in t:
        if i in s:
            return True
    return False

print question1('udacity', 'aud'), "\n"
# should return TRUE

print question1(0,0), "\n"
# should return FALSE

print question1(" "," "), "\n"
# should return TRUE

print question1("OnBelayClimbOn", "BelayOnClimbing"), "\n"
# should return FALSE
        
