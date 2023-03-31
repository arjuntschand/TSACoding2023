import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Model

# Load the data from the CSV file
data = pd.read_csv('/Users/anijain/Documents/GitHub/TSACoding2023/Pet Characteristics - Sheet1.csv')

# Encode the categorical variables as numerical features
data['Energy Level'] = data['Energy Level'].replace({'Lazy': 0, 'Playful': 1, 'Energetic': 2})
data['Free Time Required'] = data['Free Time Required'].replace({'0-2 Hours': 0, '2-4 Hours': 1, '4-8 Hours': 2, '8+ Hours': 3})
data['Experience Required'] = data['Experience Required'].replace({'None': 0, '1-3 years': 1, '3-5 years': 2, '5+ years': 3})
data['Pet Type'] = data['Pet Type'].replace({'Cat': 0, 'Dog': 1, 'Bird': 2, 'Hamster': 3, 'Other': 4})
data['Breed'] = data['Breed'].astype('category').cat.codes

# Split the data into training and testing sets
train_data = data.sample(frac=0.8, random_state=42)
test_data = data.drop(train_data.index)

# Split the features and targets
train_features = train_data[['Energy Level', 'Free Time Required', 'Experience Required']].values
train_targets = [train_data['Pet Type'].values, train_data['Breed'].values]
test_features = test_data[['Energy Level', 'Free Time Required', 'Experience Required']].values
test_targets = [test_data['Pet Type'].values, test_data['Breed'].values]

# Define the input shape
inputs = Input(shape=(3,))

# Define the layers
x = Dense(64, activation='relu')(inputs)
x = Dense(32, activation='relu')(x)
x = Dense(16, activation='relu')(x)

# Define the outputs
pet_type = Dense(5, activation='softmax', name='pet_type')(x)
breed = Dense(len(data['Breed'].unique()), activation='softmax', name='breed')(x)

# Define the model
model = Model(inputs=inputs, outputs=[pet_type, breed])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_features, train_targets, epochs=50, batch_size=32, validation_split=0.2)

# Evaluate the model on the test data
model.evaluate(test_features, test_targets)

