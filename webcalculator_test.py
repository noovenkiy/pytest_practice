import requests
import pytest
from app import Calculator


@pytest.fixture()
def calc_app():
    return Calculator()


class TestCalculatorState:
    """
    Тесты для эндпоинта state
    """

    Calculator().start()
    response = requests.get("http://localhost:17678/api/state")

    def test_external_status_code(self):
        """
        тест на внешний статус код ответа от сервера
        """
        assert self.response.status_code == 200

    def test_response(self):
        """
        тест ответа на корректный запрос
        """
        assert self.response.json()["statusCode"] == 0
        assert self.response.json()["state"] == "OК"

    def test_error_status_5(self):
        """
        тест на проверку ответа (статус кода и сообщения) при указании неверного метода HTTP
        """
        response = requests.post("http://localhost:17678/api/state")
        assert response.json()["statusCode"] == 5
        assert (
            "Не верное имя задачи или тип HTTP запроса"
            in response.json()["statusMessage"]
        )


class TestCalculatorAddition:
    """
    Тесты для эндпоинта addition
    """

    Calculator().start()
    response = requests.post(
        "http://localhost:17678/api/addition", json={"x": 1, "y": 2}
    )

    def test_external_status_code(self):
        """
        тест на внешний статус код ответа от сервера
        """
        assert self.response.status_code == 200

    def test_response(self):
        """
        тест ответа на корректный запрос
        """
        assert self.response.json()["statusCode"] == 0
        assert self.response.json()["result"] == 3

    def test_error_status_2(self):
        """
        тест на проверку ответа при указании неверного количества ключей в теле
        """
        response = requests.post("http://localhost:17678/api/addition", json={"x": 1})
        assert response.json()["statusCode"] == 2
        assert "Не указаны необходимые параметры" in response.json()["statusMessage"]

    def test_error_status_3(self):
        """
        тест на проверку ответа при указании неверного формата одного из значений (float вместо int)
        """
        response = requests.post(
            "http://localhost:17678/api/addition", json={"x": 1, "y": 2.5}
        )
        assert response.json()["statusCode"] == 3
        assert (
            "Значения параметров должны быть целыми" in response.json()["statusMessage"]
        )

    def test_error_status_4(self):
        """
        тест на проверку ответа при указании числа превышающего допустимое
        """
        response = requests.post(
            "http://localhost:17678/api/addition", json={"x": 1, "y": 100**5}
        )
        assert response.json()["statusCode"] == 4
        assert (
            "Превышены максимальные значения параметров"
            in response.json()["statusMessage"]
        )

    def test_error_status_5(self):
        """
        тест на проверку ответа (статус кода и сообщения) при указании неверного метода HTTP
        """
        response = requests.get("http://localhost:17678/api/addition")
        assert response.json()["statusCode"] == 5
        assert (
            "Не верное имя задачи или тип HTTP запроса"
            in response.json()["statusMessage"]
        )


class TestCalculatorMultiplication:
    """
    Тесты для эндпоинта multiplication
    """

    Calculator().start()
    response = requests.post(
        "http://localhost:17678/api/multiplication", json={"x": 1, "y": 2}
    )

    def test_external_status_code(self):
        """
        тест на внешний статус код ответа от сервера
        """
        assert self.response.status_code == 200

    def test_response(self):
        """
        тест ответа на корректный запрос
        """
        assert self.response.json()["statusCode"] == 0
        assert self.response.json()["result"] == 2

    def test_error_status_2(self):
        """
        тест на проверку ответа при указании неверного количества ключей в теле
        """
        response = requests.post(
            "http://localhost:17678/api/multiplication", json={"x": 1}
        )
        assert response.json()["statusCode"] == 2
        assert "Не указаны необходимые параметры" in response.json()["statusMessage"]

    def test_error_status_3(self):
        """
        тест на проверку ответа при указании неверного формата одного из значений (float вместо int)
        """
        response = requests.post(
            "http://localhost:17678/api/multiplication", json={"x": 1, "y": 2.5}
        )
        assert response.json()["statusCode"] == 3
        assert (
            "Значения параметров должны быть целыми" in response.json()["statusMessage"]
        )

    def test_error_status_4(self):
        """
        тест на проверку ответа при указании числа превышающего допустимое
        """
        response = requests.post(
            "http://localhost:17678/api/multiplication", json={"x": 1, "y": 100**5}
        )
        assert response.json()["statusCode"] == 4
        assert (
            "Превышены максимальные значения параметров"
            in response.json()["statusMessage"]
        )

    def test_error_status_5(self):
        """
        тест на проверку ответа (статус кода и сообщения) при указании неверного метода HTTP
        """
        response = requests.get("http://localhost:17678/api/multiplication")
        assert response.json()["statusCode"] == 5
        assert (
            "Не верное имя задачи или тип HTTP запроса"
            in response.json()["statusMessage"]
        )


