def parse_month(month):
    months = {
        'January': '01',
        'February': '02',
        'March': '03',
        'April': '04',
        'May': '05',
        'June': '06',
        'July': '07',
        'August': '08',
        'September': '09',
        'October': '10',
        'November': '11',
        'December': '12'
    }
    return months.get(month)

def parse_date(user_string):
    parts = user_string.split()
    month = parse_month(parts[0])
    day = parts[1].strip(',')
    year = parts[2]
    return f"{month}/{day}/{year}"

if __name__ == '__main__':
    while True:
        user_input = input()
        if user_input == '-1':
            break
        print(parse_date(user_input))
