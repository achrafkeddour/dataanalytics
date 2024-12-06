import pandas as pd1
import matplotlib.pyplot as plt1

# Création des données de ventes
ddates = [
    "2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05", "2023-01-06", "2023-01-07", "2023-01-08", "2023-01-09", "2023-01-10"
]
ssales = [100, 110, 105, 108, 102, 115, 120, 118, 113, 125]

# Création d'un DataFrame pour organiser les données (une trame)
df = pd1.DataFrame({'Date': ddates, 'Sales': ssales})
print(df)


#         Date  Sales
# 0  2023-01-01    100
# 1  2023-01-02    110
# 2  2023-01-03    105
# 3  2023-01-04    108
# 4  2023-01-05    102
# 5  2023-01-06    115
# 6  2023-01-07    120
# 7  2023-01-08    118
# 8  2023-01-09    113
# 9  2023-01-10    125

plt1.figure(figsize=(10, 5))
plt1.plot(df['Date'], df['Sales'])

plt1.show()