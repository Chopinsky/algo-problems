"""Tower of Hanoi helpers and a small CLI demo.

This module provides a clean, modular implementation of the Tower of
Hanoi algorithm. The core function `hanoi_moves` returns a list of moves,
and `hanoi_moves_gen` yields moves lazily. A small CLI is available when
running the file directly.

Each move is represented as a tuple: (disk, source, destination).
"""

from typing import List, Tuple, Iterator
import argparse


Move = Tuple[int, str, str]


def hanoi_moves(n: int, source: str = "A", dest: str = "C", aux: str = "B") -> List[Move]:
  """Return the list of moves to solve Tower of Hanoi for n disks.

  Args:
    n: Number of disks (must be >= 1).
    source: Name of source peg.
    dest: Name of destination peg.
    aux: Name of auxiliary peg.

  Returns:
    A list of moves where each move is (disk, source, dest).

  Raises:
    ValueError: if n < 1.
  """
  if n < 1:
    raise ValueError("n must be >= 1")

  moves: List[Move] = []

  def _move(disk: int, s: str, d: str, a: str) -> None:
    if disk == 1:
      moves.append((disk, s, d))
      return
    
    _move(disk - 1, s, a, d)
    moves.append((disk, s, d))
    _move(disk - 1, a, d, s)

  _move(n, source, dest, aux)
  return moves


def hanoi_moves_gen(n: int, source: str = "A", dest: str = "C", aux: str = "B") -> Iterator[Move]:
  """Generator that yields moves for Tower of Hanoi.

  This is useful when you don't want to store all moves in memory.
  """
  if n < 1:
    raise ValueError("n must be >= 1")

  def _gen(disk: int, s: str, d: str, a: str):
    if disk == 1:
      yield (disk, s, d)
      return
    
    yield from _gen(disk - 1, s, a, d)
    yield (disk, s, d)
    yield from _gen(disk - 1, a, d, s)

  yield from _gen(n, source, dest, aux)


def print_moves(moves: Iterator[Move]) -> None:
  """Print moves with a step counter.

  Accepts either an iterator/generator or a list.
  """
  for step, (disk, src, dst) in enumerate(moves, start=1):
    print(f"step {step} -> move {disk} from {src} to {dst}")


def _validate_move_count(n: int, moves_count: int) -> bool:
  """Validate that moves_count equals 2**n - 1."""
  return moves_count == (2 ** n) - 1


def _cli() -> None:
  parser = argparse.ArgumentParser(description="Tower of Hanoi demo")
  parser.add_argument("n", nargs="?", type=int, default=8, help="number of disks (default: 8)")
  parser.add_argument("--print", dest="do_print", action="store_true", help="print all moves")
  parser.add_argument("--gen", dest="use_gen", action="store_true", help="use generator (no list allocation)")
  args = parser.parse_args()

  n = args.n
  if args.use_gen:
    moves_iter = hanoi_moves_gen(n)
    if args.do_print:
      print_moves(moves_iter)

    else:
      # count moves from generator to validate
      count = sum(1 for _ in moves_iter)
      print(f"Generated {count} moves")
      assert _validate_move_count(n, count), "unexpected move count"

  else:
    moves = hanoi_moves(n)
    if args.do_print:
      print_moves(moves)
      
    else:
      print(f"Computed {len(moves)} moves")
      assert _validate_move_count(n, len(moves)), "unexpected move count"


if __name__ == "__main__":
  _cli()


