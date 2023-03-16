n = int(input())
cards = list(range(1, n+1))
ans = []
while len(cards) > 1:
    ans.append(cards[0])
    cards = cards[2:] + [cards[1]]
ans.append(cards[0])
print(*ans)
