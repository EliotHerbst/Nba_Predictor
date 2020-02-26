from keras.callbacks import EarlyStopping
from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# load dataset
dataframe = read_csv("TrainingData20.csv", header=None)
dataset = dataframe.values
secondary_test = read_csv("TrainingDataTest20.csv", header=None)
secondary = secondary_test.values
# split into input (X) and output (Y) variables
X = dataset[:, 0:28].astype(float)
Y = dataset[:, 28]
X_Test = secondary[:, 0:28].astype(float)
Y_Test = secondary[:, 28]
# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)

encoder_2 = LabelEncoder()
encoder_2.fit(Y_Test)
encoded_TY = encoder_2.transform(Y_Test)
early_stopping_monitor = EarlyStopping(patience=20)

# baseline model
def create_baseline():
    # create model
    model = Sequential()
    model.add(Dense(28, input_dim=28, activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(14, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


# evaluate baseline model with standardized dataset
# evaluate model with standardized dataset
estimator = KerasClassifier(build_fn=create_baseline, epochs=100, batch_size=5, verbose=0)
kfold = StratifiedKFold(n_splits=10, shuffle=True)
results = cross_val_score(estimator, X, encoded_Y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))

