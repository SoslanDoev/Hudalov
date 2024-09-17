""" Решение дифф. урав-ий """

""" Подключение библиотек """
import os
from sympy import *
""" END Подключение библиотек """

""" Функция очистки консоля """
def CLEAR(): os.system("cls")

def app():
    """ Главная функция запуска """
    def appInner_1():
        """ Функция для решения задачи на 225 странице """
        # Первый способ
        x = symbols("x")
        y = Function("y")
        eq = diff(y(x),x)-(exp(sqrt(x)-2)/sqrt(x))
        res = dsolve(eq,y(x)).simplify()
        print("res: ", res)
        # Второй способ
        z = exp(sqrt(x)-2)/sqrt(x)
        res = integrate(z,x).simplify()
        print(f"res: {res}")

    def appInner_2():
        """ Функция для решения задачи на 226 странице """
        x = symbols("x")
        y = Function("y")
        eq = (x+1)*diff(y(x),x)+x*y(x)
        res = dsolve(eq, y(x))
        print(f"res: {res}")    

    def appInner_3():
        """ Функция для решение задачи на 227 странице """
        x = symbols("x")
        y = Function("y")
        eq = x*diff(y(x),x)-y(x)-sqrt(y(x)**2-x**2)
        res = dsolve(eq, y(x))
        print(res)
    
    def appInner_4():
        """ Функция для решение задачи на 228 странице """
        z = symbols("z")
        fz = (1+z**2)/z**3
        I1 = integrate(fz)
        print(I1)

    def appInner_5():
        """ Функция для решение задачи на 231 странице """
        x = symbols("x")
        y = Function("y")
        eq = diff(y(x),x)-y(x)/x - (x**4)*(y(x) ** 2)
        res = dsolve(eq, y(x))
        print(f"res: {res}")

    def appInner_6():
        """ Функция для решение задачи на 233 странице """
        x = symbols("x")
        u = Function("u")
        eq = diff(u(x),x)+4*u(x)/x+u(x)**2
        des = dsolve(eq, u(x))
        res = des.simplify()
        print("res: ", res)

if (__name__ == "__main__"):
    CLEAR() # Очистить консоль
    app() # Главная функция