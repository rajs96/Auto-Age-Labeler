## helper functions that datasets with a reduced
## number of features. Common feature selection
## methods from sklearn are included.

# Feature selection methods to try
# 1.) L1-based feature selection
# 2.) chi-square feature selection
# 3.) tree based feature selection

from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectFromModel,SelectKBest,chi2
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA


def lasso_feature_selection(X,y,penalty=0.01,model='svm',threshold=0.3):
    """Function that returns dataset with L1 feature selection applied.

    Args:
        X -- training dataset for inputs
        y -- training datsets for outputs
        penalty -- L1 regularization penalty
        model -- chosen linear model for applying L1 regularization
        threshold -- if parameter has a weight lower than 0.3, delete it
    Returns:
        X_transformed,clf (tuple) -- new dataset with features selected, along
        with object that transforms the data
    """
    if model == 'svm':
        lasso_model = LinearSVC(penalty='l1',C=penalty,dual=False)
    else:
        # model is logistic regression
        lasso_model = LogisticRegression(penalty='l1',C=penalty)

    clf = SelectFromModel(lasso_model,threshold=threshold)
    clf.fit(X,y)

    # transform data using L1 regularization
    X_transformed = clf.transform(X)
    return (X_transformed,clf)

def tree_based_feature_selection(X,y,n_estimators=50):
    """Function that returns dataset with tree-based feature selection applied

    Args:
        X -- training dataset for inputs
        y -- training dataset for outputs
        n_estimators -- number of trees used in the feature selector

    Returns:
        X_transformed,clf (tuple) -- new dataset with features selected, along
        with object that transforms the data
    """
    tree_model = ExtraTreesClassifier(n_estimators=n_estimators)
    tree_model.fit(X,y)
    model = SelectFromModel(tree_model,prefit=True)
    X_transformed = model.transform(X)
    return (X_transformed,model)

def chi_squared_feature_selection(X,y,k=80):
    """Function that returns dataset with chi-squared based feature selection

    Args:
        X -- training dataset for inputs
        y -- training dataset for outputs
        k -- number of features to select

    Returns:
        X_transformed,model (tuple) -- new dataset with features selected, along
        with object that transforms the data
    """

    # need to min max scale data first because Chi2 doesn't take negative values
    min_max_scaler = MinMaxScaler()
    X_scaled = min_max_scaler.fit_transform(X)
    transformer = SelectKBest(chi2,k=k)
    X_transformed = transformer.fit_transform(X_scaled,y)
    return (X_transformed,transformer)

def pca_feature_selection(X,k=80):
    """Function that returns dataset k principal components selected

    Args:
        X -- training dataset for inputs
        k -- number of features to select

    Returns:
        X_transformed,pca (tuple) -- new dataset with features selected, along
        with object that transforms the data
    """
    pca = PCA(n_components=k)
    pca.fit(X)
    # takes k principal components
    X_transformed = pca.transform(X)
    return (X_transformed,pca)
