# Day 7 - Data Preprocessing, NumPy & Pandas

## Topics Covered

What is a Dataset, Introduction to NumPy, Creating Arrays, Array Operations, Introduction to Pandas, Series & DataFrames, Loading CSV Files, Handling Missing Values, Data Cleaning, Feature Selection, and Train-Test Split.

Day 7 ka main goal hai students ko Data Science ka practical base dena. Machine Learning model direct raw data par achha perform nahi karta. Pehle data ko read, understand, clean, transform, and split karna padta hai. Isi process ko data preprocessing bolte hain. Aaj hum NumPy aur Pandas ka use karke data handle karna seekhenge.

Teacher speaking flow: "Kal humne Data Science aur ML ka big picture samjha. Aaj hum practical side start karenge. Model training se pehle data ko prepare karna padta hai. Agar data messy hai, missing values hain, wrong format hai, ya unnecessary columns hain, to model confuse ho sakta hai. Isliye Data Preprocessing ML project ka foundation hai."

---

# 1. What is a Dataset?

Dataset organized data ka collection hota hai. Usually dataset rows and columns me hota hai. Row ek record hota hai, aur column ek feature hota hai. Example: student dataset me ek row ek student ko represent karegi. Columns ho sakte hain `name`, `gender`, `math_score`, `english_score`, `study_hours`, `attendance`, aur `result`.

Machine Learning me dataset bahut important hai because model data se hi learn karta hai. Agar dataset accurate, clean, and relevant hai, to model better learn karega. Agar dataset incomplete, duplicate, ya wrong values se filled hai, to model ki performance poor ho sakti hai.

Kaggle real-world datasets ke liye popular platform hai. Students Kaggle se CSV datasets download karke practice kar sakte hain. Beginner ke liye Titanic, Student Performance, Mall Customer Segmentation, and House Prices datasets useful hain.

## Practical Dataset

Class practice ke liye local file `data/student_scores.csv` use karenge. Ye small sample dataset hai jisme student marks, study hours, attendance, and result columns hain. Real-world practice ke liye Kaggle ka Students Performance dataset use kar sakte hain: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

---

# 2. Introduction to NumPy

NumPy Python library hai jo numerical data ke saath fast calculations karne ke liye use hoti hai. Python lists useful hoti hain, but large numerical data par NumPy arrays faster and more powerful hote hain. Data Science me marks, prices, temperatures, image pixels, and model inputs often numbers ke form me hote hain. NumPy in numbers ko efficiently process karta hai.

NumPy ka main object array hota hai. Array list jaisa dikhta hai, but mathematical operations ke liye optimized hota hai. Agar hume marks ka average, maximum, minimum, ya multiplication calculate karna hai, NumPy ka use simple and fast hota hai.

## Practice Code 1 - NumPy Array Basics

```python
import numpy as np

marks = np.array([78, 92, 45, 88, 35])

print(marks)
print(type(marks))
```

## Output

```text
[78 92 45 88 35]
<class 'numpy.ndarray'>
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `import numpy as np` | Ye line NumPy library ko import karti hai. `as np` alias hai, matlab hum NumPy ko short name `np` se use kar sakte hain. Data Science me ye standard convention hai. |
| 3 | `marks = np.array([78, 92, 45, 88, 35])` | `np.array()` Python list ko NumPy array me convert karta hai. Ye marks numerical values hain, jinke upar mathematical operations easily perform kiye ja sakte hain. |
| 5 | `print(marks)` | Ye complete NumPy array print karta hai. Output list jaisa lagta hai, but internally ye NumPy array hai. |
| 6 | `print(type(marks))` | `type()` variable ka data type batata hai. Output `numpy.ndarray` aata hai, jiska matlab ye NumPy array hai. |

---

# 3. Creating Arrays

NumPy arrays multiple ways se create hote hain. Hum direct list se array bana sakte hain, zero values ka array bana sakte hain, one values ka array bana sakte hain, ya range-based array bana sakte hain. Arrays tab useful hote hain jab hume numerical data ko structured way me store karna ho.

Real example: Student marks, monthly sales, daily temperature, and product prices arrays ke form me store ho sakte hain.

## Practice Code 2 - Different Arrays

```python
import numpy as np

scores = np.array([60, 70, 80])
zeros = np.zeros(3)
numbers = np.arange(1, 6)

print(scores)
print(zeros)
print(numbers)
```

## Output

```text
[60 70 80]
[0. 0. 0.]
[1 2 3 4 5]
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `import numpy as np` | NumPy import kiya gaya hai taaki hum array functions use kar sakein. |
| 3 | `scores = np.array([60, 70, 80])` | Ye normal list se NumPy array create karta hai. |
| 4 | `zeros = np.zeros(3)` | Ye 3 zero values ka array banata hai. Machine Learning me kabhi-kabhi placeholder arrays banane ke liye useful hota hai. |
| 5 | `numbers = np.arange(1, 6)` | `np.arange(1, 6)` 1 se 5 tak numbers create karta hai. Last value 6 include nahi hoti. |
| 7-9 | `print(...)` | Ye arrays output me display hote hain. |

