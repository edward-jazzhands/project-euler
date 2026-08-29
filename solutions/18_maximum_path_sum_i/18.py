"""
By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

           3
          7 4
         2 4 6
        8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                            75
                          95  64
                        17  47  82
                      18  35  87  10
                    20  04  82  47  65
                  19  01  23  75  03  34
                88  02  77  73  07  63  67
              99  65  04  28  06  16  70  92
            41  41  26  56  83  40  80  70  33
          41  48  72  33  47  32  37  16  94  29
        53  71  44  65  25  43  91  52  97  51  14
      70  11  33  28  77  73  17  78  39  68  17  57
    91  71  52  38  17  14  91  43  58  50  27  29  48
  63  66  04  68  89  53  67  30  73  16  69  87  40  31
04  62  98  27  23  09  70  98  73  93  38  53  60  04  23

NOTE: As there are only 16384 routes, it is possible to solve this problem 
by trying every route. However, Problem 67, is the same challenge with a triangle 
containing one-hundred rows; it cannot be solved by brute force, and requires
a clever method! (c;
"""

from functools import cache
import time


triangle_str = """\
                            75
                          95  64
                        17  47  82
                      18  35  87  10
                    20  04  82  47  65
                  19  01  23  75  03  34
                88  02  77  73  07  63  67
              99  65  04  28  06  16  70  92
            41  41  26  56  83  40  80  70  33
          41  48  72  33  47  32  37  16  94  29
        53  71  44  65  25  43  91  52  97  51  14
      70  11  33  28  77  73  17  78  39  68  17  57
    91  71  52  38  17  14  91  43  58  50  27  29  48
  63  66  04  68  89  53  67  30  73  16  69  87  40  31
04  62  98  27  23  09  70  98  73  93  38  53  60  04  23
"""

triangle1 = triangle_str.splitlines()
triangle2 = [row.strip() for row in triangle1]
triangle3 = [row.split("  ") for row in triangle2]
triangle4 = [[int(x) for x in row] for row in triangle3]

@cache
def triangle_traverse(row: int, col: int):

    value = triangle4[row][col]
    
    # on the last line, return the cell value
    if row + 1 >= len(triangle4):
        return value

    # on index 0, the two under are i=0 and i=1
    # on index 2, the two under are i=2 and i=3. etc.
    path1 = triangle_traverse(row+1, col)
    path2 = triangle_traverse(row+1, col+1)

    # === VISAULIZER ===
    for i, rowx in enumerate(triangle3):
        spaces = len(triangle3) - i
        print("  " * spaces, end="")
        for c, cell in enumerate(rowx):
            if i == row and c == col:
                print(f"\033[34m{cell}\033[0m", end="")
            else:
                print(cell, end="")
            print("  ", end="")
        print()
    print()

    print(f"{path1 = } | {path2 = }")
    print()
    time.sleep(0.10)
    # === END VISUALIZER ===

    return value + max(path1, path2)

print(triangle_traverse(0, 0))