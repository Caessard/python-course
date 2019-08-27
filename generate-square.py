import turtle

#Create lines and turn 90 degrees

def main():
    window = turtle.Screen()
    caesar = turtle.Turtle()

    make_square(caesar)

    turtle.mainloop()


def make_square(caesar):
    lenght = int(input('Tamaño del cuadrado: '))
    for i in range(4):
        make_line_and_turn(caesar, lenght)
    

def make_line_and_turn(caesar, lenght):
    caesar.forward(lenght)
    caesar.left(90)

if __name__ == '__main__':
    main()



