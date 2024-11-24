import random


def ab():
    for i in range(5):
        print(f"{i = }")


def my_mul(data: list) -> float:
    result = 1
    for num in data:
        result = result * num
    return result


def fast_power(x: float, y: int) -> int:
    """
    Return x^y with O(log(n)) Time Complexity.
    """
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y == -1:
        return 1 / x
    else:
        ans = fast_power(x, y // 2)
        if y % 2 == 0:
            return ans * ans
        else:
            return ans * ans * x


if __name__ == "__main__":
    ab()

    # my_mul(12)
    print("my_mul(1*2): ", my_mul((1, 2, 3)))
    # print("my_mul(1*2): ", my_mul(12))

    # fast_power(2, 10)
    print("fast_power(2, 10): ", fast_power(2, 10))

    data = {"a": [1, 2], "b": [3, 4]}
    print("data: ", data)

    for n in range(1, 22):
        print(f"{n = }", end=" ")
