import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import random as r


def shift_up(arr):
    return np.vstack([arr[1:], np.zeros((1, arr.shape[1]), int)])


def shift_down(arr):
    return np.vstack([np.zeros((1, arr.shape[1]), int), arr[:-1]])


def shift_left(arr):
    return np.hstack([arr[:, 1:], np.zeros((arr.shape[0], 1), int)])


def shift_right(arr):
    return np.hstack([np.zeros((arr.shape[0], 1), int), arr[:, :-1]])


def shift_up_left(arr):
    return shift_left(shift_up(arr))


def shift_up_right(arr):
    return shift_right(shift_up(arr))


def shift_down_left(arr):
    return shift_left(shift_down(arr))


def shift_down_right(arr):
    return shift_right(shift_down(arr))


def calc_neighbors(arr):
    return \
        shift_up(arr) + \
        shift_down(arr) + \
        shift_left(arr) + \
        shift_right(arr) + \
        shift_up_left(arr) + \
        shift_up_right(arr) + \
        shift_down_left(arr) + \
        shift_down_right(arr)


def calc_neighbors2(arr):
    # trying to do neighbors calc using usual nested fors... but buggy!

    the_copy = arr[:, :] # clone arr
    for row in range(HEIGHT):
        for col in range(WIDTH): # recall slicing never "indexes out of range"
            the_copy[row, col] = arr[row - 1:row + 2, row - 1:row + 2].sum() - arr[row, col]

    return the_copy


def build_glider(atx, aty, orientation):
    global life

    if orientation == 0:
        life[atx, aty] = 1
        life[atx + 2, aty] = 1
        life[atx + 1, aty + 1] = 1
        life[atx + 1, aty + 2] = 1
        life[atx + 2, aty + 1] = 1

    elif orientation == 1:
        life[atx + 2, aty] = 1
        life[atx, aty + 1] = 1
        life[atx + 1, aty + 1] = 1
        life[atx + 1, aty + 2] = 1
        life[atx + 2, aty + 2] = 1

    elif orientation == 2:
        life[atx + 1, aty] = 1
        life[atx + 2, aty] = 1
        life[atx, aty + 1] = 1
        life[atx + 1, aty + 1] = 1
        life[atx + 2, aty + 2] = 1

    elif orientation == 3:
        life[aty, atx] = 1
        life[aty + 2, atx] = 1
        life[aty + 1, atx + 1] = 1
        life[aty + 1, atx + 2] = 1
        life[aty + 2, atx + 1] = 1

def set_board_size(N, M):
    global HEIGHT
    global WIDTH

    HEIGHT = N
    WIDTH = M
    print('setting board dimensions to: (%d,%d)' % (N, M))


def update_life():
    global life

    # print("generation %d:\n" % frame_number, life)

    nbors = calc_neighbors(life)

    # nbors = calc_neighbors2(life) # alt method of neighbors calc (fail!)
    # print(len([1 for row in range(HEIGHT)
    #              for col in range(WIDTH)
    #              if nbors[row,col]==nbors2[row,col] ]))

    life = ((life & ((nbors == 2) | (nbors == 3))) + ((~life) & (nbors == 3)))
    # print (f'number born:{(nbors==3 & (~life)).sum()}')

def build_init_life_stripes():
    global WIDTH, HEIGHT
    global life

    life = np.zeros((HEIGHT, WIDTH), dtype=int)

    for row in range(0, HEIGHT//2, 2): # set every other row's cells to 1
        for col in range(WIDTH//2):
            life[row, col] = 1
            life[HEIGHT - 1 - row, col] = 1
            life[row, WIDTH-1-col] = 1
            life[HEIGHT-1-row, WIDTH-1-col] = 1


# replace above by each of variations below: different stripe strategies

    # variation 1: set 1000 random locations to 1 within inner 1/2 square

    # for count in range(1000): # set 1000 random cells to 1 within inner square
    #     life[r.randint(HEIGHT // 4, 3 * HEIGHT // 4), r.randint(WIDTH // 4, 3 * WIDTH // 4)] = 1

    # variation 2: set 1000 random locations to 1

    # for count in range(1000):
    # 	life[r.randint(0, HEIGHT-1), r.randint(0, WIDTH-1)] = 1

    # variation 3: initialize 4/5 inner square to stripes (every other row)

    # for row in range(HEIGHT // 5, 4*HEIGHT // 5,2):
    # 	for col in range(WIDTH // 5, 4*WIDTH // 5):
    #         life[row, col] = 1;

def build_init_life_gliders():
    global WIDTH, HEIGHT
    global life

    life = np.zeros((HEIGHT, WIDTH), dtype=int)

    # build 5 randomly-placed gliders, heading in one of four cardinal direction (NWSE)
    for count in range(5):
        build_glider(r.randint(10, WIDTH - 10), r.randint(10, HEIGHT - 10), r.randint(0, 3))

    # replace above by each of variations below: different glider placement strategies

    # variation 1: build spaced gliders within inner square, heading southeast

    # for row in range(HEIGHT // 3, HEIGHT * 2 // 3, 5):
    #     build_glider(row, row, 0) # random.randint(0,3))

    # variation 2: build spaced gliders within 2/3 inner square, heading northwest

    # for row in range(2 * WIDTH // 3, WIDTH // 3, -5):
    #     build_glider(row, HEIGHT - row, 2) # random.randint(0,3))
    # print('go')


# input("ENTER to continue:")

def init():
    im.set_data(life)
    return im


def animate(i): # Matplotlib supplies the arg
    global im
    global generation

    update_life()
    generation += 1
    if generation % 100 == 0: print(generation)

    im.set_data(life)
    return im


global life
global im
global generation

generation = 0
set_board_size(100, 100)  # change the board size here

### two different ways of initializing board follow...

build_init_life_gliders()  ## build randomly placed gliders
# build_init_life_stripes()  ## build board with alternating stripes

# plt.style.use('classic')
fig = plt.figure()
im = plt.imshow(life)  # , cmap='gist_gray_r')

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=2000,
                               interval=200)  # 200 ms between animation
# edit interval to change animation speed

plt.show()
