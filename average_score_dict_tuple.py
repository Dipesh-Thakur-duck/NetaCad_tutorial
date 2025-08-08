school_class = {}

while True:
    name = input("Enter a name: ")

    if name == '':
        break

    score = int(input("Enter a student's score (0-10): "))

    if score not in range(0,11):
        break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
    
    for student in sorted(school_class.keys()):
        score = 0
        subjects = 0
        for values in school_class[student]:
            score += values
            subject += 1
        print(f"{student}'s average is {score/subjects}")