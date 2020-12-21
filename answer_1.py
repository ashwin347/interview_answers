def server_cost(d1, m1, y1, d2, m2, y2):
    if d1==d2 and m1==m2 and y1==y2:
        return 20
    else:
        if m1==m2 and y1==y2:
            if d2<d1:
                return 'deleted date should not be before created date'
            days=d2-d1
            value =30*days
            return value
        elif y1==y2:
            if m2<m1:
                return 'deleted date should not be before created date'
            months=m2-m1
            value=months*1000
            return value
        else:
            return 20000

if __name__ == '__main__':
    d1M1Y1 = input().split()
    d1 = int(d1M1Y1[0])
    m1 = int(d1M1Y1[1])
    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()
    d2 = int(d2M2Y2[0])
    m2 = int(d2M2Y2[1])
    y2 = int(d2M2Y2[2])

    result = server_cost(d1, m1, y1, d2, m2, y2)
    print(str(result) + '\n')
