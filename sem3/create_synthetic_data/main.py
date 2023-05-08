# create one sample of email
def create_email(this_platform):
    from random import randrange, sample
    random_value = randrange(6, 31)
    if this_platform[:6] == 'china_':
        mail_server = 'qq.com'
    else:
        mail_server = 'gmail.com'
    random_mail = sample('abcdefghijklmnopqrstuvwxyz0123456789', random_value)
    random_mail = ''.join(random_mail)
    random_mail = random_mail + '@' + mail_server
    return random_mail


# create file with unique emails
def create_unique_email(this_platform):
    this_email = create_email(this_platform)
    with open('emails', 'w') as file:
        file.write(this_email)
    in_process = True
    while in_process:
        with open('emails', 'r') as file:
            for line in file:
                if line == this_email:
                    this_email = create_email(this_platform)
                    in_process = True
                    break
                else:
                    in_process = False
    with open('emails', 'a') as file:
        file.write(this_email + '\n')
    return this_email


# create one sample of ip
def create_ip():
    from random import randint
    a = randint(0, 255)
    b = randint(0, 255)
    c = randint(0, 255)
    d = randint(0, 255)
    return str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)


# create file with unique ips
def create_unique_ip():
    this_ip = create_ip()
    with open('ips', 'w') as file:
        file.write(this_ip)
    in_process = True
    while in_process:
        with open('ips', 'r') as file:
            for line in file:
                if line == this_ip:
                    this_ip = create_ip()
                    in_process = True
                    break
                else:
                    in_process = False
    with open('ips', 'a') as file:
        file.write(this_ip + '\n')
    return this_ip


# create one sample of platform
def create_platform():
    from random import randint
    line = randint(0, 49)
    with open('platforms', 'r') as file:
        this_platform = file.readlines()[line]
    return this_platform.replace('\n', '')


# create date with duration of one year
def create_dates(this_winter, this_spring, this_summer, this_autumn, this_rows):
    from math import ceil
    from random import randint
    if this_winter + this_spring + this_summer + this_autumn != 100 or this_winter < 0 or this_spring < 0 or this_summer < 0 or this_autumn < 0:
        print("ошибка в сезонах")
        raise SystemExit
    else:
        year = randint(2000, 2022)
        file = open('dates', 'w')
        file.close()
        if this_winter == 0:
            pass
        else:
            winter_lines = ceil(this_rows * this_winter/100)
            if year % 4 == 0:
                days_in_winter = 91
            else:
                days_in_winter = 90
            while winter_lines % days_in_winter != 0:
                with open('dates', 'a') as file:
                    file.write(f'31-12-{year - 1}\n')
                winter_lines -= 1
            dates_in_one_day = int(winter_lines/days_in_winter)
            for day in range(1, 32):
                with open('dates', 'a') as file:
                    for date in range(dates_in_one_day):
                        file.write(f'{day}-12-{year - 1}\n')
            if days_in_winter == 91:
                end = 30
            else:
                end = 29
            for day in range(1, end):
                with open('dates', 'a') as file:
                    for date in range(dates_in_one_day):
                        file.write(f'{day}-01-{year}\n')
            for day in range(1, 32):
                with open('dates', 'a') as file:
                    for date in range(dates_in_one_day):
                        file.write(f'{day}-02-{year}\n')

        if this_spring == 0:
            pass
        else:
            spring_lines = ceil(this_rows * this_spring/100)
            days_in_spring = 92
            while spring_lines % days_in_spring != 0:
                with open('dates', 'a') as file:
                    file.write(f'1-03-{year}\n')
                spring_lines -= 1
            dates_in_one_day = int(spring_lines/days_in_spring)
            for day in range(1, 32):
                with open('dates', 'a') as file:
                    for date in range(dates_in_one_day):
                        file.write(f'{day}-03-{year}\n')
            for day in range(1, 31):
                with open('dates', 'a') as file:
                    for date in range(dates_in_one_day):
                        file.write(f'{day}-04-{year}\n')
            for day in range(1, 32):
                with open('dates', 'a') as file:
                    for date in range(dates_in_one_day):
                        file.write(f'{day}-05-{year}\n')

        if this_summer == 0:
            pass
        else:
            summer_lines = ceil(this_rows * this_summer/100)
            days_in_summer = 92
            while summer_lines % days_in_summer != 0:
                with open('dates', 'a') as file:
                    file.write(f'1-06-{year}\n')
                summer_lines -= 1
            dates_in_one_day = int(summer_lines / days_in_summer)
            for day in range(1, 31):
                with open('dates', 'a') as file:
                    for date in range(dates_in_one_day):
                        file.write(f'{day}-06-{year}\n')
            for day in range(1, 32):
                with open('dates', 'a') as file:
                    for date in range(dates_in_one_day):
                        file.write(f'{day}-07-{year}\n')
            for day in range(1, 32):
                with open('dates', 'a') as file:
                    for date in range(dates_in_one_day):
                        file.write(f'{day}-08-{year}\n')

        if this_autumn == 0:
            pass
        else:
            autumn_lines = ceil(this_rows * this_autumn/100)
            days_in_autumn = 91
            while autumn_lines % days_in_autumn != 0:
                with open('dates', 'a') as file:
                    file.write(f'1-09-{year}\n')
                autumn_lines -= 1
            dates_in_one_day = int(autumn_lines / days_in_autumn)
            for day in range(1, 31):
                with open('dates', 'a') as file:
                    for date in range(dates_in_one_day):
                        file.write(f'{day}-09-{year}\n')
            for day in range(1, 32):
                with open('dates', 'a') as file:
                    for date in range(dates_in_one_day):
                        file.write(f'{day}-10-{year}\n')
            for day in range(1, 31):
                with open('dates', 'a') as file:
                    for date in range(dates_in_one_day):
                        file.write(f'{day}-11-{year}\n')


