py.test test_sample.py --collect-only  # collects information test suite - набор тестов для сбора информации

py.test test_sample.py -v  # outputs verbose messages - выводит подробные сообщения

py.test -q test_sample.py  # omit filename output - опускать вывод имени файла

python -m pytest -q test_sample.py  # calling pytest through python - вызов pytest через python

py.test --markers  # show available markers - показать доступные маркеры

# In order to create a reusable marker. - Для создания многоразового маркера.
/*
# content of pytest.ini - содержимое pytest.ini
[pytest]
markers =
    webtest: mark a test as a webtest.
*/

py.test -k "TestClass and not test_one"  # only run tests with names that match the "string expression" - запускать только тесты с именами, соответствующими "строковому выражению"

py.test test_server.py::TestClass::test_method  # cnly run tests that match the node ID - Только запускать тесты, соответствующие идентификатору узла

py.test -x  # stop after first failure - остановить после первого сбоя

py.test --maxfail=2  # stop after two failures - остановить после двух сбоев

py.test --showlocals  # show local variables in tracebacks - показывать локальные переменные в трассировке
py.test -l  # (shortcut) - (ярлык)

py.test --tb=long  # the default informative traceback formatting - форматирование информативной трассировки   по умолчанию
py.test --tb=native  # the Python standard library formatting - форматирование стандартной библиотеки Python
py.test --tb=short  # a shorter traceback format - более короткий формат трассировки  
py.test --tb=line  # only one line per failure - только одна строка на сбой
py.test --tb=no  # no tracebak output - нет вывода tracebak

py.test -x --pdb # drop to PDB on first failure, then end test session - перейти в PDB при первой ошибке , затем завершить сеанс тестирования

py.test --durations=10  # list of the slowest 10 test durations. - список из 10 самых медленных длительностей теста.

py.test --maxfail=2 -rf  # exit after 2 failures, report fail info. - выйти после 2 сбоев, сообщить информацию о сбое

py.test -n 4  # send tests to multiple CPUs - отправлять тесты на несколько процессоров

py.test -m slowest  # run tests with decorator @pytest.mark.slowest or slowest = pytest.mark.slowest; @slowest - запускать тесты с декоратором @ pytest.mark.slowest или slowest = pytest.mark.slowest; @slowest

py.test --traceconfig  # find out which py.test plugins are active in your environment. - узнайте, какие плагины py.test активны в вашей среде.

py.test --instafail  # if pytest-instafail is installed, show errors and failures instantly instead of waiting until the end of test suite. - если установлен pytest-instafail, мгновенно отображать ошибки и сбои, а не ждать окончания набора тестов.

# Test using parametrize - Тестирование с использованием параметризации
/*
    import pytest


    @pytest.mark.parametrize(
        ('n', 'expected'), [
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            pytest.mark.xfail((1, 0)),
            pytest.mark.xfail(reason="some bug")((1, 0)),
            pytest.mark.skipif('sys.version_info >= (3,0)')((10, 11)),
        ]
    )
    def test_increment(n, expected):
        assert n + 1 == expected
*/