---

# 4. Array Operations

Array operations ka matlab hai arrays par mathematical operations perform karna. NumPy arrays par addition, multiplication, mean, max, min, and comparison operations easily hote hain. Ye Data Science me useful hai because hume large numeric data ka summary calculate karna hota hai.

## Practice Code 3 - Marks Summary

```python
import numpy as np

marks = np.array([78, 92, 45, 88, 35])

print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("After Bonus:", marks + 5)
```

## Output

```text
Average: 67.6
Highest: 92
Lowest: 35
After Bonus: [83 97 50 93 40]
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `import numpy as np` | NumPy import hota hai. |
| 3 | `marks = np.array([78, 92, 45, 88, 35])` | Marks ka NumPy array create hota hai. |
| 5 | `print("Average:", np.mean(marks))` | `np.mean()` marks ka average calculate karta hai. |
| 6 | `print("Highest:", np.max(marks))` | `np.max()` highest marks find karta hai. |
| 7 | `print("Lowest:", np.min(marks))` | `np.min()` lowest marks find karta hai. |
| 8 | `print("After Bonus:", marks + 5)` | NumPy array me `+ 5` karne se har element me 5 add hota hai. Ye vectorized operation hai. |

---

# 5. Introduction to Pandas

Pandas Python library hai jo tabular data handle karne ke liye use hoti hai. CSV files, Excel files, SQL data, and structured datasets ko read and analyze karne ke liye Pandas bahut important hai. Data Science me Pandas daily use hoti hai.

Pandas me two important structures hote hain: Series and DataFrame. Series single column jaisa hota hai. DataFrame table jaisa hota hai jisme rows and columns hote hain.

## Practice Code 4 - Create DataFrame

```python
import pandas as pd

data = {
    "name": ["Aman", "Neha", "Rahul"],
    "marks": [78, 92, 45],
    "result": ["Pass", "Pass", "Pass"]
}

df = pd.DataFrame(data)

print(df)
```

## Output

```text
    name  marks result
0   Aman     78   Pass
1   Neha     92   Pass
2  Rahul     45   Pass
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `import pandas as pd` | Pandas library import hoti hai. `pd` alias standard short name hai. |
| 3-7 | `data = {...}` | Dictionary create hoti hai jisme keys column names hain aur values column data lists hain. |
| 9 | `df = pd.DataFrame(data)` | Dictionary ko Pandas DataFrame me convert kiya gaya hai. DataFrame table jaisa structure hota hai. |
| 11 | `print(df)` | Complete DataFrame output me print hota hai. |

---

# 6. Series & DataFrames

Series Pandas ka one-dimensional data structure hai. Ye ek column jaisa hota hai. DataFrame two-dimensional table hota hai. DataFrame me multiple Series columns hote hain.

Example: `marks` ek Series ho sakti hai. Student table jisme name, marks, result columns hain, wo DataFrame hota hai.

## Practice Code 5 - Series and DataFrame

```python
import pandas as pd

marks_series = pd.Series([78, 92, 45])

student_df = pd.DataFrame({
    "name": ["Aman", "Neha", "Rahul"],
    "marks": marks_series
})

print(marks_series)
print(student_df)
```

## Output

```text
0    78
1    92
2    45
dtype: int64
    name  marks
0   Aman     78
1   Neha     92
2  Rahul     45
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `import pandas as pd` | Pandas import kiya gaya hai. |
| 3 | `marks_series = pd.Series([78, 92, 45])` | List ko Pandas Series me convert kiya gaya hai. Series ek single column jaisa hota hai. |
| 5-8 | `student_df = pd.DataFrame({...})` | Dictionary se DataFrame create hota hai. `name` column list se ban raha hai aur `marks` column Series se ban raha hai. |
| 10 | `print(marks_series)` | Series output me index ke saath print hoti hai. |
| 11 | `print(student_df)` | DataFrame table format me print hota hai. |

---

# 7. Loading CSV Files

CSV file comma-separated values file hoti hai. Real datasets mostly CSV format me milte hain. Pandas ka `read_csv()` function CSV file ko DataFrame me load karta hai. Kaggle datasets usually CSV form me download hote hain.

## Practice Code 6 - Load Student CSV

```python
import pandas as pd

df = pd.read_csv("data/student_scores.csv")

print(df.head())
print(df.shape)
```

## Output

```text
   student_id    name  gender  math_score  english_score  science_score  study_hours  attendance result
