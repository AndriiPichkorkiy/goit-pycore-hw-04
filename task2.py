from pprint import pprint
from helpers import run_with_try_except


def get_cats_info(path: str) -> list[dict[str, str | int]] | None:
    # preprare main code to run
    def fun() -> list[dict[str, str | int]] | None:
        with open(path, "r", encoding="utf-8") as file:
            # get lines as list and remove the next line symbol
            cats_data = [line.rstrip() for line in file.readlines()]

            # validation to empty file
            if len(cats_data) == 0:
                print("Error: file is empty")
                return

            # get id, name and age of each cat
            # ignore empty lines
            cats_raw_list = [cat.split(",") for cat in cats_data if len(cat)]

            cats_info = []
            for cat in cats_raw_list:
                cats_info.append(
                    {
                        "id": cat[0],
                        "name": cat[1],
                        "age": int(cat[2]),
                    }
                )
            return cats_info

    # run the function with Exception Handling
    return run_with_try_except(fun)


cats_info = get_cats_info("./cats_file.txt")
pprint(object=cats_info, sort_dicts=False)
