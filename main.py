def sum(nums):
    result = 0
    for num in nums:
        result = result + num
    return result

def subtraction(nums):
    result = nums[0]
    for num in range(1, len(nums)):
        result = result - nums[num]
    return result
def division(nums):
    result = nums[0]
    for num in range(1, len(nums)):
        result = result/nums[num]
    return result

def multiplication(nums):
    result = 1
    for num in nums:
        result = result * num
    return result

print("Calculator")
print("1 - Sum")
print("2 - Subtraction")
print("3 - Division")
print("4 - Multiplication")

option = int(input("Choose your operation: "))

if option > 0 and option < 5:

    nums = []
    num1 = int(input("Provide the first number: "))
    nums.append(num1)
    num2 = int(input("Provide the second number: "))
    nums.append(num2)

    if option == 1:
        print("The result is:", sum(nums))
    elif option == 2:
        print("The result is:", subtraction(nums))
    elif option == 3:
        print("The result is:", division(nums))
    elif option == 4:
        print("The result is:", multiplication(nums))

else:
    print("This option is not valid!")