# create amount of ads in range 1 to 100
def amount_of_ads():
    from random import randint
    return randint(1, 100)


# calculate time default 30sec to 120sec to 1 ad
def adv_time(this_ads, min_sec=30, max_sec=120):
    from random import randint
    time = this_ads*randint(min_sec, max_sec)/60.0
    duration = str(round(time, 2))
    seconds = '0.'
    checked = False
    for letter in duration:
        if checked:
            seconds += letter
        if letter == '.':
            checked = True
    minutes = str(round(time))
    if seconds != '0':
        seconds = str(round(float(seconds)*60))
    if len(seconds) == 1:
        seconds = ':' + '0' + seconds
    else:
        seconds = ":" + seconds
    return minutes + seconds + ' минут'


# create product depending on season
def create_product(this_winter, this_spring, this_summer, this_autumn, this_rows):
    from math import ceil
    from random import randint

    winter_lines = ceil(this_rows*this_winter/100)
    spring_lines = ceil(this_rows*this_spring/100)
    summer_lines = ceil(this_rows*this_summer/100)
    autumn_lines = ceil(this_rows*this_autumn/100)

    with open('products', 'r') as surf:
        products = surf.readlines()
        with open('prod', 'w') as file:
            for line in range(winter_lines):
                file.write(products[randint(0, 11)])
            for line in range(spring_lines):
                file.write(products[randint(12, 23)])
            for line in range(summer_lines):
                file.write(products[randint(25, 35)])
            for line in range(autumn_lines):
                file.write(products[randint(37, 49)])


if __name__ == '__main__':
    import xlsxwriter

    workbook = xlsxwriter.Workbook('adv.xlsx')
    worksheet = workbook.add_worksheet()

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Write some data headers.
    worksheet.write('A1', 'email', bold)
    worksheet.write('B1', 'ip', bold)
    worksheet.write('C1', 'platform', bold)
    worksheet.write('D1', 'date', bold)
    worksheet.write('E1', 'amount_od_ads', bold)
    worksheet.write('F1', 'duration', bold)
    worksheet.write('G1', 'product', bold)

    # Start from the first cell below the headers.
    row = 1
    col = 0

    # File params
    rows = 50000

    # Season
    winter = 25
    spring = 25
    summer = 25
    autumn = 25

    create_dates(winter, spring, summer, autumn, rows)
    with open('dates', 'r') as file:
        dates = file.readlines()

    create_product(winter, spring, summer, autumn, rows)
    with open('prod', 'r') as file:
        products = file.readlines()

    # Iterate over the data and write it out row by row.
    for i in range(rows):
        platform = create_platform()
        email = create_unique_email(platform)
        ip = create_unique_ip()
        ads = amount_of_ads()
        time = adv_time(ads)
        worksheet.write(row, col, email)
        worksheet.write(row, col + 1, ip)
        worksheet.write(row, col + 2, platform.replace('china_', ''))
        worksheet.write(row, col + 3, dates[i].replace('\n', ''))
        worksheet.write(row, col + 4, ads)
        worksheet.write(row, col + 5, time)
        worksheet.write(row, col + 6, products[i].replace('\n', ''))
        row += 1

    workbook.close()


