from collections import Counter
import sys
def get_input():
    for line in sys.stdin:
        for word in line.split():
            yield word

tokens = get_input()

def ns(): 
    """Get next string (token)"""
    return next(tokens, None)

def ni(): 
    """Get next integer"""
    token = ns()
    return int(token) if token is not None else None


def solve():
    from collections import Counter
    s=ns()
    if s[0]==s[-1]:
        sys.stdout.write(s + '\n')
    else:
        list_s=list(s)
        count=Counter(list_s)
        if count[s[0]]>=count[s[-1]]:
            list_s[-1]=list_s[0]
            sys.stdout.write(''.join(list_s) + '\n')
        else:
            list_s[0]=list_s[-1]
            sys.stdout.write(''.join(list_s) + '\n')
    
        

def main():
    t_str = ns()
    if t_str is not None:
        t = int(t_str)
        for _ in range(t):
            solve()

if __name__ == "__main__":
    main()
    