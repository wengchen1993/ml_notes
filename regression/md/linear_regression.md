---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.7.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Linear Regression


Given one or more observable data points in n-dimensional spaces (independent variables) and  
corresponding scalar response (dependent variables): 

Linear regression attempts to model the relationship between independent variables and dependent variables in a
linear relationship.


## General Equation form


### Multivariate Linear Regression


$$ 
Y = W^{T}X + b 
$$


where:  
```
Y = dependent variables  (also known as response variables)
X = independent variables  (also known as predictor variables)
W = weights / gradients  
b = bias  
```

Note the term **b** is in lower case as it is a scalar value.  
The upper case letters are either vectors or matrices.


More specifically, the dimensions of the parameters are as below:

```
Y -> (1, num_targets)
W -> (num_features, 1)
X -> (num_features, num_data)
b -> scalar
```


### Useful tips


In Statistics, it is common practice to have feature **column** vector. 
This should server as a good reminder on the supposed dimension of parameters if one is struggling to define the shape.

Keeping this in mind, if we have 3 features to model after, our weight vector, W can be initialised randomly as such:  
    
```
W = np.random.randn(num_features, 1)
```


## Assumptions


### 1. Linear relationship between predictor and response variables.


If we were to expand the following term in the equation:

$ W^{T}X $

we get:
    
$ w_1x_1 + w_2x_2 ... + w_nx_n $ .

The change in term $w_ix_i$ is linear as we increase/decrease the weight. This results in the straight plotted line 
as seen in linear regression plots.


### Possible circumvention


If relationship between predictor and response variables are exponential, using log transform might help 
transforming this to a linear relationship.


### 2. Independence of Errors


Error term of observations should be uncorrelated with each other.   
If there is a correlation, this is known as autocorrelation.  
Any correlation might indicate that the feature itself is likely to not be linear which violatesthe first assumption.


### Possible circumvention


Add more predictor variables that can help predict the error term for the observations.


### 3. Homoscedascity


Homoscedascity is a term referring to constant variance. In this assumption, homoscedascity is referred in particular
to the response variables such that response variables have same variance regardless of values of predictor variables.

If variance is not constant i.e heteroscedascity, the coefficient estimates in linear regression will be less precise.
The lower in precision results in further deviation of coefficient estimates from the actual population value.


It is common that heteroscedascity caused by either temporal drift or the huge range of predictor variables.

**One classic example is:**  
Lower income family typically earns £30k with standard deviation of +/- £5k (lower bound of £25k and upper bound of £35k).  

Higher income family typically earns £80k with standard deviation of +/- £10k (lower bound of £70k and upper bound of 90k).

Despite we are sampling from the same population, higher income family may include bonuses in their income which tend
to vary a lot by sectors. This leads to greater standard deviation and thus heteroscedascity.


### Possible circumvention


Convert raw scalar features into rate / ratio to re-normalise the range.


### 4. Normal Distributed Errors


If this assumption is violated, p-value and confidence intervals raound coefficient estimate could be wrong, leading 
to incorrect conclusion on statistical significance of predictors.
