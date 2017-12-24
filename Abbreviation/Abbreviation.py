# https://www.hackerrank.com/challenges/abbr/problem

def abbreviation(A, B):
    table = []
    for i in range(len(A) + 1):
        cache = table
        table = [False] * (len(B) + 1)
        for j in range(len(B) + 1):
            a = A[:i]
            b = B[:j]
               
            if not b:
                if not a or a.lower() == a:
                    table[j] = True
                else:
                    table[j] = False
            else:
                if not a:
                    table[j] = False
                elif a[-1] == a[-1].upper():
                    if a[-1] == b[-1]:
                        table[j] = cache[j - 1]
                    else:
                        table[j] = False
                else:   
                    table[j] = (
                        # Drop the letter
                        cache[j]
                        or
                        # Make it upper case
                        (
                            a[-1].upper() == b[-1]
                            and
                            cache[j - 1]
                        )
                    )
                    
    return table[len(B)]
    
    
    
if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        a = input().strip()
        b = input().strip()
        result = 'YES' if abbreviation(a, b) else 'NO'
        print(result)

