def open_or_senior(data):
    liste = []
    for i in range(len(data)):
        if data[i][0] >= 55 and data[i][1] > 7:
            liste.append("Senior")
        else:
            liste.append("Open")
    return liste
print(open_or_senior([[18,20] ,[55,15]]))
