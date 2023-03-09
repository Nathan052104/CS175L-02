#Nathan Tunnessen
#CS175L-02
#AverageFromInput.py

def main():
   
    numbers_file = open('numbers.txt', 'r')
  
    total = 0
    x = 0
    
    for line in numbers_file:
        
        number = float(line)
        total = total + number
        x = x + 1
       
        print(f'I read in {x} numbers(s) Current number is: {number:.2f}    Total is: {total:.2f}')

    
    average = total/x
    print(f'Average: {average:.2f}')


   
    numbers_file.close()


if __name__ == '__main__':
    main()
