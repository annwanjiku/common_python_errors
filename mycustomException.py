number = input("Enter a number : ")

class CustomException(Exception):
    pass

def calculate(num):
    try:
        num = int(num)
        result = (num)*2
        print(result)
        return result
    except Exception as e:
        raise CustomException(f"An error {e} occured")
    finally:
        print("\nExiting....\n")


try:
    calculate(num=number)

except CustomException as e:
    print(e)
