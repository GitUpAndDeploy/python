student_scores = [180, 124, 165, 173, 189, 169, 146]

print(sum(student_scores))
print(max(student_scores))

# Max with for loop
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(highest_score)
