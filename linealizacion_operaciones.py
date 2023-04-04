import unittest

def linealizacion(a, b, c, d, Vo, t):
    e = ((c**2)+b)/d
    x=Vo*t+((a*(t**2))/2)
    y = (a/(a-b))/(a/(a-b))
    z = (a+b-(c/(a*d)))/(a-b*(c/d))
    w = ((a/b)+(b/c))/((a/b)+(c/d))
    return [e, x, y, z, w]


class CajaTest(unittest.TestCase):
    def test_columna1(self):
        a = 1
        b = 2
        c = 4
        d = -2
        Vo = 8
        t = 7

        resultado  = linealizacion(a, b, c, d, Vo, t)
        self.assertEqual(resultado, [-9.0, 80.5, 1.0, 1.0, -0.6666666666666666])

    def test_columna2(self):
        a = -2
        b = 5
        c = 2
        d = 6
        Vo = 0.8
        t = 17

        resultado  = linealizacion(a, b, c, d, Vo, t)
        self.assertEqual(resultado, [1.5, -275.4, 1, -0.8636363636363636, -31.499999999999982])

    def test_columna3(self):
        a = 3
        b = -2
        c = 10
        d = 1
        Vo = 1
        t = 2

        resultado  = linealizacion(a, b, c, d, Vo, t)
        self.assertEqual(resultado, [98.0, 8.0, 1.0, -0.10144927536231885,-0.19999999999999998])

        
if __name__ == '__main__':
    unittest.main()


