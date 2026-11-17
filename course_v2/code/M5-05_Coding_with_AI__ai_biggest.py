# M5-05_Coding_with_AI - ai_biggest.py
# Suggested by an AI helper:
def biggest(scores):
    best = 0
    for s in scores:
        if s > best:
            best = s
    return best

print(biggest([4, 9, 2]))
print(biggest([15, 3, 12]))
