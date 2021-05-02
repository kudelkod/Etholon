import wtxl
import wtx


def choise():
    ch = int(input('1 - Ввод был через эксель, 2 - Хочу ввести через программу'"\n"))
    if ch == 1:
        wtx.ex()
    elif ch == 2:
        wtxl.no_ex()
    else:
        print("Неверный выбор")
        choise()