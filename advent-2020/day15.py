INPUT = '0,12,6,13,20,1,17'
def enumerate_nums(seed):
    last_seen = {}
    turn = 1
    last = None
    turns_since_last_spoken = None
    was_new = False
    for n in seed:
        yield n
        if n in last_seen:
            turns_since_last_spoken = turn - last_seen[n]
        else:
            turns_since_last_spoken = None
        last_seen[n] = turn
        turn += 1
        last = n
    while True:
        if turns_since_last_spoken is None:
            n = 0
        else:
            n = turns_since_last_spoken
        yield n
        if n in last_seen:
            turns_since_last_spoken = turn - last_seen[n]
        else:
            turns_since_last_spoken = None
        last_seen[n] = turn
        turn += 1
        last = n

def part1(s):
    nums = list(map(int, s.split(',')))
    game = enumerate_nums(nums)
    answer = None
    for _ in range(2020):
        answer = next(game)
    print(f'The answer to part one is {answer}')

def part2(s):
    nums = list(map(int, s.split(',')))
    game = enumerate_nums(nums)
    answer = None
    for _ in range(30000000):
        answer = next(game)
    print(f'The answer to part two is {answer}')


part1(INPUT)
part2(INPUT)