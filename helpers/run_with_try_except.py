from types import FunctionType

def run_with_try_except(fun: FunctionType) -> any:
    try:
        return fun()
    except FileNotFoundError as err:
        print("Error: " + err.strerror)
    except UnicodeError as err:
        print("Error: " + err.args[0])
    except (IndexError, ValueError) as err:
        print("Error: content in the file is not valid")
    except BaseException as err:
        print("Unhandled error, check path and file structure")
        print(err)