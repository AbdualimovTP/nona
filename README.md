<div align="center">
  <img src="https://i.ibb.co/520wGTn/nona.png"><br>
</div>

-----------------

# nona: Python gap filling toolkit

## What is it?

**nona** a simple toolkit for filling gaps in a dataset.  Filling in the gap using artificial intelligence methods. 

We go through all the columns. We find a column with gaps and split the dataset into a train, this is the part in which we know all the values ​​​​and the test, where there is no missing value in the column and predict using any machine learning method that supports a simple implementation of fit and predict.

## Main Features

Here are just a few of the things that **nona** does well:

- Easy and fast filling of missing values. 
- Using Machine Learning Methods
- Support for machine learning methods with the base implementation of fit and predict
- High Prediction Accuracy of Missing Values

## Where to get it

The source code is currently hosted on GitHub at:
[GitHub - AbdualimovTP/nona: library for filling in missing values ​​using artificial intelligence methods](https://github.com/AbdualimovTP/nona)
Binary installers for the latest released version are available at the [Python
Package Index (PyPI)](https://pypi.org/project/nona)

```sh
# PyPI
pip install nona
```

## Dependencies

- [NumPy - Adds support for large, multi-dimensional arrays, matrices and high-level mathematical functions to operate on these arrays](https://www.numpy.org)
- [Pandas - Python data analysis toolkit]([pandas documentation &#8212; pandas 1.5.2 documentation](http://pandas.pydata.org/pandas-docs/stable/))
- [Scikit-Learn - machine learning in Python](https://scikit-learn.org/stable/)
- [GitHub - tqdm/tqdm: A Fast, Extensible Progress Bar for Python and CLI](https://github.com/tqdm/tqdm)

## Quick start

Out of the box, use ridge regression to fill in the gaps with the regression problem, and RandomForestClassifier for the classification problem in columns with missing values.

```python
# load library
from nona.nona import nona


# prepare your data with na to ML
# only numerical values ​​in the dataset


# fill the missing values
nona(YOUR_DATA)
```

## Accuracy improvement

You can insert other machine learning methods into the function. They should support a simple implementation of fit and predict.

Parameters:

- data: prepared dataset

- algreg: Regression algorithm to predict missing values ​​in columns

- algclss: Classification algorithm to predict missing values ​​in columns

```python
# load library
from nona.nona import nona


# prepare your data with na to ML
# only numerical values ​​in the dataset


# fill the missing values
nona(data=YOUR_DATA, algreg=make_pipeline(StandardScaler(with_mean=False), Ridge(alpha=0.1)), algclass=RandomForestClassifier(max_depth=2, random_state=0))
```

## Comparison of accuracy with other gap filling methods

[Framingham heart study dataset | Kaggle](https://www.kaggle.com/datasets/aasheesh200/framingham-heart-study-dataset)

![](https://ltdfoto.ru/images/2023/01/08/test_nona_fr.png)



Results of RMSE techniques for filling gaps depending on the percentage of missing values ​​in the dataset.

|                   | 10%  | 20%  | 30%  | 40%  | 50%  | 70%  | 90%  |
| ----------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **Baseline_MEAN** | 2.67 | 3.8  | 4.7  | 5.66 | 6.4  | 7.4  | 8.43 |
| **KNN**           | 2.48 | 3.7  | 4.57 | 5.55 | 6.35 | 7.47 | 8.49 |
| **MICE**          | 2.12 | 3.17 | 4.59 | 5.41 | 5.94 | 7.33 | 8.61 |
| **MISSFOREST**    | 2.26 | 3.36 | 4.31 | 5.33 | 6.15 | 8.06 | 9.85 |
| **NONA**          | 2.24 | 3.35 | 4.28 | 5.16 | 5.83 | 7.12 | 8.43 |
