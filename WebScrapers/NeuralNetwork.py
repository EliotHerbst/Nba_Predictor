from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
# load the dataset
data_set = loadtxt('TrainingData20.csv', delimiter=',')
data_set_training = data_set[0: int(float(len(data_set)) * 0.75)]
data_set = data_set[int(float(len(data_set)) * 0.75):]
# split into input (X) and output (y) variables
X = data_set_training[:, 0:28]
y = data_set_training[:, 28]
X_Test = data_set[:, 0:28]
Y_Test = data_set[:, 28]
# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=28, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10, verbose=0)
# make class predictions with the model
predictions = model.predict_classes(X_Test)
# check accuracy
correct = 0.0
incorrect = 0.0
for x in range(len(predictions)):
	if predictions[x] == Y_Test[x]:
		correct += 1
	else:
		incorrect += 1
print(str(correct) + " " + str(incorrect) + " " + str(100 * correct / (correct + incorrect)))