class TestCalculatorDivision:
    """
    Тесты для эндпоинта division
    """

    Calculator().start()
    response = requests.post(
        "http://localhost:17678/api/division", json={"x": 4, "y": 2}
    )

    def test_external_status_code(self):
        """
        тест на внешний статус код ответа от сервера
        """
        assert self.response.status_code == 200

    def test_response(self):
        """
        тест ответа на корректный запрос
        """
        assert self.response.json()["statusCode"] == 0
        assert self.response.json()["result"] == 2

    def test_error_status_1(self):
        """
        тест на проверку ответа при указании параметров, приводящих к ошибке вычисления
        """
        response = requests.post(
            "http://localhost:17678/api/division", json={"x": 4, "y": 0}
        )
        assert response.json()["statusCode"] == 1
        assert "Ошибка вычисления" in response.json()["statusMessage"]

    def test_error_status_2(self):
        """
        тест на проверку ответа при указании неверного количества ключей в теле
        """
        response = requests.post("http://localhost:17678/api/division", json={"x": 1})
        assert response.json()["statusCode"] == 2
        assert "Не указаны необходимые параметры" in response.json()["statusMessage"]

    def test_error_status_3(self):
        """
        тест на проверку ответа при указании неверного формата одного из значений (float вместо int)
        """
        response = requests.post(
            "http://localhost:17678/api/division", json={"x": 1, "y": 2.5}
        )
        assert response.json()["statusCode"] == 3
        assert (
            "Значения параметров должны быть целыми" in response.json()["statusMessage"]
        )

    def test_error_status_4(self):
        """
        тест на проверку ответа при указании числа превышающего допустимое
        """
        response = requests.post(
            "http://localhost:17678/api/division", json={"x": 1, "y": 100**5}
        )
        assert response.json()["statusCode"] == 4
        assert (
            "Превышены максимальные значения параметров"
            in response.json()["statusMessage"]
        )

    def test_error_status_5(self):
        """
        тест на проверку ответа (статус кода и сообщения) при указании неверного метода HTTP
        """
        response = requests.get("http://localhost:17678/api/division")
        assert response.json()["statusCode"] == 5
        assert (
            "Не верное имя задачи или тип HTTP запроса"
            in response.json()["statusMessage"]
        )


