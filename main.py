import tkinter as tk
from threading import Timer

import custom_views as cv
import file_interactor as fi


class ControllerModel:
    def __init__(self):
        """
         initialize instance object of ControllerModel
        """
        self.number_of_wrong_attempts = 0

    def increment_wrong_attempts(self):
        """
         increase the value of number_of_wrong_attempts
        :return: void
        """
        self.number_of_wrong_attempts = self.number_of_wrong_attempts + 1

    def get_wrong_attempts(self):
        """
        getting number_of_wrong_attempts value
        :return:
        """
        return self.number_of_wrong_attempts

    def reset_wrong_answer(self):
        """
        reset the value of number_of_wrong_attempts
        :return:
        """
        self.number_of_wrong_attempts = 0


global current_question
global question_form, selection_form, result_form

selection_diff_form_root = tk.Tk()
selection_diff_form_root.minsize(500, 200)
selection_diff_form_root.maxsize(800, 400)
selection_diff_form_frame = tk.Frame(selection_diff_form_root)
selection_diff_form_frame.pack()

question_form_root = tk.Toplevel(selection_diff_form_root)
question_form_root.minsize(600, 300)
question_form_root.maxsize(800, 400)
question_form_frame = tk.Frame(question_form_root)
question_form_frame.pack()

result_form_root = tk.Toplevel(question_form_root)
result_form_root.minsize(400, 200)
result_form_root.maxsize(800, 400)
result_form_frame = tk.Frame(result_form_root)
result_form_frame.pack()

file_model = fi.FileModel()
controller = ControllerModel()


def newQuestion():
    """
     this function handle getting new question from file interactor
    :return:
    """
    global current_question

    if file_model.is_end_of_file():
        question_form_root.withdraw()
        result_form_root.deiconify()
        result_form.set_number_of_wrong_attempts(controller.get_wrong_attempts())
        if controller.get_wrong_attempts() == selection_form.get_guessed_number():
            result_form.set_guess_message("Yes, you could guess right XD !")

    else:
        question_form.reset_answers_back_ground_color()
        current_question = file_model.get_next_question()
        question_form.set_question_view(current_question)


def when_answer_choosed(text):
    """
    callback function that handle logic when user choose answer
    :param text: String
    :return: void
    """
    global current_question
    print(text)
    # if choose the correct answer
    if current_question.get_correct_answer() in text:
        question_form.hide_wrong_answer_label()
        index = current_question.get_answers().index(text)
        question_form.show_answer(index + 1)
        t = Timer(1.0, newQuestion)
        t.start()
    else:
        controller.increment_wrong_attempts()
        question_form.show_wrong_answer_label()


def when_level_selected(text):
    """
    callback function that handle logic when user choose level
    :param text: String
    :return: void
    """
    global current_question
    file_model.open_file(text.lower())
    current_question = file_model.get_next_question()
    question_form_root.deiconify()
    question_form.clear()
    selection_diff_form_root.withdraw()
    question_form.set_question_view(current_question)


def newQuiz(text):
    """
     handle new Quiz logic
    :param text: String
    :return: void
    """
    print(text)
    selection_diff_form_root.deiconify()
    selection_form.clear()
    result_form_root.withdraw()
    controller.reset_wrong_answer()


question_form = cv.QuestionForm(question_form_frame, when_answer_choosed)
question_form_root.withdraw()

selection_form = cv.LevelSelectionForm(selection_diff_form_frame, when_level_selected)
selection_form.set_chooses(["Easy", "Medium", "Hard"])

result_form = cv.ResultForm(result_form_frame, newQuiz)
result_form_root.withdraw()
result_form.set_number_of_wrong_attempts(10)

selection_diff_form_root.mainloop()
question_form_root.mainloop()
