# a script to define a function
# to output results of the model
import matplotlib.pyplot as plt
import itertools
from sklearn.metrics import confusion_matrix
from keras.models import Sequential
import numpy as np
from sklearn.metrics import classification_report

# function to
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()



def print_model_results(model,X_train,X_test,y_train,y_test,class_names):
	

	# testing results 
	testing_score = model.evaluate(X_test,y_test,batch_size=32)
	print("Results on primary testing set:")
	print("Loss: {}".format(testing_score[0]))
	print("Accuracy: {}".format(testing_score[1]))

	y_pred = model.predict(X_test)
	cnf_matrix = confusion_matrix(y_test.argmax(axis=1), y_pred.argmax(axis=1))

	# plot normal confusion matrix
	plt.figure()
	plot_confusion_matrix(cnf_matrix, classes=class_names,
                      title='Confusion matrix')

	# Plot normalized confusion matrix
	plt.figure()
	plot_confusion_matrix(cnf_matrix, classes=class_names, normalize=True,
                      title='Normalized confusion matrix')

	plt.show()

	print(classification_report(y_test.argmax(axis=1), y_pred.argmax(axis=1),
		target_names=class_names))




