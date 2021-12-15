import pandas as pd
def counter(df, num, lst): # filepass - шлях до файлу, num - кількість, якої хочеш досягнути, lst - список завдань
    with open (df) as file:
        counter = 0
        while counter <= num:
            inp = input("On which goal you upgraded:")
            for i in lst: #list of goals
                if lst[i] == inp:
                    counter+= 1
            for i in file:
                if counter < num:
                    df[i]['Failue'] = "*"
                    #додаємо '*' до Failue
                elif counter == num:
                    df[i]['Success'] = "*"
                    #додаємо '*' до Success