class Question:
    def __init__(self):
        self.question = ""

    def set_question(self, question):
        """
        set question
        :param question: String
        :return: void
        """
        self.question = question

    def get_question(self):
        """
        get question
        :return: String
        """
        return self.question


class FillInBlanksQuestion(Question):

    def __init__(self):
        super().__init__()
        self.answers = ()
        self.correct_answer = ""

    def get_answers(self):
        """
        get answers
        :return: Tuple
        """
        return self.answers

    def set_answers(self, answers):
        """
        set answers
        :param answers:Tuple
        :return: void
        """
        self.answers = answers

    def get_correct_answer(self):
        """
         getting correct answer
        :return:
        """
        return self.correct_answer

    def set_correct_answer(self, correct_answer):
        """
        set correct answer
        :param correct_answer: String
        :return: void
        """
        self.correct_answer = correct_answer
