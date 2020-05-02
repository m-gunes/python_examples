def calc_note(line):
    line = line[:-1]  # remove last character
    arr = line.split(',')  # add list every line
    name, first, second, final = arr  # unpacking a list

    first = int(first)
    second = int(second)
    final = int(final)
    last_note = first * (3 / 10) + second * (3 / 10) + final * (4 / 10)

    if last_note >= 90:
        letter = "AA"
    elif last_note >= 85:
        letter = "BA"
    elif last_note >= 80:
        letter = "BB"
    elif last_note >= 75:
        letter = "CB"
    elif last_note >= 70:
        letter = "CC"
    elif last_note >= 65:
        letter = "DC"
    elif last_note >= 60:
        letter = "DD"
    elif last_note >= 55:
        letter = "FD"
    else:
        letter = "FF"

    if letter == "FD" or letter == "FF":
        failed = name + "-------------> " + letter + "\n"
        obj = {
            'failed': failed,
            'all': name + "-------------> " + letter + "\n"
        }
        return obj
    else:
        succeed = name + "-------------> " + letter + "\n"
        obj = {
            'succeed': succeed,
            'all': name + "-------------> " + letter + "\n"
        }
        return obj


with open('notes.txt', 'r', encoding='utf-8') as file:
    all_list = []
    failed_list = []
    succeed_list = []

    for line in file:
        obj = calc_note(line)

        all_list.append(obj['all'])

        if 'failed' in obj:
            failed_list.append(obj['failed'])
        elif 'succeed' in obj:
            succeed_list.append(obj['succeed'])

    with open('all-result.txt', 'w', encoding='utf-8') as file2:
        for item in all_list:
            file2.write(item)
    with open('failed-result.txt', 'w', encoding='utf-8') as file2:
        for item in failed_list:
            file2.write(item)
    with open('succeed-result.txt', 'w', encoding='utf-8') as file2:
        for item in succeed_list:
            file2.write(item)
