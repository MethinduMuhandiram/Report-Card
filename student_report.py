import json

# reading data from json file
with open('student_socre.json', 'r') as my_file:
    data = json.load(my_file)

    # defining arrays for science score in each class
    arrsc10a = []
    arrsc10b = []
    arrsc10c = []
    arrsc10d = []
    arrsc10e = []
    arrsc10f = []
    arrsc10g = []
    arrsc10h = []
    arrsc10i = []

    # defining arrays for literature score in each class
    arrlit10a = []
    arrlit10b = []
    arrlit10c = []
    arrlit10d = []
    arrlit10e = []
    arrlit10f = []
    arrlit10g = []
    arrlit10h = []
    arrlit10i = []

    # defining arrays for average score in each class
    arravgscore10a = []
    arravgscore10b = []
    arravgscore10c = []
    arravgscore10d = []
    arravgscore10e = []
    arravgscore10f = []
    arravgscore10g = []
    arravgscore10h = []
    arravgscore10i = []

    scavg = []  # science average score array
    litavg = []  # literature average score array

    score_avg_arr = []  # average score array for all students
    all_info_arr = []   # all info array for all students

    for score in data:

        math_score = int(score['math'])
        science_score = score['science']
        english_score = score['english']
        literature_score = int(score['literature'])
        class_name = score['class']
        student_id = score['student_id']
        score_avg = (math_score + science_score + english_score + literature_score) / 4
        # get the average value for each student
        score_avg_arr.append(score_avg)  # adding the average values into average score array
        all_info = [student_id, class_name, math_score, science_score, english_score, literature_score, score_avg]
        all_info_arr.append(all_info)

        """for each class adding the science score,  literature score, average score into class vise arrays. """
        if score['class'] == '10-A':
            arrsc10a.append(score['science'])
            arrlit10a.append(int(score['literature']))
            arravgscore10a.append(score_avg)

        if score['class'] == '10-B':
            arrsc10b.append(score['science'])
            arrlit10b.append(int(score['literature']))
            arravgscore10b.append(score_avg)

        if score['class'] == '10-C':
            arrsc10c.append(score['science'])
            arrlit10c.append(int(score['literature']))
            arravgscore10c.append(score_avg)

        if score['class'] == '10-D':
            arrsc10d.append(score['science'])
            arrlit10d.append(int(score['literature']))
            arravgscore10d.append(score_avg)

        if score['class'] == '10-E':
            arrsc10e.append(score['science'])
            arrlit10e.append(int(score['literature']))
            arravgscore10e.append(score_avg)

        if score['class'] == '10-F':
            arrsc10f.append(score['science'])
            arrlit10f.append(int(score['literature']))
            arravgscore10f.append(score_avg)

        if score['class'] == '10-G':
            arrsc10g.append(score['science'])
            arrlit10g.append(int(score['literature']))
            arravgscore10g.append(score_avg)

        if score['class'] == '10-H':
            arrsc10h.append(score['science'])
            arrlit10h.append(int(score['literature']))
            arravgscore10h.append(score_avg)

        if score['class'] == '10-I':
            arrsc10i.append(score['science'])
            arrlit10i.append(int(score['literature']))
            arravgscore10i.append(score_avg)

    def science_avg(arrsc):
        # finding  the classes with the average above 70 for science
        if (sum(arrsc) / len(arrsc)) > 70:
            scavg.append(sum(arrsc) / len(arrsc))

    science_avg(arrsc10a)
    science_avg(arrsc10b)
    science_avg(arrsc10c)
    science_avg(arrsc10d)
    science_avg(arrsc10e)
    science_avg(arrsc10f)
    science_avg(arrsc10g)
    science_avg(arrsc10h)
    science_avg(arrsc10i)

    def literature_avg(arrlit):
        # finding  the classes with the average above 70 for science
        if (sum(arrlit) / len(arrlit)) > 70:
            litavg.append(sum(arrlit) / len(arrlit))

    literature_avg(arrlit10a)
    literature_avg(arrlit10b)
    literature_avg(arrlit10c)
    literature_avg(arrlit10d)
    literature_avg(arrlit10e)
    literature_avg(arrlit10f)
    literature_avg(arrlit10g)
    literature_avg(arrlit10h)
    literature_avg(arrlit10i)

# print(all_info_arr)
print("Number of classes that have an above-average 70 for Science - ", len(scavg))

print("Number of classes that have an above-average 70 for Literature - ", len(litavg))

"""finding the maximum average value for each class and give the output as the student ID"""
max_10a = max(arravgscore10a)
ten_a = score_avg_arr.index(max_10a)
print("10 - A First -", all_info_arr[ten_a][0])

max_10b = max(arravgscore10b)
ten_b = score_avg_arr.index(max_10b)
print("10 - B First -", all_info_arr[ten_b][0])

max_10c = max(arravgscore10c)
ten_c = score_avg_arr.index(max_10c)
print("10 - C First -", all_info_arr[ten_c][0])

max_10d = max(arravgscore10d)
ten_d = score_avg_arr.index(max_10d)
print("10 - D First -", all_info_arr[ten_d][0])

max_10e = max(arravgscore10e)
ten_e = score_avg_arr.index(max_10e)
print("10 - E First -", all_info_arr[ten_e][0])

max_10f = max(arravgscore10f)
ten_f = score_avg_arr.index(max_10f)
print("10 - F First -", all_info_arr[ten_f][0])

max_10g = max(arravgscore10g)
ten_g = score_avg_arr.index(max_10g)
print("10 - G First -", all_info_arr[ten_g][0])

max_10h = max(arravgscore10h)
ten_h = score_avg_arr.index(max_10h)
print("10 - H First -", all_info_arr[ten_h][0])

max_10i = max(arravgscore10i)
ten_i = score_avg_arr.index(max_10i)
print("10 - I First -", all_info_arr[ten_i][0])

"""Finding the maximum average value from the whole section and give the output as the student  ID"""
max_val = max(score_avg_arr)
# print("max value", max_val)
# batch_top = score_avg_arr.index(max_val)
# print(batch_top)
print("Section First -", all_info_arr[score_avg_arr.index(max_val)][0])

"""writing all the information in a csv file"""
with open('Report_card_answers.csv', 'w', encoding='utf-8') as report_answers:
    report_answers.write(f"1. How many classes are there that have an above-average 70 for science? {len(scavg)}\n")
    report_answers.write(f"\n")
    report_answers.write(f"2. How many classes are there that have an above-average 70 for literature? {len(litavg)}\n")
    report_answers.write(f"\n")
    report_answers.write(f"4. Best student in each class:\n")
    report_answers.write(f"10-A First:{all_info_arr[ten_a][0]}\n")
    report_answers.write(f"10-B First:{all_info_arr[ten_b][0]}\n")
    report_answers.write(f"10-C First:{all_info_arr[ten_c][0]}\n")
    report_answers.write(f"10-D First:{all_info_arr[ten_d][0]}\n")
    report_answers.write(f"10-E First:{all_info_arr[ten_e][0]}\n")
    report_answers.write(f"10-F First:{all_info_arr[ten_f][0]}\n")
    report_answers.write(f"10-G First:{all_info_arr[ten_g][0]}\n")
    report_answers.write(f"10-H First:{all_info_arr[ten_h][0]}\n")
    report_answers.write(f"10-I First:{all_info_arr[ten_i][0]}\n")
    report_answers.write(f"\n")
    report_answers.write(f"5. Section 1st place: {all_info_arr[score_avg_arr.index(max_val)][0]}")
    report_answers.close()