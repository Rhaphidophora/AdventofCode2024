def safe():
    # increasing
    if report[0] < report[1]:
        for i in range(len(report) - 1):
            if report [i] > report[i+1]:
                return False
            if not (1 <= abs(report[i] - report[i+1]) <= 3):
                return False
            

    #decreasing
    if report [0] > report[1]:
        for i in range(len(report) - 1):
            if report [i] < report[i+1]:
                return False
            if not (1 <= abs(report[i] - report[i+1]) <= 3):
                return False
            

    if report[0] == report[1]:
        return False

    return True

data_test = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


safe_reports = 0
reports = data_test.split(sep="\n")
for report in reports:
    report = report.split()
    report = list(map(int, report))
    if safe():
        safe_reports += 1

assert safe_reports == 2


#part 1
with open("2.txt") as file:
    reports = []
    for line in file:
        reports.append(list(map(int, line.split())))
        safe_reports = 0
    for report in reports:
        if safe():
            safe_reports += 1

    print(safe_reports)

#part 2

with open("2.txt") as file:
    reports = []
    for line in file:
        reports.append(list(map(int, line.split())))
        safe_reports = 0
    for report in reports:
        if safe():
            safe_reports += 1
        else:
            report_copy = report.copy()
            for i in range(len(report)):
                report = report_copy.copy()
                del report[i]
                if safe():
                    safe_reports += 1
                    break

    print(safe_reports)
