from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# load the data
data_set = loadtxt('TrainingData20.csv', delimiter=',')
testing_set = loadtxt('TrainingDataTest20.csv', delimiter=',')
# create scaler
scaler = MinMaxScaler()
scaler_s = StandardScaler()
# split into input (X) and output (y) variables
X = data_set[:, 0:28]
# normalized_x = scaler.fit_transform(X)
# standardized_x = scaler_s.fit_transform(normalized_x)
y = data_set[:, 28]
X_secondary_Test = testing_set[:, 0:28]
# normalized_x_test = scaler.fit_transform(X_secondary_Test)
# standardized_x_test = scaler_s.fit_transform(normalized_x_test)
Y_secondary_Test = testing_set[:, 28]
# define the keras model
early_stopping_monitor = EarlyStopping(patience=20)
model = Sequential()
model.add(Dense(28, input_dim=28, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(14, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=100, validation_split=0.2, batch_size=10, verbose=2, callbacks=[early_stopping_monitor])
# make class predictions with the model
predictions = model.predict_classes(X_secondary_Test)
# check accuracy
correct = 0.0
incorrect = 0.0
for x in range(len(predictions)):
	if predictions[x] == Y_secondary_Test[x]:
		correct += 1
	else:
		incorrect += 1
print(str(correct) + " " + str(incorrect) + " " + str(100 * correct / (correct + incorrect)))