0           1    Aman    Male          78           82.0             80            4          88   Pass
1           2    Neha  Female          92           89.0             94            6          95   Pass
2           3   Rahul    Male          45           50.0             48            2          62   Pass
3           4  Ayesha  Female          88            NaN             90            5          91   Pass
4           5   Karan    Male          35           40.0             38            1          55   Fail
(6, 9)
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `import pandas as pd` | Pandas import hoti hai. |
| 3 | `df = pd.read_csv("data/student_scores.csv")` | CSV file read hoti hai aur DataFrame `df` me store hoti hai. Path file location batata hai. |
| 5 | `print(df.head())` | `head()` DataFrame ki first 5 rows show karta hai. Data check karne ka ye common first step hai. |
| 6 | `print(df.shape)` | `shape` rows and columns count batata hai. `(6, 9)` ka matlab 6 rows and 9 columns. |

---

# 8. Handling Missing Values

Missing values ka matlab dataset me kuch cells empty hain. Pandas missing value ko often `NaN` show karta hai. Machine Learning models usually missing values directly handle nahi karte. Isliye missing values ko identify and fix karna important preprocessing step hai.

Missing values handle karne ke common ways hain: missing rows remove karna, missing values mean/median/mode se fill karna, ya domain knowledge se correct value fill karna.

## Practice Code 7 - Fill Missing Marks

```python
import pandas as pd

df = pd.read_csv("data/student_scores.csv")

print(df.isnull().sum())

mean_english = df["english_score"].mean()
df["english_score"] = df["english_score"].fillna(mean_english)

print(df.isnull().sum())
```

## Output

```text
student_id       0
name             0
gender           0
math_score       0
english_score    1
science_score    0
study_hours      0
attendance       0
result           0
dtype: int64
student_id       0
name             0
gender           0
math_score       0
english_score    0
science_score    0
study_hours      0
attendance       0
result           0
dtype: int64
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `import pandas as pd` | Pandas import kiya gaya hai. |
| 3 | `df = pd.read_csv("data/student_scores.csv")` | Dataset load hota hai. |
| 5 | `print(df.isnull().sum())` | `isnull()` missing values check karta hai. `sum()` har column me missing values count karta hai. |
| 7 | `mean_english = df["english_score"].mean()` | English score column ka average calculate hota hai. |
| 8 | `df["english_score"] = df["english_score"].fillna(mean_english)` | Missing English score ko average value se fill kiya gaya hai. |
| 10 | `print(df.isnull().sum())` | Cleaning ke baad missing values dobara check hoti hain. |

---

# 9. Data Cleaning

Data cleaning ka matlab dataset ko correct and usable banana. Isme missing values handle karna, duplicate rows remove karna, wrong data types fix karna, unnecessary spaces remove karna, and new useful columns create karna include hota hai.

Real ML project me data cleaning bahut important hota hai. Data Scientists ka kaafi time data cleaning me jata hai because model ki quality data quality par depend karti hai.

## Practice Code 8 - Clean Data and Add Total

```python
import pandas as pd

df = pd.read_csv("data/student_scores.csv")

df["english_score"] = df["english_score"].fillna(df["english_score"].mean())
df["total_score"] = df["math_score"] + df["english_score"] + df["science_score"]
df["percentage"] = (df["total_score"] / 300) * 100

print(df[["name", "total_score", "percentage"]])
```

## Output

```text
     name  total_score  percentage
0    Aman        240.0   80.000000
1    Neha        275.0   91.666667
2   Rahul        143.0   47.666667
3  Ayesha        244.6   81.533333
4   Karan        113.0   37.666667
5   Priya        223.0   74.333333
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `import pandas as pd` | Pandas import hoti hai. |
| 3 | `df = pd.read_csv("data/student_scores.csv")` | CSV dataset DataFrame me load hota hai. |
| 5 | `df["english_score"] = df["english_score"].fillna(df["english_score"].mean())` | English score ke missing value ko column mean se fill kiya gaya hai. |
| 6 | `df["total_score"] = ...` | Math, English, and Science scores add karke new column `total_score` create hota hai. |
| 7 | `df["percentage"] = (df["total_score"] / 300) * 100` | Total score ko percentage me convert kiya gaya hai. |
| 9 | `print(df[["name", "total_score", "percentage"]])` | Sirf selected columns output me print kiye gaye hain. |

---

# 10. Feature Selection

Feature selection ka matlab important input columns choose karna. Machine Learning model ko har column dena zaroori nahi hota. Kuch columns useful hote hain, kuch irrelevant. Example: student result predict karne ke liye `math_score`, `english_score`, `science_score`, `study_hours`, and `attendance` useful features ho sakte hain. `name` model ke liye useful feature nahi hai because name se performance predict nahi karna chahiye.

