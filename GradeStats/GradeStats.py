grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grd in grades:
        print grd

def grades_sum(scores):
    total = 0
    for scr in scores:
        total += scr
    return total

def grades_average(grades):
    return grades_sum(grades) / float(len(grades))

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for scr in scores:
        variance += (average - scr) ** 2
    variance = variance / len(scores)
    return variance

def grades_std_deviation(variance):
    return variance ** 0.5

print "Grades average: " + str (grades_average(grades))
print "Grades variance: " + str(grades_variance(grades))
print "Grades std deviation: " + str(grades_std_deviation(grades_variance(grades)))