"""
相传在古印度圣庙中，有一种被称为汉诺塔(Hanoi)的游戏。
该游戏是在一块铜板装置上，有三根杆(编号A、B、C)，在A杆自下而上、由大到小按顺序放置64个金盘。
游戏目标：
    把A杆上的金盘全部移到C杆上，并仍保持原有顺序叠好。操作规则：每次只能移动一个盘子，
    并且在移动过程中三根杆上都始终保持大盘在下，小盘在上，操作过程中盘子可以置于A、B、C任一杆上。
分析思路：
    1.把n-1个金盘从A经过C移动到B；
    2.将第n个金盘从A移动到C；
    3.把n-1个金盘从B经过A移动到C。
"""


def hanoi(n: int, a: str, b: str, c: str) -> None:
    """
    hanoi求解
    :param n: 盘子个数
    :param a: 开始柱子
    :param b: 中间柱子
    :param c: 目标柱子
    :return: None
    """
    if n > 0:
        hanoi(n - 1, a, c, b)
        print(f"将最上面的金盘从{a}移动到{c}")
        hanoi(n - 1, b, a, c)


hanoi(3, "A", "B", "C")