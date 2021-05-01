import wtxl
import wtx


v = int(input('1 - Ввод был через эксель, 2 - Хочу ввести через программу'"\n"))
if v == 1:
    wtx.ex()
elif v == 2:
    wtxl.no_ex()
else:
    print("Неверный выбор")


