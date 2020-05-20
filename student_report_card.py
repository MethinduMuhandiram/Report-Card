import json
import os

result = []

def read_student_score(file_path):
    """
    :param file_path:   reading the data from student_score.jason file
    :return:    {'10-A': [['10-A_00000',
    {'math': 91, 'science': 88, 'english': 35, 'literature': 41, 'total': 255, 'avg': 63}], .........
    """
    grade_10 = {}   # need to load student data into a dictionary (creating a empty dict)

    with open(file_path, 'r', encoding='utf-8')as json_file:
        data_set = json.load(json_file)
    #
    for student in data_set:
        if student['class'] not in grade_10.keys():     # need to add only  the class names into dict
            grade_10[student['class']] = []
        # {'10-A': [], '10-B': [], '10-C': [], '10-D': [], '10-E': [], '10-F': [], '10-G': [], '10-H': [], '10-I': []}

        """need to delete the 'class' and 'student_id' attributes,  because they are not necessary for calculations"""
        d = student.copy()
        del d['class']
        del d['student_id']

        # finding each student total scores
        total = sum(map(int, d.values()))

        # finding each student average scores
        avg = total/ len(d.values())

        # adding total and avg to the grade_10 dict.
        d['total'] = total
        d['avg'] = avg
        """any calculation cannot be performed if there is any string values other than integer values"""
        for y in dict(d).items():
            d[y[0]] = int(y[1])

        grade_10[student['class']].append([student['student_id'], d])
        # return json.dumps(grade_10, indent=3)
    return grade_10


def evaluate_subject_avg(data, level, subject, bmark, rank):
    """
    :param data:    processed data taken from 'grade_10' dictionary.
    :param level:   grade or class
    :param subject: enter the subject (math, science, english, literature, total, avg)
    :param bmark:   bench mark
    :return:        classes or grades, greater than the benchmark value.
    """
    num_std = 0
    num_sbj = 1

    for cls in data.items():
        c = [cls[0]]    # only shows the class name like ['10-A'], ['10-B'], ['10-C'],......

        num_std = len(cls[1])      # number of  student in  each cls

        total = sum(map(lambda x: x[1][subject], cls[1]))
        avg = total/num_std

        c.append(total)
        c.append(avg)
        result.append(c)  # gives an array of class name, total, average values for the given subject


    if level == "grade":
        res_2 = sum(map(lambda x: x[1], result))/ len(result)
        return res_2

    elif level == 'class':
        if bmark is not None:
            return list(filter(lambda x: x[-1] > bmark, result))
            # checking the if the avg value of each class is greater than benchmark
        else:
            return result


def evaluate_class_avg(data,subject):
    """
    :param data: processed data taken from 'grade_10' dictionary.
    :param subject: enter the subject (math, science, english, literature, total, avg)
    :return: top 3 classes of the grade 10
    """
    tot_arr = []
    cls_arr = []

    for cls in data.items():
        c = [cls[0]]  # only shows the class name like ['10-A'], ['10-B'], ['10-C'],......

        num_std = len(cls[1])  # number of  student in  each cls

        total = sum(map(lambda x: x[1][subject], cls[1]))
        avg = total / num_std

        c.append(total)
        c.append(avg)
        result.append(c)

        cls_arr.append(cls[0])
        tot_arr.append(total)
    top1_cls = tot_arr.index(sorted(tot_arr)[-1])
    top2_cls = tot_arr.index(sorted(tot_arr)[-2])
    top3_cls = tot_arr.index(sorted(tot_arr)[-3])
    top_cls = [cls_arr[top1_cls], cls_arr[top2_cls], cls_arr[top3_cls]]
    return f"Top 3 classes of grade 10 = {top_cls}"

def evaluate_student_rank(data, cls_name):
    """
    :param data: processed data taken from 'grade_10' dictionary.
    :param cls_name: class name from grade 10
    :return: Class first id number
    """
    arr_avg_score_cls = []
    id_arr_cls = []

    for cls in data.items():
        c = [cls[0]]  # only shows the class name like ['10-A'], ['10-B'], ['10-C'],......
        if cls[0] == cls_name:
            for x in cls[1]:
                arr_avg_score_cls.append(x[1]['avg'])   # taking the average of students of given class
                id_arr_cls.append(x[0])
            max_10a = max(arr_avg_score_cls)
            ten_cls = arr_avg_score_cls.index(max_10a)
            return 'Class First -', id_arr_cls[ten_cls]


def evaluate_student_avg(file_path):
    """
    :param file_path: reading the data from student_score.jason file
    :return: batch top  student's id number.
    """

    grade_10 = {}
    avg_arr = []
    id_arr = []
    with open(file_path, 'r', encoding='utf-8')as json_file:
        data_set = json.load(json_file)

    for student in data_set:
        if student['class'] not in grade_10.keys():  # need to add only  the class names into dict
            grade_10[student['class']] = []
        # {'10-A': [], '10-B': [], '10-C': [], '10-D': [], '10-E': [], '10-F': [], '10-G': [], '10-H': [], '10-I': []}

        """need to delete the 'class' and 'student_id' attributes,  because they are not necessary for calculations"""
        d = student.copy()
        del d['class']
        del d['student_id']

        # finding each student total scores
        total = sum(map(int, d.values()))
        # finding each student average scores
        avg = total / len(d.values())

        # adding total and avg to the grade_10 dict.
        d['total'] = total
        d['avg'] = avg
        """any calculation cannot be performed if there is any string values other than integer values"""
        for y in dict(d).items():
            d[y[0]] = int(y[1])

        avg_arr.append(avg)
        id_arr.append(student['student_id'])

    section_1st = avg_arr.index(sorted(avg_arr)[-1])    # sorting the average values min to max

    batch_top = [id_arr[section_1st]]
    return batch_top


if __name__ == '__main__':

    file_path = os.path.join('student_score.json')
    data = read_student_score(file_path)
    # print(data)

    #  Enter the  subject and the bench mark,
    q1q2 = evaluate_subject_avg(data=data, level='class', subject='science', bmark=70, rank = 10)
    print("Number of classes above the average of given benchmark for entered subject  = ", len(q1q2))
    print('------------------------------------------------------------------------------------------------')
    # Evaluate the top 3 classes in Grade 10
    q3= evaluate_class_avg(data=data, subject='total')
    print("Top  3 classes in grade  10 = ", q3)
    print('------------------------------------------------------------------------------------------------')

    q4 = evaluate_student_rank(data=data, cls_name='10-E')
    print(q4)
    print('------------------------------------------------------------------------------------------------')

    q5 = evaluate_student_avg(file_path)
    print(f"section 1st = ", q5)