class TestCalculatorRemainder:
    """
    Тесты для эндпоинта remainder
    """

    Calculator().start()
    response = requests.post(
        "http://localhost:17678/api/remainder", json={"x": 3, "y": 2}
    )

    def test_external_status_code(self):
        """
        тест на внешний статус код ответа от сервера
        """
        assert self.response.status_code == 200

    def test_response(self):
        """
        тест ответа на корректный запрос
        """
        assert self.response.json()["statusCode"] == 0
        assert self.response.json()["result"] == 1

    def test_error_status_1(self):
        """
        тест на проверку ответа при указании параметров, приводящих к ошибке вычисления
        """
        response = requests.post(
            "http://localhost:17678/api/remainder", json={"x": 4, "y": 0}
        )
        assert response.json()["statusCode"] == 1
        assert "Ошибка вычисления" in response.json()["statusMessage"]

    def test_error_status_2(self):
        """
        тест на проверку ответа при указании неверного количества ключей в теле
        """
        response = requests.post("http://localhost:17678/api/remainder", json={"x": 1})
        assert response.json()["statusCode"] == 2
        assert "Не указаны необходимые параметры" in response.json()["statusMessage"]

    def test_error_status_3(self):
        """
        тест на проверку ответа при указании неверного формата одного из значений (float вместо int)
        """
        response = requests.post(
            "http://localhost:17678/api/remainder", json={"x": 1, "y": 2.5}
        )
        assert response.json()["statusCode"] == 3
        assert (
            "Значения параметров должны быть целыми" in response.json()["statusMessage"]
        )

    def test_error_status_4(self):
        """
        тест на проверку ответа при указании числа превышающего допустимое
        """
        response = requests.post(
            "http://localhost:17678/api/remainder", json={"x": 1, "y": 100**5}
        )
        assert response.json()["statusCode"] == 4
        assert (
            "Превышены максимальные значения параметров"
            in response.json()["statusMessage"]
        )

    def test_error_status_5(self):
        """
        тест на проверку ответа (статус кода и сообщения) при указании неверного метода HTTP
        """
        response = requests.get("http://localhost:17678/api/remainder")
        assert response.json()["statusCode"] == 5
        assert (
            "Не верное имя задачи или тип HTTP запроса"
            in response.json()["statusMessage"]
        )


class TestCalculatorFunctions:
    """
    тесты основных функций приложения (старт, стоп, перезапуск, смена адреса хоста/порта)
    """

    def test_start_without_params(self, calc_app):
        """
        тест запуска приложения со стандартными параметрами
        """
        calc_app.stop()
        res = calc_app.start()
        assert "Веб-калькулятор запущен" in res["stdout"]
        assert "127.0.0.1:17678" in res["stdout"]
        assert "" == res["stderr"]

    def test_start_with_host_and_port(self, calc_app):
        """
        тест запуска приложения с указанием кастомного хоста и порта
        """
        calc_app.stop()
        host = "127.0.0.1"
        port = "5000"
        res = calc_app.start(host, port)
        assert "Веб-калькулятор запущен" in res["stdout"]
        assert f"{host}:{port}" in res["stdout"]
        assert "" == res["stderr"]

    def test_start_with_host(self, calc_app):
        """
        тест запуска приложения только с указанием хоста
        """
        calc_app.stop()
        host = "127.0.0.1"
        res = calc_app.start(host)
        assert "Веб-калькулятор запущен" in res["stdout"]
        assert f"{host}" in res["stdout"]
        assert "" == res["stderr"]

    def test_start_when_is_active(self, calc_app):
        """
        тест запуска приложения, когда оно уже запущено
        """
        res = calc_app.start()
        assert "Сервер уже запущен" in res["stdout"]
        assert "" == res["stderr"]

    def test_start_with_wrong_params(self, calc_app):
        """
        тест ввода неверных параметров
        """
        calc_app.stop()
        host = "a.a.a.a"
        port = "0"
        res = calc_app.start(host, port)
        assert "Не удалось запустить Веб-калькулятор" in res["stdout"]
        assert f"{host}:{port}" in res["stdout"]
        assert "" == res["stderr"]

    def test_restart_when_is_active(self, calc_app):
        """
        тест рестарта приложения, если оно активно
        """
        calc_app.start()
        res = calc_app.restart()
        assert "Пытаемся остановить Веб-калькулятор" in res["stdout"]
        assert "Веб-калькулятор остановлен" in res["stdout"]
        assert "Запуск Веб-калькулятора" in res["stdout"]
        assert "Веб-калькулятор запущен" in res["stdout"]
        assert "" == res["stderr"]

    def test_restart_when_is_not_active(self, calc_app):
        """
        тест рестарта приложения, если оно не активно
        """
        calc_app.stop()
        res = calc_app.restart()
        assert (
            'Веб-калькулятор не запущен. Используйте команду "start"' in res["stdout"]
        )
        assert "" == res["stderr"]

    def test_stop(self, calc_app):
        """
        тест остановки приложения
        """
        res = calc_app.stop()
        assert "Пытаемся остановить Веб-калькулятор" in res["stdout"]
        assert "Веб-калькулятор остановлен" in res["stdout"]
        assert "" == res["stderr"]
