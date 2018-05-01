import pandas as pd

import models


class FileModel:

    def __init__(self):
        """
        initialize instance of FileModel object
        """
        self._count = 0
        self._dataSet = pd.DataFrame()
        self.q = models.FillInBlanksQuestion()

    def open_file(self, file_name):
        """
         open CSV file
        :return: void
        """
        self._count = 0
        self._dataSet = pd.read_csv(file_name + '.csv', encoding="ISO-8859-1")
        return self._dataSet

    def get_next_question(self):
        """
        read question from csv file and return it.
        :return: models.Question
        """
        if self._count < 4:
            self.q = models.FillInBlanksQuestion()
            self.q.set_question(str(self._dataSet['Question'][self._count]))
            self.q.set_answers(tuple(self._dataSet.iloc[self._count])[1:5])
            self.q.set_correct_answer(str(self._dataSet['Correct Answer'][self._count]))
            self._count = self._count + 1
        return self.q

    def is_end_of_file(self):
        """
         check if the seek at the end of file
        :return: boolean
        """
        if self._count == 4:
            return 1
        else:
            return 0
