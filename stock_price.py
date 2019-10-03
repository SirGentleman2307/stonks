def open_file(file_name):
    return open(file_name,"r")

def get_data_list(file_name):
    data_file = open_file(file_name)
    data_list = []

    for line_str in data_file:
        data_list.append(line_str.strip().split(','))

    data_file.close()
    return data_list

def get_useful_info(data_list):
    THE_DATE = 0
    ADJ_CLOSE = 5
    VOLUME = 6
    useful_list = []
    LENGTH = len(data_list)
    for i in range(1, LENGTH):
        useful_data = [data_list[i][THE_DATE].split('-'), float(data_list[i][ADJ_CLOSE]), float(data_list[i][VOLUME])]
        useful_list.append(useful_data)
    return useful_list

def get_year_info(data_list):
    year_list = []
    for i in range(len(data_list)):
        THE_DATE = data_list[i][0][0]
        if THE_DATE not in year_list:
            year_list.append(THE_DATE)
    return year_list

def get_monthly_averages(data_list,year_list):
    month_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    over_sum = 0
    under_sum = 0
    ave_list = []
    for year in year_list:
        for month in month_list:
            THE_DATE = year + '-' + month
            x = False
            for item in data_list:
                if item[0][0] == year and item[0][1] == month:
                    ADJ_CLOSE = item[1]
                    VOLUME = item[2]

                    over_sum += ADJ_CLOSE * VOLUME
                    under_sum += VOLUME
                    x = True
            if x:
                the_tuple = THE_DATE, over_sum/under_sum
                ave_list.append(the_tuple)
                over_sum = 0
                under_sum = 0
    return ave_list

def print_info(the_tuple):
    print("{:12}{}".format("Month","Price"))
    for item in the_tuple:
        print("{:10}{:.2f}".format(item[0], item[1]))

def highest_price(data_list):
    max_value = 0
    for item in data_list:
        if item[1] > max_value:
            max_value = item[1]
            MAX_DATE = item[0][0] + '-' + item[0][1] + '-' + item[0][2]

    print("Highest price {:.2f} on day {}".format(max_value, MAX_DATE))


def main():
    try:
        file_name = input("Enter filename: ")
        data_list = get_data_list(file_name)

        good_info_list = get_useful_info(data_list)
        year_list = get_year_info(good_info_list)
        ave_price = get_monthly_averages(good_info_list, year_list)
        print_info(ave_price)
        highest_price(good_info_list)

    except FileNotFoundError:
        print("Filename {} not found!".format(file_name))

# ----- Main program -----#
main()