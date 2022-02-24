#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance .csv')
df.info()

female_math = df[df['gender']== 'female']['math score'].mean()
male_math = df[df['gender']=='male']['math score'].mean()
female_reading = df[df['gender']=='female']['reading score'].mean()
male_reading = df[df['gender']=='female']['reading score'].mean()

genders = df['gender'].value_counts()
genders.plot(kind = 'pie')
plt.show()
s = pd.Series(data = [female_math, male_math, female_reading, male_reading, female_write, male_write])
index = ['Мат.девочки', 'Мат.мальчики', 'Чт.девочки', 'Чт.мальчики', 'Письмо девочки', 'Письмо мальчики']
s.plot(kind = 'barh')
plt.show()