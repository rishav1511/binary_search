import turtle
t=turtle.Turtle()
t.screen.bgcolor('black')
t.pensize(20)
t.color('green')
t.left(900)
t.backward(1000)
t.speed(2000)
t.shape('turtle')

def tree(i):
    if i<10:
        return
    else:
        t.forward(i)
        t.color('orange')
        t.circle(20)
        t.color('brown')
        t.left(300)
        tree(30*i/40)
        t.left(300)
        t.backward(i)

tree(1000)
turtle.done()