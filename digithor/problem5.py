test_case = int(input())
all_totals = []


for i in range(test_case):

    days = int(input())

    series_val = (days*(days+1))/2
    #print(series_val)
    five_count = days // 5
    #print(five_count)
    sub_val = 5 * (five_count*(five_count+1)/2)
    #print(sub_val)

    total = series_val - sub_val
    all_totals.append(int(total))


for i in range(len(all_totals)):
    print( "Case {0}: {1}".format((i+1), all_totals[i]))

