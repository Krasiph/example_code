import random

def choose_from_list(l):
    return l.pop(random.randint(0, len(l) - 1))


def the_numbers(big, little):
    if big < 0 or little < 0:
        raise RuntimeError('no negative numbers allowed')

    if big > 4:
        raise RuntimeError('must pick between 1 and 4 big numbers; received {}'.format(big))

    if big + little != 6:
        raise RuntimeError('can only pick a total of 6 numbers; received {}'.format(big + little))

    numbers = []
    big_ones = [25, 50, 75, 100]
    little_ones = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]

    for i in range(0, big):
        numbers.append(choose_from_list(big_ones))

    for i in range(0, little):
        numbers.append(choose_from_list(little_ones))

    return numbers


def the_target(numbers):
    operations = ['+', '-', '*', '/']

    nums = numbers.copy()
    attempts = 3
    target = None

    while attempts > 0 and target is None:
        num_1 = choose_from_list(nums)
        num_2 = choose_from_list(nums)
        op = random.choice(operations)

        if op == '-' and  num_1 < num_2:
            temp = num_1
            num_1 = num_2
            num_2 = temp

        elif op == '/' and num_1 % num_2 != 0:
            nums.append(num_1)
            nums.append(num_2)
            continue

        potential_target = eval('{0}{1}{2}'.format(num_1, op, num_2))

        # If we've exhausted the list, try again or succeed
        if len(nums) == 0:
            if potential_target < 100 or potential_target > 1000:
                attempts -= 1
                nums = numbers.copy()

            else:
                target = potential_target

        # If we have a viable target, potentially succeed
        elif len(nums) < 4 and potential_target >= 100 and potential_target <= 999:
            temp = [True]

            for i in range(0, len(nums)):
                temp.append(False)

            if random.choice(temp):
                target = potential_target

            else:
                nums.append(potential_target)

        # Add the new number back into the pool of numbers
        else:
            nums.append(potential_target)

    if target is None:
        target = random.randint(100, 999)

    return target
