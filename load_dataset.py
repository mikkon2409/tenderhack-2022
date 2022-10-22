import pandas as pd
import json



def func(x):
    try:
        return json.loads(x)
    except:
        if pd.isna(x):
            return []
        else:
            if len(x) == 0:
                return []
            else:
                return json.loads(''.join([x, '"}]']))



contr = pd.read_excel('Контракты_Иркутск.xlsx')
contr['СТЕ'] = contr['СТЕ'].apply(json.loads)

cte = pd.read_excel('СТЕ_Иркутск.xlsx')
cte["ID СТЕ"] = cte["ID СТЕ"].astype(str)
cte['Характеристики'] = cte['Характеристики'].apply(func)