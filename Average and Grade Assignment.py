#Nathan Tunnessen
#CS 175L
#Average Grade Assignment

def calc_average(score1,score2,score3,score4,score5):
    score_total=score1+score2+score3+score4+score5
    average=score_total/5
    return average

def determine_grade(scores):
    if scores<=100 and scores>=90:
        letter_grade='A'
    elif scores<90 and scores>=80:
        letter_grade='B'
    elif scores<80 and scores>=70:
        letter_grade='C'
    elif scores<70 and scores>=60:
        letter_grade='D'
    elif scores<60:
        letter_grade='F'
    return letter_grade

def repeat(keep_going):
    while keep_going==True:
        keep_going=input('Enter \'yes\' if you would like to do another calculation: ')
        if keep_going=='yes':
            keep_going==True
            main()
        else:
            keep_going==False

def main():
    keep_going=True
    score1=float(input('Enter score 1: '))
    score2=float(input('Enter score 2: '))
    score3=float(input('Enter score 3: '))
    score4=float(input('Enter score 4: '))
    score5=float(input('Enter score 5: '))
    print(f'\n{"Score":>12}',f'{"Numeric Grade":>18}',f'{"Letter Grade":>18}')
    scores=score1
    print(f'{"Score 1:":>14} {scores:>8}',f'{determine_grade(scores):>18}')
    scores=score2
    print(f'{"Score 2:":>14} {scores:>8}',f'{determine_grade(scores):>18}')
    scores=score3
    print(f'{"Score 3:":>14} {scores:>8}',f'{determine_grade(scores):>18}')
    scores=score4
    print(f'{"Score 4:":>14} {scores:>8}',f'{determine_grade(scores):>18}')
    scores=score5
    print(f'{"Score 5:":>14} {scores:>8}',f'{determine_grade(scores):>18}')
    scores=calc_average(score1,score2,score3,score4,score5)
    print('Average score:',f'{calc_average(score1,score2,score3,score4,score5):>8}',
          f'{determine_grade(scores):>18}')
    repeat(keep_going)
    
main()
