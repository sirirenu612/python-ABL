
teams = []
n = int(input("Enter number of teams: "))
rounds = int(input("Enter number of rounds: "))

for i in range(n):
    print("\nTeam", i + 1)
    name = input("Enter team name: ")
    members = int(input("Enter number of members: "))

    # Validate team size
    if members < 3 or members > 5:
        print("Invalid team size! Team must have 3 to 5 members.")
        continue
    else:
        print("Valid team")

    round_scores = []

    # Read student scores round-wise
    for r in range(rounds):
        total = 0
        print("Round", r + 1)

        for s in range(members):
            score = int(input("Enter student score: "))
            total += score

        round_scores.append(total)

    grand_total = sum(round_scores)

    teams.append({
        "name": name,
        "members": members,
        "scores": round_scores,
        "total": grand_total
    })

# Sort teams using total score and tie-breaking rules
teams.sort(
    key=lambda x: (x["total"], *x["scores"][::-1]),
    reverse=True
)

print("\n===== FINAL TEAM RANKING =====")

rank = 1
for team in teams:
    print("Rank:", rank)
    print("Team:", team["name"])
    print("Members:", team["members"])
    print("Round Scores:", team["scores"])
    print("Total Score:", team["total"])
    rank += 1
