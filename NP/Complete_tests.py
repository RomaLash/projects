import re
from function import *

inputfile = "data_optimal.txt"
output_file = "output_optimal.txt"
Etalon_otvet = [[1,1,0,0,0,0,0,1],[0,0,1,0,0,0,1,0],[1,0,0,1,0,0,0,0],[1,1,0,0,0,1,0,0],[0,1,0,0,1,0,0,0]]
Etalon_comfort = 16
Etalon_meri = [[1,1,0,0,0,0,0,1],[0,0,1,0,0,0,1,0],[1,0,0,1,0,0,0,0],[1,1,0,0,0,1,0,0],[0,1,0,0,1,0,0,0],[1,0,0,0,1,0,0,0],[3,6,4,9,1,8]]
Etalon_kolichestvo = 8

#тест корректности
Correct_test(inputfile)

#тест входа
input_test(inputfile, Etalon_meri, Etalon_kolichestvo)

#тест алгоритма
algoritm_test(Etalon_meri, Etalon_kolichestvo,Etalon_otvet, Etalon_comfort)

#тест выхода
output_test(output_file,Etalon_otvet,Etalon_comfort)

