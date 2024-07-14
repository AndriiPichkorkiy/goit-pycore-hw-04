from helpers import run_with_try_except


def total_salary(path: str) -> tuple[int, int] | None:
    # preprare main code to run
    def fun() -> list[int] | None:
        with open(path, "r", encoding="utf-8") as file:
            # get lines as list
            salaries_data = file.readlines()

            # validation to empty file
            if len(salaries_data) == 0:
                print("Error: file is empty")
                return

            # get salaries from lines and convert to integer
            # ignore empty lines
            salaries_list = [
                int(salarie.split(",")[1].strip())
                for salarie in salaries_data
                if len(salarie.strip())
            ]

            # total salary
            total = sum(salaries_list)
            # avarage without float
            average = total // len(salaries_list)

            return [total, average]

    # run the function with Exception Handling
    return run_with_try_except(fun)


total, average = total_salary("./salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
