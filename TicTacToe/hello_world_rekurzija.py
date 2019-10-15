
def hello_world_rekurzija(ponavljanje=0): #ako ne stavis varijablu, onda je 0
    print("Hello wordl", ponavljanje)
    hello_world_rekurzija(ponavljanje + 1)


def hello_world_rekurzija2(ponavljanje = 0):
    hello_world_rekurzija2(ponavljanje + 1)
    print("Hello World ", ponavljanje)


def hello_world_rekurzija3(ponavljanje = 0):
    print("Hello World", ponavljanje)
    if ponavljanje != 10:
        hello_world_rekurzija3(ponavljanje + 1)

def hello_world_rekurzija4(ponavljanje = 0):
    if ponavljanje != 10:
        hello_world_rekurzija4(ponavljanje + 1)
    print("hello world",ponavljanje)


if __name__ == '__main__':
    # hello_world_rekurzija()
    # hello_world_rekurzija2()
    # hello_world_rekurzija3()
    hello_world_rekurzija4()