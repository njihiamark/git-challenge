import sys


def get_perf_pay(readers):
    if readers < 200:
        return 0
    if readers <= 400:
        return readers/4
    return 100 + (readers - 400) * 0.030


if __name__ == "__main__":
    if (len(sys.argv)) < 2:
        print('Please provide the number of readers...')
    else:
        print('Total pay:')
        print(get_perf_pay(int(sys.argv[1])))
