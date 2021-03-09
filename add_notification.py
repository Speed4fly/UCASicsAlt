record = []
records = []
target = open('result.ics', 'w')
with open('cal.ics', 'r+') as f:
    lines = f.readlines()
    for index in range(len(lines)):
        if lines[index] == 'BEGIN:VEVENT\n':
            record.append(index)
        if lines[index][:7] == 'SUMMARY':
            record.append(lines[index])
        if lines[index] == 'END:VEVENT\n':
            record.append(index)
            records.append(record)
            record = []
    last_class_name = records[0][1]
    last_class_index = 0
    cnt = 1
    for index_lines in range(records[0][0]):
        target.write(lines[index_lines])
    for index in range(len(records)):
        if records[index][1] == last_class_name:
            cnt += 1
        else:
            if cnt < 3:
                duration = 'DURATION:PT' + str(cnt * 50) + 'M\n'
            else:
                duration = 'DURATION:PT' + str(cnt * 50 + 20) + 'M\n'
            for index_lines in range(records[last_class_index][0], records[last_class_index][2]):
                if lines[index_lines][0:8] != 'DURATION':
                    target.write(lines[index_lines])
                else:
                    target.write(duration)
            target.write(
                'BEGIN:VALARM\nTRIGGER:-PT30M\nREPEAT:2\nDURATION:PT15M\nACTION:DISPLAY\nDESCRIPTION:\nEND:VALARM\n')
            target.write('END:VEVENT\n')
            cnt = 1
            last_class_name = records[index][1]
            last_class_index = index
    target.close()
