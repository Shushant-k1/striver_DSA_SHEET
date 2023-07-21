def maximumMeetings(start, end):
    z = []
    for i, j in zip(start, end):
        z.append([i, j])

    z.sort(key=lambda x: x[1])
    count = 1
    prev = z[0][1]

    for i in range(1, len(z)):
        if prev <= z[i][0]:
            count += 1
            prev = z[i][1]

    return count
