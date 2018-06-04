import sys


def get_perf_pay(readers):
    return readers * 0.017


if __name__ == "__main__":
    if (len(sys.argv)) < 2:
        print('Please provide the number of readers...')
    else:
        print('Total pay:')
        print(get_perf_pay(int(sys.argv[1])))