Target wo column hota hai jisko model predict karega. Example: `result` target column ho sakta hai.

## Practice Code 9 - Select Features and Target

```python
import pandas as pd

df = pd.read_csv("data/student_scores.csv")
df["english_score"] = df["english_score"].fillna(df["english_score"].mean())

features = df[["math_score", "english_score", "science_score", "study_hours", "attendance"]]
target = df["result"]

print(features.head())
print(target.head())
```

## Output

```text
   math_score  english_score  science_score  study_hours  attendance
0          78           82.0             80            4          88
1          92           89.0             94            6          95
2          45           50.0             48            2          62
3          88           66.6             90            5          91
4          35           40.0             38            1          55
0    Pass
1    Pass
2    Pass
3    Pass
4    Fail
Name: result, dtype: object
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `import pandas as pd` | Pandas import hoti hai. |
| 3 | `df = pd.read_csv("data/student_scores.csv")` | Dataset load hota hai. |
| 4 | `df["english_score"] = df["english_score"].fillna(df["english_score"].mean())` | Missing English score fill hota hai taaki features clean rahen. |
| 6 | `features = df[[...]]` | Multiple input columns select kiye gaye hain. Double square brackets DataFrame columns select karne ke liye use hote hain. |
| 7 | `target = df["result"]` | Target column select hota hai. Ye wahi value hai jo ML model predict karega. |
| 9 | `print(features.head())` | Features ki first rows print hoti hain. |
| 10 | `print(target.head())` | Target values ki first rows print hoti hain. |

---

# 11. Train-Test Split

Train-test split Machine Learning ka important step hai. Hum complete data ko two parts me divide karte hain: training data and testing data. Model training data se learn karta hai. Testing data se hum check karte hain ki model new/unseen data par kaisa perform karta hai.

Common split 80 percent training and 20 percent testing hota hai. Agar model ko wahi data test me de diya jisse usne learn kiya hai, to actual performance ka sahi idea nahi milega. Isliye test data separate rakhna zaroori hai.

## Practice Code 10 - Train-Test Split

```python
import pandas as pd

df = pd.read_csv("data/student_scores.csv")
df["english_score"] = df["english_score"].fillna(df["english_score"].mean())

features = df[["math_score", "english_score", "science_score", "study_hours", "attendance"]]
target = df["result"]

train_data = df.sample(frac=0.8, random_state=42)
test_data = df.drop(train_data.index)

X_train = train_data[["math_score", "english_score", "science_score", "study_hours", "attendance"]]
y_train = train_data["result"]

X_test = test_data[["math_score", "english_score", "science_score", "study_hours", "attendance"]]
y_test = test_data["result"]

print("Training rows:", X_train.shape[0])
print("Testing rows:", X_test.shape[0])
```

## Output

```text
Training rows: 5
Testing rows: 1
```

## Detailed Code Explanation

| Line | Code | Explanation |
|---|---|---|
| 1 | `import pandas as pd` | Pandas dataset loading and processing ke liye import hoti hai. |
| 3 | `df = pd.read_csv("data/student_scores.csv")` | CSV dataset load hota hai. |
| 4 | `df["english_score"] = df["english_score"].fillna(df["english_score"].mean())` | Missing value fill hoti hai. Model ko clean data dena important hai. |
| 6 | `features = df[[...]]` | Input columns select kiye gaye hain. In columns se model learn karega. |
| 7 | `target = df["result"]` | Output column select hota hai. Ye value model predict karega. |
| 9 | `train_data = df.sample(frac=0.8, random_state=42)` | `sample()` DataFrame se random rows select karta hai. `frac=0.8` ka matlab 80 percent rows training ke liye choose karna. `random_state=42` same split repeat karne me help karta hai. |
| 10 | `test_data = df.drop(train_data.index)` | Training rows ke index ko original DataFrame se drop karke remaining rows testing data ban jaati hain. |
| 12 | `X_train = train_data[[...]]` | Training data ke input feature columns select hote hain. |
| 13 | `y_train = train_data["result"]` | Training data ka target column select hota hai. |
| 15 | `X_test = test_data[[...]]` | Testing data ke input feature columns select hote hain. |
| 16 | `y_test = test_data["result"]` | Testing data ka target column select hota hai. |
| 18 | `print("Training rows:", X_train.shape[0])` | Training data me kitni rows hain, ye print hota hai. |
| 19 | `print("Testing rows:", X_test.shape[0])` | Testing data me kitni rows hain, ye print hota hai. |

Day 7 ka final takeaway ye hai: ML model banane se pehle data ko understand, clean, select, and split karna bahut important hai. NumPy numerical calculations ke liye useful hai, Pandas table data handle karne ke liye powerful hai, aur train-test split model evaluation ke liye necessary hai.
