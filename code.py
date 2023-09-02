from posixpath import split
import pandas as p
import seaborn as sns
fr = p.read_csv("titanic_train (1).csv")
fr.drop(['Ticket','Name','Fare','PassengerId','Parch'],axis = 1)
fr['Age'].median()



def funcname(cols):
  Age = cols[0]
  Pclass = cols[1]
  if p.isnull(Age):
    if Pclass ==1:
      return 37
    elif Pclass ==2:
      return 29
    else:
      return 20
  else:
      return Age

fr['Age'] = fr[['Age','Pclass']].apply(funcname,axis = 1)
fr.drop(['Embarked','Cabin','Fare','Ticket','Name','PassengerId'],axis =1,inplace= True)
gender = p.get_dummies(fr['Sex'],drop_first = True)
fr = p.concat([fr,gender],axis = 1)
fr.drop('Sex',axis = 1,inplace = True)
print(fr.head())
x = fr.drop('Survived',axis = True)
y=fr['Survived']
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size = 0.2)
xtest
"enter kevbot"
