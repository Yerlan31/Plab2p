from lab_python_oop.classes import Rect, Circle, Square
import matplotlib.pyplot as plt


def main():
    N = 5
    sqr1 = Square(N, 'красный')
    rect1 = Rect(N, N, 'зеленый')
    cir1 = Circle(N, 'голубой')
    print(sqr1)
    print(rect1)
    print(cir1)
    circle1 = plt.Circle((0, 0), N, color='r')
    rect1 = plt.Rectangle((N, 0), N, N, 0, color='b')
    rect2 = plt.Rectangle((2 * N, 0), N, N, 0, color='g')
    fig, ax = plt.subplots()

    ax.set_xlim([-5, 15])
    ax.set_ylim([-5, 15])
    ax.add_patch(circle1)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    plt.show()
#    fig.savefig('plotcircles.png')


main()
