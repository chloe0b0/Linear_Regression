# Linear_Regression
Simple Linear Regression model in Python and Numpy

linear_regressor.py is an implementation of simple linea regression using the [ordinary least squares method](https://en.wikipedia.org/wiki/Ordinary_least_squares). 

### Simple Linear Regression
[Simple Linear Regression](https://en.wikipedia.org/wiki/Simple_linear_regression) aims to find parameters alpha and beta for the best fit line of the form y = alpha + beta*x.


### Using the model
```py
model = linear_regression()

X = np.arange(start=1, stop=301)
y = np.random.normal(loc=x, scale=100)

model.fit(X, y)

print(model)
```
