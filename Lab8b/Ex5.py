# Program to remove any scores from a list that are below 50.

scores = [60, 45, 30, 85, 10, 90]
new_scores = []

for score in scores:
    if score >= 50:
        new_scores.append(score)

print(new_scores)