from random import randint


def run():
  mask = randint(100, 1000000)
  val = mask

  while val > 0:
    print('iter:', val, bin(val)[2:])
    val = (val-1) & mask


run()
