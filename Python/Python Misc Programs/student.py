# Shivali Dalmia
# student.py

# Student class
class Student:

    def __init__(self,name):        # Initialize all field variables of class
        self._name = name
        self._scores = []
        self._average = 0.0
        self._drop_number = 0

    def add_score(self,score):      # Adding a new score
        self._scores.append(score)

    def get_number_quizzes(self):   # Return total quizzes
        return len(self._scores)

    def calc_quiz_stats(self,drop_number):      # Calculate average score
        no_of_scores = self.get_number_quizzes()
        if drop_number >= no_of_scores:
            self._average = 0.0
        else:
            valid_scores_len = no_of_scores-drop_number
            sorted_scores = sorted(self._scores,reverse=True)
            sum_of_scores = sum(sorted_scores[0:valid_scores_len])
            self._average = sum_of_scores/valid_scores_len

        self._drop_number = drop_number

    def get_average(self):      # Return average score
        return self._average

    def __str__(self):      # Return string representation of Student instance
        no_of_scores = self.get_number_quizzes()
        sorted_scores = sorted(self._scores, reverse=True)
        dropped_quizzes = sorted_scores[no_of_scores - self._drop_number:no_of_scores]
        scores_str = ''
        for quiz_no in range(no_of_scores):
            if self._scores[quiz_no] in dropped_quizzes:
                scores_str = scores_str + str(quiz_no+1) + " - " + str(self._scores[quiz_no]) + " *" + "\n"
            else:
                scores_str = scores_str + str(quiz_no+1) + " - " + str(self._scores[quiz_no]) + "\n"

        result_str1 = "Name: "+ self._name + "\n\n" + "Quiz Average: "+ str(self._average) + "\n"
        result_str2 = "Number of Quizzes: " + str(no_of_scores) + "\n" + "Dropped Quizzes: " + str(self._drop_number) + "\n\n"
        result_str3 = "Quiz Scores (* => dropped):" + "\n" + scores_str

        return result_str1 + result_str2 + result_str3

def main():
    student1 = Student("Moxie Berner")      # Initializing Student1
    student1.add_score(64.0)                # Score1
    student1.add_score(30.0)                # Score2
    student1.add_score(10.5)                # Score3
    student1.add_score(20.0)                # Score4
    student1.calc_quiz_stats(2)             # Passing number of quizzes to be dropped for Student1
    print(student1)

    student2 = Student("John Jane")         # Initializing Student2
    student2.add_score(75.0)                # Score1
    student2.add_score(100.0)               # Score2
    student2.add_score(65.5)                # Score3
    student2.add_score(90.0)                # Score4
    student2.add_score(100.0)               # Score5
    student2.calc_quiz_stats(3)             # Passing number of quizzes to be dropped for Student2
    print(student2)

main()
