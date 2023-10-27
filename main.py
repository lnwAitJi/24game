import random
import time
import itertools
import os

# x____________________x #
# Dev Settings Zone:
showAns = True
notClear = False
# x____________________x #

def display(num, game_ans):
    for i in range(4):
        display_var = num[i]
        if display_var == -99:
            display_var = "-"
        print(f" | {display_var}")
    if showAns:
        print(f"[Dev] Answer: {game_ans}")
    return

def checker(slot1, num, toggle=True):
    for i in range(len(num)):
        if slot1 == num[i]:
            if toggle: return i
            else: return True
        continue
    if toggle: return -1
    else: return False

def cls():
    if not notClear:
        print("\n" * 30)
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'nt':
            os.system('cls')

def is_str(s):
    try:
        num = int(s)
        return False
    except ValueError:
        try:
            float(s)
            return False
        except ValueError:
            return True

def check(num1, num2, num3, num4):
    valid_operations = ['+', '-', '*', '/']

    permutations = itertools.permutations([num1, num2, num3, num4])

    for p in permutations:
        for ops in itertools.product(valid_operations, repeat=3):
            expression = f"({p[0]}){ops[0]}({p[1]}){ops[1]}({p[2]}){ops[2]}({p[3]})"
            try:
                result = eval(expression)
                if abs(result - 24) < 1e-6:
                    return expression
            except ZeroDivisionError:
                pass

    return "Cannot calculate 24 using + - * / with these numbers."


def main():
    cls()
    op_array = ["+", "-", "×", "÷"]
    print("×——————————————————————————————————×\nGenerating numbers, please wait..\n")
    while True:
        clone_num = [random.randint(1, 9) for _ in range(4)]
        num = clone_num.copy()
        if not num.count(0) > 0:
            solution = check(num[0], num[1], num[2], num[3])
            game_ans = check(num[0], num[1], num[2], num[3])
            if solution != "Cannot calculate 24 using + - * / with these numbers.":
                print(f"Solution found for ({num[0]}:{num[1]}:{num[2]}:{num[3]}) ✓")
                break
            else:
                print(f"No solution found for ({num[0]}:{num[1]}:{num[2]}:{num[3]}) ×")
                time.sleep(0.005)
        else:
            print("Game Interval Random 0 (pass)")
    print("×——————————————————————————————————×")
    time.sleep(2)
    while True:
        cls()
        print("×——————————————————————————————————×")
        if num.count(-99) >= 3:
            if 24 in num:
                print(f"You solved the 24 Game!\nThanks for playing!\nComputer Way: {game_ans}\nYou Way: idk how to save later ok?")
                print("×——————————————————————————————————×")
                break
            else:
                while True:
                    print(f"Game Over Your Number ran out :--;")
                    var = input("1) Try Again - Reset all number index\n2) Show Answer - Show the computer answer\n(1/2) > ")
                    if var == "2": print(f"Computer Answer: {game_ans}"); break
                    if var == "1":
                        print(f"Ok wait a moment [Reset number..] : {clone_num[0]}, {clone_num[1]}, {clone_num[2]}, {clone_num[3]}")
                        time.sleep(3)
                        num = clone_num
                        break
                    else:
                        print(f"Invalid Input '{var}'\n* Please type only (1/2)")
                        time.sleep(3)
        print("24 Game:\nSlot | Number")
        display(num, game_ans)
        print("[Calculate: [_ _ _ = __]")
        while True:
            try:
                slot1 = int(input("Enter your number\n> "))
                if slot1 == -99:
                    print("Invalid Input. That input already taken")
                else:
                    if checker(slot1, num, False):
                        break
            except ValueError:
                print("Invalid Input. Please enter a number.")
        slot_1 = checker(slot1, num, True)
        save1 = num[slot_1]
        num[slot_1] = -99

        cls()
        print("×——————————————————————————————————×")
        print(f"24 Game:\nSlot | Operation\nNumber:")
        display(num, game_ans)
        print("\n\nOperation")
        print("1    | +")
        print("2    | -")
        print("3    | ×")
        print("4    | ÷")
        print(f"Calculate: [{save1} _ _ = __]")
        op_str = input("Enter Operator slot [1-4 or +-*/]\n> ")
        if op_str == "+":
            op = 0
            ops = op_array[0]
        if op_str == "-":
            op = 1
            ops = op_array[1]
        if op_str == "*":
            ops = op_array[2]
            op = 2
        if op_str == "/":
            op = 3
            ops = op_array[3]
        else:
            if op_str in [1,2,3,4]:
                op = op_array[op_str - 1]

        cls()
        print("×——————————————————————————————————×")
        print("24 Game:\nSlot | Number")
        display(num, game_ans)
        print(f"[Calculate: [{save1} {ops} _ = __]")
        while True:
            try:
                slot2 = int(input("Enter your second slot\n> "))
                if slot2 == -99:
                    print("Invalid Input. That input already taken.")
                else:
                    if checker(slot2, num, False): break
                    else:
                        print("Invalid Input. Please enter a number.")
            except ValueError:
                print("Invalid Input. Please enter a number.")

        slot_2 = checker(slot2, num, True)
        save2 = num[slot_2]
        num[slot_2] = -99

        cls()
        print("×——————————————————————————————————×")
        ans = -99
        op = op + 1
        save1 = int(save1)
        save2 = int(save2)
        if op == 1:
            ans = save1 + save2
        elif op == 2:
            ans = save1 - save2
        elif op == 3:
            ans = save1 * save2
        elif op == 4:
            ans = round(save1 / save2, 2)
        print(f"Calculator: {save1}{ops}{save2}={ans}")
        print("Preparing for the next round..")
        num[slot_1] = ans
        print("×——————————————————————————————————×")
        time.sleep(1)

main()
