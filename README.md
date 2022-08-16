# Comparing of Fixed-point iteration with Bisection method
---
Данный репозиторий показывает работу по сравнению двух алгоритмов, используемых для вычисления рабочей точки системы трубопровод-насос (НПС). 
Первый метод широко используемый на сегодняшний момент - [Метод бисекции](https://en.wikipedia.org/wiki/Bisection_method).
Второй метод - [Метод простой итерации](https://en.wikipedia.org/wiki/Fixed-point_iteration) разработан мной как альтернатива первому.

В файле [Presentation](https://github.com/ArtemevIvanAlekseevich/Comparing_of_Fixed-point_iteration_with_Bisection_method/blob/Flow/Presentation.pdf) показаны две презентации. В первой описан вывод вспомогательных формул для метода простой итерации, a так же его реализация 

В файлах [Bisection method](https://github.com/ArtemevIvanAlekseevich/Comparing_of_Fixed-point_iteration_with_Bisection_method/blob/Flow/Bisection%20method.py) и [Fixed-point iteration](https://github.com/ArtemevIvanAlekseevich/Comparing_of_Fixed-point_iteration_with_Bisection_method/blob/Flow/Fixed-point%20iteration.py) соответственно реализованы методы бисекции и простой итерации. А файлы [TEST Bisection method](https://github.com/ArtemevIvanAlekseevich/Comparing_of_Fixed-point_iteration_with_Bisection_method/blob/Flow/TEST%20Bisection%20method.py) и [TEST Fixed-point iteration](https://github.com/ArtemevIvanAlekseevich/Comparing_of_Fixed-point_iteration_with_Bisection_method/blob/Flow/TEST%20Fixed-point%20iteration.py) тестируют время работы двух методов на одинаковых входных данных. 

В результате новый алгоритм работает на предложенных тестах приблизительно в 5 раз быстрее. Так на Intel core i7-6700QH классический алгоритм отрабатывает за 305 секунд, новый - 65.