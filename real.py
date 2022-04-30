
#!/usr/bin/python3

__version__ = '0.001b'
__author__ = 'Leonardo Sousa'
_change_log = ''

class Real():

    def __init__(self):
        pass
    def string_to_f(x):
        # metodo para converte os formato real strings em float para calculos
        s = x[0:1]
        x = list(x)[4:]
        c = ''
        for i in x:
            if i == '.':
                pass
            elif i == ',':
                c += '.'
            else:
                c += i
        if s == '-':
            c = (float(c) - (2 * float(c)))
            return c
        elif s == ' ':
            return float(c)

    def float_to_s(x):
        # função que add os caracters em R$ no valor

        s = str(x)[0:1]
        if type(x) == float:
            x = str('{:.2f}'.format(x))
        c = ''
        for i in x:
            if i == '.':
                pass
            elif i == '-':
                pass
            else:
                c += i
            x = list(c)

        if s == '-':
            c = '-R$ '
        else:
            c = ' R$ '

        cont = 1

        # 15 caracters
        if len(x) == 15:
            for i in x:
                if cont == 1:
                    c += i + '.'
                elif cont == 4:
                    c += i + '.'
                elif cont == 7:
                    c += i + '.'
                elif cont == 10:
                    c += i + '.'
                elif cont == 13:
                    c += i + ','
                else:
                    c += i
                cont += 1

        # 14 caracters
        elif len(x) == 14:
            for i in x:
                if cont == 3:
                    c += i + '.'
                elif cont == 6:
                    c += i + '.'
                elif cont == 9:
                    c += i + '.'
                elif cont == 12:
                    c += i + ','
                else:
                    c += i
                cont += 1

        # 13 caracters
        elif len(x) == 13:
            for i in x:
                if cont == 2:
                    c += i + '.'
                elif cont == 5:
                    c += i + '.'
                elif cont == 8:
                    c += i + '.'
                elif cont == 11:
                    c += i + ','
                else:
                    c += i
                cont += 1

        # 12 caracters
        elif len(x) == 12:
            for i in x:
                if cont == 1:
                    c += i + '.'
                elif cont == 4:
                    c += i + '.'
                elif cont == 7:
                    c += i + '.'
                elif cont == 10:
                    c += i + ','
                else:
                    c += i
                cont += 1

        # 11 caracters
        elif len(x) == 11:
            for i in x:
                if cont == 3:
                    c += i + '.'
                elif cont == 6:
                    c += i + '.'
                elif cont == 9:
                    c += i + ','
                else:
                    c += i
                cont += 1

        # 10 caracters
        elif len(x) == 10:
            for i in x:
                if cont == 2:
                    c += i + '.'
                elif cont == 5:
                    c += i + '.'
                elif cont == 8:
                    c += i + ','
                else:
                    c += i
                cont += 1
        # 9 caracters
        elif len(x) == 9:
            for i in x:
                if cont == 1:
                    c += i + '.'
                elif cont == 4:
                    c += i + '.'
                elif cont == 7:
                    c += i + ','
                else:
                    c += i
                cont += 1

        # 8 caracters
        elif len(x) == 8:
            for i in x:
                if cont == 3:
                    c += i + '.'
                elif cont == 6:
                    c += i + ','
                else:
                    c += i
                cont += 1

        # 7 caracters
        elif len(x) == 7:
            for i in x:
                if cont == 2:
                    c += i + '.'
                elif cont == 5:
                    c += i + ','
                else:
                    c += i
                cont += 1

        # 6 caracters
        elif len(x) == 6:
            for i in x:
                if cont == 1:
                    c += i + '.'
                elif cont == 4:
                    c += i + ','
                else:
                    c += i
                cont += 1

        # 5 caracters
        elif len(x) == 5:
            for i in x:
                if cont == 3:
                    c += i + ','
                else:
                    c += i
                cont += 1

        # 4 caracters
        elif len(x) == 4:
            for i in x:
                if cont == 2:
                    c += i + ','
                else:
                    c += i
                cont += 1

        # 3 caracters
        elif len(x) == 3:
            for i in x:
                if cont == 1:
                    c += i + ','
                else:
                    c += i
                cont += 1

        return c

    def add_number(x, y):

        x = str('{:.2f}'.format(x))
        c = ''
        for i in x:
            if i == '.':
                pass
            else:
                c += i
        x = c
        x += str(y)
        if x[0] == '0':
            x = list(x[1:])
            x = Real.float_to_s( x )
        return x 





a = 456465464640.15
b = -11.15
aa = 195.45
c = ' R$ 200,15'
d = '-R$ 4.100.100,15'   


print( Real.string_to_f(d) )