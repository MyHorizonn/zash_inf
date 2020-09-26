import math


def main():
    ans = []
    print("y_zab")
    y_zab = float(input())
    print("x_zab")
    x_zab = float(input())
    print("y_win")
    y_win = float(input())
    print("x_win")
    x_win = float(input())
    print("x_win1")
    x_win1 = float(input())
    print("y_info")
    y_info = float(input())
    print("x_info")
    x_info = float(input())
    print("p1")
    p1 = float(input())
    print("p2")
    p2 = float(input())
    print("k1")
    k1 = float(input())
    print("k2")
    k2 = float(input())
    for i in reversed(range(1, int(y_zab) + 1)):
        if i == int(y_zab):
            print("=" * int(x_zab))
        elif i == y_win:
            print(" " * int(x_win - 1) + "-" + " " * int(x_win1 - x_win) + "-" + " " * int(x_zab - x_win1 - 2) + "|")
        elif i == y_info:
            print(" " * int(x_info - 1) + "#" + " " * int(x_zab - x_info - 1) + "|")
        else:
            print(" " * int(x_zab - 1) + "|")
    l21 = math.sqrt(((y_win - y_info) ** 2) + (math.fabs(x_win - x_info) ** 2))
    l22 = math.sqrt(((y_win - y_info) ** 2) + (math.fabs(x_win1 - x_info) ** 2))
    for i in range(1, 100):
        l11 = math.sqrt(((y_zab - y_win) ** 2) + (math.fabs(x_win - i) ** 2))
        l12 = math.sqrt(((y_zab - y_win) ** 2) + (math.fabs(x_win1 - i) ** 2))
        ans.append([(k1 / l11 * p1 * k2 / l21), i, 1])
        ans.append([(k1 / l12 * p2 * k2 / l22), i, 2])
    return min(ans)


print(main())
