
INPUT_FILE = "./input.txt"

class PassengerGroup:

    def __init__(self, data):
        self.data = data
        self.questions = dict()
        self.person_questions = list()

    def extract_questions(self):
        # Each new line represents the questions answered by a passenger.
        questions = self.data.split("\n")
        for idx, question_list in enumerate(questions):
            self.person_questions.append(list())
            for question in question_list:
                if question not in self.questions:
                    self.questions[question] = 1
                if question not in self.person_questions[idx]:
                    self.person_questions[idx].append(question)
        
        return len(self.questions)
    
    def extract_common_questions(self):
        common_questions = set(self.person_questions[0])
        for questions in self.person_questions[1:]:
            common_questions.intersection_update(questions)

        return len(common_questions)

if __name__ == "__main__":

    with open(INPUT_FILE, "r") as input_:
        groups = [PassengerGroup(line) for line in input_.read().split("\n\n")]
    
    total_sum = 0
    total_common_sum = 0
    for group in groups:
        total_sum += group.extract_questions()
        total_common_sum += group.extract_common_questions()

    print(f"Total number of questions answered: {total_sum}")
    print(f"Total number of common questions answered: {total_common_sum}")