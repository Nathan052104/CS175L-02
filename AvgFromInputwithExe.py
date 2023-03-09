#Nathan Tunnessen
#CS175L-02
#AverageFromInputwithExe.py

def main():
    try:
        numbers_file = open('numbers.txt', 'r')
        total = 0
        x = 0
        for line in numbers_file:
            number = float(line)
            total = total + number
            x = x + 1
            output_lines(x, number, total)
     

        average = get_average(total, x)
        output_average(average)
           
        numbers_file.close()

    except IOError:
        print("Error: Can't find file")
    except ValueError:
        print("Error: Invalid value")
    

def get_average(total, x):
    average = total/x
    return average

def output_average(average):
    print(f'Average: {average:.2f}')

def output_lines(x, number, total):
    print(f'I read in {x} numbers(s) Current number is: {number:.2f}  \t  Total is: {total:.2f}')
    


if __name__ == '__main__':
    main()


