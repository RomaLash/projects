import re
from function import *

inputfile = "data_nonoptimal.txt"
output_file = "output_nonoptimal.txt"
Etalon_otvet = [[1,0,0,0,0],[0,1,1,0,0],[0,0,0,0,1],[0,0,0,1,0]]
Etalon_comfort = 5
Etalon_meri = [[1,0,0,1,0],[1,0,0,0,0],[1,1,1,0,0],[0,1,1,0,0],[0,0,0,0,1],[0,0,0,1,0],[2,1,8,2,1,1]]
Etalon_kolichestvo = 5

#тест корректности
Correct_test(inputfile)

#тест входа
input_test(inputfile, Etalon_meri, Etalon_kolichestvo)

#тест алгоритма
algoritm_test(Etalon_meri, Etalon_kolichestvo,Etalon_otvet, Etalon_comfort)

#тест выхода
output_test(output_file,Etalon_otvet,Etalon_comfort)

