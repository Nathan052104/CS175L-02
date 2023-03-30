def main():
    books = book_list()
    print(f'Read {len(books)} books')
    menu(books)    

def book_list():
    books=[]
    infile = open('bestsellers.txt', 'r')
    bestsellers = infile.readlines()
    infile.close()
    for index in range(len(bestsellers)):
        bestsellers[index] = bestsellers[index].rstrip('\n')
        cols = bestsellers[index].split('\t')
        books.append(cols)
    return books
    
def menu(books):
    print('1: Look up year range')
    print('2: Look up month/year')
    print('3: Search for author')
    print('4: Search for title')
    print('Q: Quit')
    user = input('What would you like to do? ').lower()
    if user == '1':
        year_range(books)
        menu(books)
    elif user == '2':
        month_year(books)
        menu(books)
    elif user == '3':
        search_author(books)
        menu(books)
    elif user == '4':
        search_title(books)
        menu(books)
    elif user == 'q':
        print('Done')
        exit()
    elif user != '1' or '2' or '3' or '4' or 'q':
        print("I don't understand this command")
        menu(books)

def year_range(books):
    startYear = int(input('Enter start year: '))
    endYear = int(input('Enter end year: '))
    
    for b in books:
        date= b[3].split('/')
        year = int(date[2])
        title = b[0]
        author = b[1]
        publisher = b[2]
        genre = b[4]
        final_date = b[3]
        if year >= startYear and year <= endYear:
            print(f'{title} by: {author} (pub date: {final_date})')
    menu(books)
    
def month_year(books):
    month_input = int(input('Enter month (1-12): '))
    year_input = int(input('Enter year: '))
    for b in books:
        date = b[3].split('/')
        year = int(date[2])
        month = int(date[0])
        title = b[0]
        author = b[1]
        publisher = b[2]
        genre = b[4]
        final_date = b[3]
        if month_input == month and year_input == year:
            print(f'{title} by: {author} (pub date: {final_date})')
    menu(books)

def search_author(books):
    author_input = str(input('Enter search string: ')).lower()
    for b in books:
        title = b[0]
        author = b[1].lower()
        author_final = b[1]
        publisher = b[2]
        genre = b[4]
        final_date = b[3]
        if author.__contains__(author_input):
           print(f'{title} by: {author_final} (pub date: {final_date})')
    menu(books)

def search_title(books):
    search = str(input('Enter search string: ')).lower()
    bestsellers_file = open('bestsellers.txt', 'r')
    for b in books:
        title = b[0].lower()
        title_final = b[0]
        author = b[1]
        publisher = b[2]
        genre = b[4]
        final_date = b[3]
        if title.__contains__(search):
           print(f'{title_final} by: {author} (pub date: {final_date})')
    menu(books)

if __name__ == '__main__':
    main()
