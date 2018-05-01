import tkinter as tk


class CustomButton(tk.Frame):
    def __init__(self, master, fnc):
        """
          initialize instance of CustomButton object
         :param master: Frame
         :param fnc:  Observable function
        """
        super().__init__(master)
        self._text = tk.StringVar()
        self._button = tk.Button(master,
                                 fg="black",
                                 bg="white",
                                 textvariable=self._text,
                                 command=self.button_clicked,
                                 relief=tk.GROOVE, height=1, width=30, padx=5, pady=5)
        self._button.pack()
        self._function_listener = fnc

    def button_clicked(self):
        """ this function delegate to function callback, user click action."""
        self._function_listener(self._text.get())

    def set_text_button(self, text):
        """
        this function set the that will being showed on the button
        :param text: String
        :return: void
        """
        self._text.set(text)

    def change_color_button(self, color):
        """
        this function change color of button
        :param color: String
        :return:
        """
        self._button.config(bg=color)


class QuestionForm(tk.Frame):
    def __init__(self, master, fnc):
        """
         initialize instance of QuestionForm object
        :param master: Frame
        :param fnc:  Observable function
        """
        super().__init__(master)
        self._question_view = tk.Label(master, text="",
                                       font=("Helvetica", 16), padx=5, pady=25)
        self._question_view.pack()
        self._wrong_answer = tk.Label(master, text="Try a gain", fg="red",
                                      font=("Helvetica", 16))
        self._answer_one_view = CustomButton(master, fnc)
        self._answer_two_view = CustomButton(master, fnc)
        self._answer_three_view = CustomButton(master, fnc)
        self._answer_four_view = CustomButton(master, fnc)

    def set_question_view(self, _question):
        """
         set question and answer views
        :param _question: FillInQuestion
        :return: void
        """
        self.set_answers(_question.get_answers())
        self.set_question(_question.get_question())
        self._wrong_answer.pack_forget()

    def set_question(self, question):
        """
        this function set or change the text question label
        :param question:
        :return: void
        """
        self._question_view.config(text=question)

    def set_answers(self, answers):
        """
        this function set or change the text of all answer buttons
        :param answers: Tuple
        :return: void
        """
        self._answer_one_view.set_text_button(answers[0])
        self._answer_two_view.set_text_button(answers[1])
        self._answer_three_view.set_text_button(answers[2])
        self._answer_four_view.set_text_button(answers[3])

    def show_answer(self, correct_answer):
        """
        show the correct answer to user with green color and all wrong answers with red color
        :param correct_answer: Int
        :return: void
        """
        self._answer_one_view.change_color_button("red")
        self._answer_two_view.change_color_button("red")
        self._answer_three_view.change_color_button("red")
        self._answer_four_view.change_color_button("red")
        if correct_answer == 1:
            self._answer_one_view.change_color_button("green")

        elif correct_answer == 2:
            self._answer_two_view.change_color_button("green")

        elif correct_answer == 3:
            self._answer_three_view.change_color_button("green")

        elif correct_answer == 4:
            self._answer_four_view.change_color_button("green")

    def reset_answers_back_ground_color(self):
        """
        reset all answers button colors with white color
        :return:
        """
        self._answer_one_view.change_color_button("white")
        self._answer_two_view.change_color_button("white")
        self._answer_three_view.change_color_button("white")
        self._answer_four_view.change_color_button("white")

    def show_wrong_answer_label(self):
        """
        show wrong answer label
        :return:
        """
        print("wrong answer")
        self._wrong_answer.pack()

    def hide_wrong_answer_label(self):
        """
        hide wrong answer label
        :return:
        """
        self._wrong_answer.pack_forget()

    def clear(self):
        """
        clear all form views
        :return:
        """
        self.reset_answers_back_ground_color()


class LevelSelectionForm(tk.Frame):
    def __init__(self, master, fnc):
        """
        initialize instance of LevelSelectionForm object
        :param master: Frame
        :param fnc:  Observable function
        """
        super().__init__()
        self._title_view = tk.Label(master, text="Select difficulty of levels .",
                                    font=("Helvetica", 14), padx=5, pady=25)
        self._title_view.pack()
        self._level_one = CustomButton(master, fnc)
        self._level_two = CustomButton(master, fnc)
        self._level_three = CustomButton(master, fnc)
        self._wrong_answer_question = tk.Label(master, text="How many wrong you guess before enter the quiz ?",
                                               padx=5,
                                               pady=25)
        self._wrong_answer_question.pack(side=tk.LEFT)
        self._guesses_number = tk.Entry(master, bd=5, relief=tk.FLAT)
        self._guesses_number.pack(side=tk.RIGHT)

    def set_chooses(self, chooses):
        """
        set text chooses button
        :param chooses: Tuple
        :return: void
        """
        self._level_one.set_text_button(chooses[0])
        self._level_two.set_text_button(chooses[1])
        self._level_three.set_text_button(chooses[2])

    def get_guessed_number(self):
        """
        get the entered guessed number
        :return: int
        """
        try:
            return int(self._guesses_number.get())
        except:
            return -1

    def clear(self):
        """
        clear all views
        :return:
        """
        self._guesses_number.config(text="")


class ResultForm(tk.Frame):
    def __init__(self, master, fnc):
        """
        initialize instance of ResultForm object
        :param master: Frame
        :param fnc: Observable function
        """
        super().__init__()
        self._title_view = tk.Label(master,
                                    text="The Quiz Ended .",
                                    font=("Helvetica", 16),
                                    padx=5,
                                    pady=25)
        self._title_view.pack()
        self._new_quiz_button = CustomButton(master, fnc)
        self._new_quiz_button.set_text_button("New Quiz")
        self._number_of_wrong_attempts = tk.Label(master,
                                                  text="",
                                                  fg="red",
                                                  font=("Helvetica", 16),
                                                  padx=5,
                                                  pady=25)
        self._guess_message = tk.Label(master,
                                       text="",
                                       font=("Helvetica", 14),
                                       padx=5,
                                       pady=25)

    def set_number_of_wrong_attempts(self, number):
        """
        set the number of wrog attempts
        :param number:
        :return: void
        """
        self._number_of_wrong_attempts.config(text="Number of wrong attempts  : " + str(number))
        self._number_of_wrong_attempts.pack()

    def set_guess_message(self, message):
        """
        set guess message
        :param message: String
        :return: void
        """
        self._guess_message.config(text=message)
        self._guess_message.pack()

    def clear(self):
        """
        clear all views
        :return:
        """
        self._guess_message.config(text="")
        self._number_of_wrong_attempts.pack_forget()
