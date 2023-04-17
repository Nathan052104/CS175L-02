#Nathan Tunnessen
#CS175L
#PieChart.py



import matplotlib.pyplot as plt

def main():
    try:
        file = open('expenses.txt', 'r')
        replace = []
        costs = []
        slice_labels = []
        for line in file:
            xline = line.rstrip()
            replace.append(xline.split('\t'))
        
        for position in replace:
            slice_labels.append(position[0])
        
    
        for position in replace:
            costs.append(position[1])
        

        for i in range(0, len(costs)):
            try:
                costs[i] = int(costs[i])
            except ValueError:
                print("Invalid input")
        

        file.close()

        try:
            plt.pie(costs, labels=slice_labels)

            plt.title('Monthly Expenses')

            plt.show()
        except:
            print("Invalid inputs to display pie chart")

    except IOError:
        print("Invalid file")
    
    

if __name__ == '__main__':
    main()
