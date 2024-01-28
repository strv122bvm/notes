# 忽略警告提示
import warnings
warnings.filterwarnings('ignore')

#导入处理数据包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#导入数据
#训练数据集
train = pd.read_csv(r'D:\数据分析\python\titanic\train.csv')
#获取数据类型列的描述统计信息
train.describe()
# 查看每一列的数据类型，和数据总数
train.info()
n = train['Survived'].value_counts()
train['Survived'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(n,autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=15))
plt.title('总体生还率')
plt.Text(0.5, 1.0, '总体生还率')
plt.show()

# 不同性别乘客的生还情况
sex_count = train.groupby(by='Sex')['Survived'].value_counts()

# 两张饼图画在同一张图纸上
plt.figure(figsize=(2*5,5))

axes1=plt.subplot(1,2,1)
axes1.pie(sex_count.loc['female'][::-1],autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=10),colors=['#9400D3','#FFB6C1'],startangle=90)
axes1.set_title('女性生还率')

axes2=plt.subplot(1,2,2)
axes2.pie(sex_count.loc['male'],autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=10),colors=['#2E8B57','#AFEEEE'])
axes2.set_title('男性生还率')
plt.Text(0.5, 1.0, '男性生还率')
plt.show()

# 船上年龄范围
age_range = train['Age']
# 各年龄阶段人数
age_num,_ = np.histogram(age_range,range=[0,80],bins=16)

np.array([ 40,  22,  16,  86, 114, 106,  95,  72,  48,  41,  32,  16,  15,
         4,   6,   1], dtype="int64")
# 各年龄阶段生还人数
age_survived = []
for age in range(5,81,5):
    survived_num = train.loc[(age_range>=age-5) & (age_range<=age)]['Survived'].sum()
    age_survived.append(survived_num)

# 绘制条形图
plt.figure(figsize=(12,6))
plt.bar(np.arange(2,78,5)+0.5,age_num,width=5,label='总人数',alpha=0.8)
plt.bar(np.arange(2,78,5)+0.5,age_survived,width=5,label='生还人数')
plt.xticks(range(0,81,5))
plt.yticks(range(0,121,10))
plt.xlabel('年龄',position=(0.95,0),fontsize=15)
plt.ylabel('人数',position=(0,0.95),fontsize=15)
plt.title('各年龄阶段人数和生还人数条形图')
plt.grid(True,linestyle=':',alpha=0.6)
plt.show()

# 不同登入港口乘客的生还情况
embarked_count = train.groupby(by='Embarked')['Survived'].value_counts()
# 三张饼图画在同一张图纸上
plt.figure(figsize=(3*5,5))

axes1=plt.subplot(1,3,1)
axes1.pie(embarked_count.loc['C'][::-1],autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=10),colors=['#9400D3','#FFB6C1'],startangle=45)
axes1.set_title('法国瑟堡市乘客生还率')

axes2=plt.subplot(1,3,2)
axes2.pie(embarked_count.loc['Q'],autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=10),colors=['#4169E1','#AFEEEE'])
axes2.set_title('爱尔兰昆士敦乘客生还率')

axes3=plt.subplot(1,3,3)
axes3.pie(embarked_count.loc['S'],autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=10),colors=['#698B69','#76EE00'])
axes3.set_title('英国南安普顿乘客生还率')
plt.Text(0.5, 1.0, '英国南安普顿乘客生还率')
plt.show()

# 不同登入港口乘客的生还情况
pclass_count = train.groupby(by='Pclass')['Survived'].value_counts()
# 三张饼图画在同一张图纸上
plt.figure(figsize=(3*5,5))

axes1=plt.subplot(1,3,1)
axes1.pie(pclass_count.loc[1][::-1],autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=10),colors=['#9400D3','#FFB6C1'],startangle=45)
axes1.set_title('一等舱乘客生还率')

axes2=plt.subplot(1,3,2)
axes2.pie(pclass_count.loc[2],autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=10),colors=['#4169E1','#AFEEEE'])
axes2.set_title('二等舱乘客生还率')

axes3=plt.subplot(1,3,3)
axes3.pie(pclass_count.loc[3],autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1],textprops=dict(size=10),colors=['#698B69','#76EE00'])
axes3.set_title('三等舱乘客生还率')
plt.Text(0.5, 1.0, '三等舱乘客生还率')
plt.show()

# 不同登入港口乘客的船舱分布情况情况
embarked_pclass = train.groupby(by='Embarked')['Pclass'].value_counts()
# 三张饼图画在同一张图纸上
plt.figure(figsize=(3*5,5))

axes1=plt.subplot(1,3,1)
axes1.pie(embarked_pclass.loc['C'],autopct='%.2f%%',labels=['一等舱','三等舱','二等舱'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1,0.1],textprops=dict(size=10),colors=['#9400D3','#FFB6C1','#FF6347'])
axes1.set_title('法国瑟堡市乘客生还率')

axes2=plt.subplot(1,3,2)
axes2.pie(embarked_pclass.loc['Q'],autopct='%.2f%%',labels=['三等舱','二等舱','一等舱'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1,0.1],textprops=dict(size=10),colors=['#4169E1','#AFEEEE','#66CDAA'],startangle=10)
axes2.set_title('爱尔兰昆士敦乘客生还率')

axes3=plt.subplot(1,3,3)
axes3.pie(embarked_pclass.loc['S'],autopct='%.2f%%',labels=['三等舱','二等舱','一等舱'],pctdistance=0.4,labeldistance=0.6,
       shadow=True,explode=[0,0.1,0.1],textprops=dict(size=10),colors=['#698B69','#76EE00','#76EEC6'],startangle=180)
axes3.set_title('英国南安普顿乘客生还率')
plt.Text(0.5, 1.0, '英国南安普顿乘客生还率')
plt.show()
