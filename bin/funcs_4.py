# with default values
def add(a, b=10):
    return a + b


r = add(10)
print('r = ', r)


def get_ips(file_path, mode='r'):
        f = open(file_path, mode)
        if file_path.endswith('.csv'):
            ips = [line.split(',')[0] for line in f if line[:3].isdigit()]
            return ips
        else:
            ips = [line.split()[0] for line in f if line[:3].isdigit()]
            return ips


r = get_ips('log_report.txt')
print('r = ', r)