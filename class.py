class A:
    def __init__(self, egor, katya):
        self.egor = egor
        self.katya = katya

    def school(self):
        print("school of class A")

    def vpk(self):
        print("vpk of class A")

    def mgy(self):
        print("mgy of class A")


class B(A):
    def __init__(self, egor, katya, olya):
        super().__init__(egor, katya)
        self.olya = olya

    def mgy(self):
        print("mgy of class B")


class C(A):
    def __init__(self, egor="default_egor", katya="default_katya"):
        super().__init__(egor, katya)

    def avtobus(self):
        print("avtobus of class C")

    def tt(self):
        print("tt of class C")


a = A("egor_value", "katya_value")
b = B("egor_value", "katya_value", "olya_value")
c = C()

a.school()
a.vpk()
a.mgy()

b.school()
b.vpk()
b.mgy()

c.school()
c.vpk()
c.mgy()
c.avtobus()
c.tt()