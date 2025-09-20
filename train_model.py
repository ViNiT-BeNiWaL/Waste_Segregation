import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import json

# --- Configuration ---
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 64
EPOCHS = 10
VALIDATION_SPLIT = 0.2  # Use 20% of the data for validation
DATA_DIR = 'dataset/train'

# --- GPU Configuration ---
# Check for GPU and allow TensorFlow to allocate all memory by default
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"✅ GPU(s) found: {len(gpus)}. TensorFlow will allocate available GPU memory.")
    # By removing 'tf.config.experimental.set_memory_growth', we revert to
    # the default behavior, which is to allocate memory upfront.
else:
    print("❌ No GPU found. Training will happen on the CPU.")

# --- 1. Data Augmentation and Loading ---
datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest',
    validation_split=VALIDATION_SPLIT
)

train_generator = datagen.flow_from_directory(
    DATA_DIR,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)

validation_generator = datagen.flow_from_directory(
    DATA_DIR,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

# --- 2. Model Building (Transfer Learning) ---
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
num_classes = len(train_generator.class_indices)
predictions = Dense(num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

# --- 3. Compile the Model ---
model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

# --- 4. Train the Model ---
print("\n🚀 Starting model training...")
history = model.fit(
    train_generator,
    epochs=EPOCHS,
    validation_data=validation_generator
)

# --- 5. Save the Trained Model & Class Indices ---
model.save('model.h5')
print("\n✅ Training complete! Model saved as model.h5")

with open('class_indices.json', 'w') as f:
    json.dump(train_generator.class_indices, f)
print("✅ Class indices saved to class_indices.json")