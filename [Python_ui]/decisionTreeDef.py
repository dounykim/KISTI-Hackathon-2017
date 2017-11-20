
"""
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.externals.six import StringIO  
import pydot
import pydotplus


iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

dot_data = StringIO()
tree.export_graphviz(clf,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     out_file=dot_data,
                     filled=True,
                     rounded=True,
                     special_characters=True)


graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph = pydotplus.graph_from_dot_data(dot_data.getvalue()) 


#graph.write_pdf("iris.pdf") 

graph.write_gif('iris.gif')
"""





# rule 출력
"""
from sklearn import tree
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

clf.predict([[2., 2.]])

clf.predict_proba([[2., 2.]])


from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)


with open("iris.txt", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)

"""










"""
print(__doc__)

# Import the necessary modules and libraries
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

# Create a random dataset
rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))

# Fit regression model
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_1.fit(X, y)
regr_2.fit(X, y)

# Predict
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)

# Plot the results
plt.figure()
plt.scatter(X, y, c="darkorange", label="data")
plt.plot(X_test, y_1, color="cornflowerblue", label="max_depth=2", linewidth=2)
plt.plot(X_test, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()
"""



















"""
import copy
import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


from sklearn.datasets import load_iris
from sklearn.cross_validation import cross_val_score
from sklearn import tree




iris = load_iris()
"""
"""
def decisionTree(속성리스트, 데이터, 목적속성):
    print(len(속성리스트))
    print(len(데이터))
    print(len(목적속성))
"""    


"""
clf = tree.DecisionTreeClassifier(random_state=0)
clf = clf.fit(iris.data, iris.target)

#tree.export_graphviz(clf, out_file='dtRule.txt')
"""


"""
#print(clf.tree_.value[1])

#for each in clf.tree_.value:
#    print(each)
"""

"""
data = []

파일 = open('dtRule.txt', 'r')
for line in 파일:
    data.append(line)
"""


"""
from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Data Analysis User interface')
root.config(width=800, height=600, bg='gray')

# File Menu Frame 생성
mainFrame = ttk.Frame(root, padding=(5, 5))
mainFrame.place(height=596, width=796, x=2, y=2) 


tree = ttk.Treeview(mainFrame)

tree['columns']=('one','two','three','four')
tree.column('one', width=150)
tree.column('two', width=100)
tree.column('three', width=100)
tree.column('four', width=200)

tree.heading('one', text='클래스')
tree.heading('two', text='클래스 비율(%)')
tree.heading('three', text='셈플 수')
tree.heading('four', text='클래스 분포')

 
#tree.insert("" , 0,    text="노드", values=("불순도","데이터 수","클래스별 데이터 수"))


nd0 = tree.insert('', 1, 'Node1', text='노드1')
"""

""" 
id2 = tree.insert("", 1, "dir2", text="Dir 2")
tree.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A","2B"))


##alternatively:
tree.insert("", 3, "dir3", text="Dir 3")
tree.insert("dir3", 3, text=" sub dir 3",values=("3A"," 3B"))
"""
"""
tree.pack()


#root.mainloop()
"""









# 클러스터링
"""
def useKmeans(속성List,종속변수List,독립변수Table,군집수,X축속성명,Y축속성명):
    n_clusters_Num = 군집수
    수치X = copy.deepcopy(독립변수Table)
    변환X = np.array(minMaxTrans(독립변수Table))
    Xindex = 속성List.index(X축속성명)
    Yindex = 속성List.index(Y축속성명)
    plt.figure(figsize=(12, 12))
    y_pred = KMeans(n_clusters=n_clusters_Num).fit_predict(변환X)
    plt.scatter(수치X[:, Xindex], 수치X[:, Yindex], c=y_pred, s=150)
    plt.xlabel(X축속성명)
    plt.ylabel(Y축속성명)
    plt.title(X축속성명 + '과' + Y축속성명 + ' graph')
    saveFile(속성List,종속변수List,수치X,y_pred)
    plt.show()
    
def minMaxTrans(독립변수Table):
    matrixLen = len(독립변수Table)
    rowLen = len(독립변수Table[0])
    for rowNum in range(matrixLen):
            minVal = min(독립변수Table[rowNum])
            maxVal = max(독립변수Table[rowNum])
            for i in range(rowLen):
                독립변수Table[rowNum][i] = (독립변수Table[rowNum][i] - minVal)/(maxVal - minVal)
    return(독립변수Table)

def saveFile(속성List,종속변수List,독립변수Table,추가리스트):
    ofile = open('군집파일.csv', 'w',newline='')
    writer = csv.writer(ofile)
    속성List.append('군집결과')
    writer.writerow(속성List)
    count = 0
    for row in 독립변수Table:
        row = list(row)
        row.append(종속변수List[count])
        row.append(추가리스트[count])
        writer.writerow(row)
        count += 1
    ofile.close()
"""



