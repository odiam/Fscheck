import unittest
from fscheck import new_image_controller
import os

class Tester(unittest.TestCase):

    __testpath = os.getcwd() + os.path.sep

    def test1(self):
        '''
        Esegue con input test/'test1' e test/'test1_out .
        Si tratta di alcuni file dallo stesso contenuto e alcune cartelle
        vuote.
        ' '''
        print("TEST1")
        new_image_controller(path=self.__testpath+"test1", output_dir=self.__testpath+"test1_out")
        print("---------------\n\n")

    def test2(self):
        '''
        BLA BLA BLA COME SOPRA
        un primo livello di sole cartelle contenenti file diversi
        :return:
        '''
        print("TEST2")
        new_image_controller(self.__testpath+"test2", self.__testpath+"test2_out")
        print("---------------\n\n")

if __name__ == "__main__":
    t = Tester()

    t.test1()
    t.test2()