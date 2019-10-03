def open_file(file_name):
    """Input: filename
    Output: file contents."""
    return open(file_name,"r")

def get_data_list(file_name):
    """Input: filename
    Output: List containing all lines in file."""
    data_file = open_file(file_name)                    # function: open file and save data
    data_list = []
    for line_str in data_file:                          # iterate through data and add every word/number to list
        data_list.append(line_str.strip().split(','))   # seperated by ","
    data_file.close()
    return data_list

def get_useful_info(data_list):
    """Input: list contaning all data
    Output: list containg only necessary data."""
    THE_DATE = 0
    ADJ_CLOSE = 5
    VOLUME = 6
    useful_list = []
    LENGTH = len(data_list)
    for i in range(1, LENGTH):                  # iterate through list and add desired data to new list (skips header)
        useful_data = [data_list[i][THE_DATE].split('-'), float(data_list[i][ADJ_CLOSE]), float(data_list[i][VOLUME])]
        useful_list.append(useful_data)
    return useful_list

def get_year_info(data_list):
    """Input: List containing only necessary data
    Output: list containing all years from input list."""
    year_list = []
    for item in data_list:              # iterate through list
        THE_YEAR = item[0][0]           # year in current item
        if THE_YEAR not in year_list:   # add all unique years to new list
            year_list.append(THE_YEAR)
    return year_list

def get_monthly_averages(data_list,year_list):
    """Input: list containing only necessary data, list of unique years
    Output: List containing tuples of average price for each month in each different year."""
    month_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    over_sum = 0
    under_sum = 0
    ave_list = []
    for year in year_list:                                      # iterate through each unique year
        for month in month_list:                                # iterate through each month
            THE_DATE = year + '-' + month                       # create the date for tuple
            check_month_data = False                            # test to see if month has data 
            for item in data_list:                              # iterate through each item in list
                if item[0][0] == year and item[0][1] == month:  # check if the item year and month match
                                                                # current iteration of year and month
                    ADJ_CLOSE = item[1]
                    VOLUME = item[2]

                    over_sum += ADJ_CLOSE * VOLUME              # calculate sum above division line
                    under_sum += VOLUME                         # calculate sum under division line
                    check_month_data = True                     # month has data, test becomes True

            if check_month_data:                                # if month has data
                the_tuple = THE_DATE, over_sum/under_sum        # add date and calculated sum to tuple
                ave_list.append(the_tuple)                      # add tuple to list
                over_sum = 0                                    # reset calculated results
                under_sum = 0
    return ave_list

def print_info(the_tuple):
    """Input: list containing tuples
    Output: print info in a table."""
    print("{:12}{}".format("Month","Price"))
    for item in the_tuple:                              # iterate through list and print date and average price
        print("{:10}{:.2f}".format(item[0], item[1]))

def highest_price(data_list):
    """Input: list containing only necessary data
    Output: finds the highest price and prints it."""
    max_value = 0
    for item in data_list:                                                  # iterate through list
        if item[1] > max_value:                                             # compare largest value to current item in iteration
            max_value = item[1]                                             # save the largest value if found
            MAX_DATE = item[0][0] + '-' + item[0][1] + '-' + item[0][2]     # save the date for said value
    print("Highest price {:.2f} on day {}".format(max_value, MAX_DATE))


def main():
    """Main program function"""
    try:
        file_name = input("Enter filename: ")
        data_list = get_data_list(file_name)                        # function: get data from file
        good_info_list = get_useful_info(data_list)                 # function: isolate necessary data in list
        year_list = get_year_info(good_info_list)                   # function: save all unique years in list
        ave_price = get_monthly_averages(good_info_list, year_list) # function: calculate average price and save date
        print_info(ave_price)                                       # function: prints out average prices
        highest_price(good_info_list)                               # function: finds the highest price and prints it

    except FileNotFoundError:
        print("Filename {} not found!".format(file_name))

# ----- Main program -----#
main()                      # function: all function calls in one function 