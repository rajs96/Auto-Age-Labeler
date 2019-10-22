# Modeling

1. [Preprocessing](#prep)
2. [Feature Selection](#feat_select)
3. [Model Selection](#model_select)
4. [Results](#res)

<a name = "prep"></a>
## 1. Preprocessing
### Standard Scaler
Since many of our features are on different scales, using a feature scaler is
essential to any machine learning algorithm that uses gradient descent. When
features are on the same scale, gradient descent **tends** to reach a minimum
of the cost function faster, and a minimum that results in better model
predictions.

<a name = "feat_select"></a>
## 2. Feature Selection
A key part of this project is feature selection because we start out with 170
features. The scikit-learn library provides us easy ways of doing this.
### L1 Feature Selection
Using L1 regularization is a common way of selecting features in a machine learning
model. Adding the L1 norm to the cost function of any linear model penalizes less
important features. So, we create a logistic regression model with an L1 penalty,
and remove any features that have parameter values than 0.3. We also tried out
a support vector machine, but it failed to converge (recall that the support
vector machine is an optimization problem, and so it can fail to converge at a
minimum).
### Tree-based Feature Selection
We can get feature importances by using a random forest model. We create a
random forest of 50 trees and rank features that tend to appear closer to the
tree as higher, because this generally means that the feature provides a more
meaningful split in the data.
### Chi Squared Feature Selection
Coming soon.
### PCA Feature Selection
Finally, PCA is a very common dimensionality reduction technique that finds
n principal components, which means that we return the features that account
for the most variability in the data.

We tested these feature selection methods on the baseline model and got the best
results with tree-based feature selection, so we chose to proceed with this
feature selection approach when moving over to the more complex model.
<a name = "model_select"></a>
## 3. Model Selection
### Architecture Development
Coming soon.
### Hyperparameter Tuning
Coming soon.

<a name = "res"></a>
## 4. Results
### Performance metrics
Coming soon.
