class Main:

    def __init__(self, r_color, height):
        self.color = r_color
        self.height = height

    def __str__(self):
        return 'homestr' + self.color + 'height = ' + str(self.height)

    def __len__(self):
        return self.height

    def __eq__(self, other):
        if self.height >= other.height:
            return True
        else:
            return False
        
    def __repr__(self):
        return "Main('" + str(self.color) + "', " + str(self.height) + ")"

    def func(self, r_color):
        self.color = r_color

    def printc(self):
        print(self.color)

main = Main('green',10)
#main.func('lightgreen')
main.printc()
print(str(main))
print(len(main))
print(repr(main))

main1 = Main('pinkod',14)
#main1.func('red')
main1.printc()

print(main == main1)
