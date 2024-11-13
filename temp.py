from typing_extensions import reveal_type

my_list: list[int | str] = [1, 2, 3, "11"]

my_dict: dict[str, int] = {"a": 1}

my_tuple: tuple[int, ...] = (
    1,
    2,
    3,
)

reveal_type(my_list)

# def number(a : list[int] ):
#     return a
