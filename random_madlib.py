import random
from ready_madlibs import nosferatu, sample

if __name__ == "__main__":
  pego = random.choice([nosferatu, sample])
  pego.madlib()