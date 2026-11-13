def lowest_students(student_list):
    scores = []
    for students in student_list:
        scores.append(students[1])
    sorted_scores = sorted(set(scores))
    second_lowest = sorted_scores[1]
    
    second_lowest_name = []
    for students in student_list:
        if students[1] == second_lowest:
            second_lowest_name.append(students[0])
    second_lowest_name = sorted(second_lowest_name)
    
    for name in second_lowest_name:
        print(name)
    
if __name__ == '__main__':
    student_list = []
    for num in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name,score])
        
    lowest_students(student_list)
   
