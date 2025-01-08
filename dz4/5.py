all_marks = dict()

while True :
    line = input()

    if line == '' :
        break

    vec = line.split(' ')
    subject = str(vec[0])
    person = str(vec[1])
    mark = int(vec[2])

    subject_marks = all_marks.get(subject, dict())
    persons_marks = subject_marks.get(person, list())
    persons_marks.append(mark)

    subject_marks[person] = persons_marks
    all_marks[subject] = subject_marks

for subject, subject_marks in all_marks.items() :
    print(subject)
    for person, persons_marks in subject_marks.items():
        line = person
        for mark in persons_marks :
            line += ' ' + str(mark)
        print(line)
    print('')
