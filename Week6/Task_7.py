# Task 7: Filter active players, sort by score,
# keep the top 3, and format their ranks.

players = [
    ("Aria", 88, True),
    ("Kael", 95, False),
    ("Zane", 91, True),
    ("Mira", 76, True),
    ("Lyra", 99, True),
    ("Dax", 84, True)
]

active_players = sorted(
    [player for player in players if player[2]],
    key=lambda player: player[1],
    reverse=True
)

result = [
    f"Rank {rank}: {username} ({score})"
    for rank, (username, score, is_active)
    in enumerate(active_players[:3], start=1)
]

print("Top 3 players:")
for player in result:
    print(player)
