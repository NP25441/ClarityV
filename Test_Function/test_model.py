from keras.models import load_model

model = load_model('model_car(VGG16)')
model.summary()
print("Loaded Model from disk")

# compile and evaluate loaded model

print(model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy']))
