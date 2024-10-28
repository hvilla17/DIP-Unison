# Does not work
# Exception raised in line 40
# It seems there is conflict between keras and tensorflow.keras

import keras_applications
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras_applications.vgg19 import VGG19
from keras_preprocessing.image import load_img, img_to_array
from tensorflow.python.keras.models import Model
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.optimizer_v2 import adam as adam_v2

print(tf.__version__)

# Set the backend manually
K.set_image_data_format('channels_last')

# Helper functions for loading and processing images
def load_and_process_image(image_path, target_size=(400, 400)):
    img = load_img(image_path, target_size=target_size)
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = keras_applications.vgg19.preprocess_input(img)
    return img


def deprocess_image(image):
    img = image.copy()
    img[:, :, 0] += 103.939
    img[:, :, 1] += 116.779
    img[:, :, 2] += 123.68
    img = img[:, :, ::-1]
    img = np.clip(img, 0, 255).astype('uint8')
    return img


# Define model layers for content and style extraction
def get_model():
    vgg = VGG19(include_top=False, weights='imagenet')
    vgg.trainable = False

    style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1', 'block4_conv1', 'block5_conv1']
    content_layers = ['block5_conv2']

    style_outputs = [vgg.get_layer(name).output for name in style_layers]
    content_outputs = [vgg.get_layer(name).output for name in content_layers]

    model_outputs = style_outputs + content_outputs
    return Model(vgg.input, model_outputs)


# Content loss function
def content_loss(base_content, target):
    return tf.reduce_mean(tf.square(base_content - target))


# Gram matrix for style representation
def gram_matrix(input_tensor):
    result = tf.linalg.einsum('bijc,bijd->bcd', input_tensor, input_tensor)
    input_shape = tf.shape(input_tensor)
    num_locations = tf.cast(input_shape[1] * input_shape[2], tf.float32)
    return result / num_locations


# Style loss function
def style_loss(base_style, gram_target):
    height, width, channels = base_style.get_shape().as_list()
    gram_style = gram_matrix(base_style)
    return tf.reduce_mean(tf.square(gram_style - gram_target))


# Total loss calculation
def compute_loss(model, loss_weights, init_image, gram_style_features, content_features):
    style_weight, content_weight = loss_weights

    model_outputs = model(init_image)

    style_output_features = model_outputs[:len(gram_style_features)]
    content_output_features = model_outputs[len(gram_style_features):]

    style_score = 0
    content_score = 0

    for target_style, comb_style in zip(gram_style_features, style_output_features):
        style_score += style_loss(comb_style, target_style)

    for target_content, comb_content in zip(content_features, content_output_features):
        content_score += content_loss(comb_content, target_content)

    style_score *= style_weight
    content_score *= content_weight
    loss = style_score + content_score
    return loss


# Extract features
def get_feature_representations(model, content_image, style_image):
    content_outputs = model(content_image)
    style_outputs = model(style_image)

    style_features = [style_layer for style_layer in style_outputs[:5]]
    content_features = [content_layer for content_layer in content_outputs[5:]]
    return style_features, content_features


# Optimizer and training step
def compute_grads(cfg):
    with tf.GradientTape() as tape:
        all_loss = compute_loss(**cfg)
    total_loss = all_loss
    return tape.gradient(total_loss, cfg['init_image']), all_loss


# Neural Style Transfer function
def run_style_transfer(content_path, style_path, iterations=1000, content_weight=1e3, style_weight=1e-2):
    model = get_model()

    for layer in model.layers:
        layer.trainable = False

    content_image = load_and_process_image(content_path)
    style_image = load_and_process_image(style_path)

    style_features, content_features = get_feature_representations(model, content_image, style_image)

    gram_style_features = [gram_matrix(style_feature) for style_feature in style_features]

    init_image = tf.Variable(content_image, dtype=tf.float32)
    opt = adam_v2.Adam(learning_rate=5.0)

    best_loss, best_img = float('inf'), None

    loss_weights = (style_weight, content_weight)

    cfg = {
        'model': model,
        'loss_weights': loss_weights,
        'init_image': init_image,
        'gram_style_features': gram_style_features,
        'content_features': content_features,
    }

    norm_means = np.array([103.939, 116.779, 123.68])
    min_vals = -norm_means
    max_vals = 255 - norm_means

    for i in range(iterations):
        grads, all_loss = compute_grads(cfg)
        loss = all_loss
        opt.apply_gradients([(grads, init_image)])

        clipped = tf.clip_by_value(init_image, min_vals, max_vals)
        init_image.assign(clipped)

        if loss < best_loss:
            best_loss = loss
            best_img = np.array(init_image)

        if i % 100 == 0:
            print(f"Iteration: {i}, Loss: {loss}")

    return best_img


# Running Neural Style Transfer
content_image_path = 'content.png'
style_image_path = 'style.png'

best_image = run_style_transfer(content_image_path, style_image_path, iterations=1000)

# Display the final output
best_img = deprocess_image(best_image[0])
plt.imshow(best_img)
plt.show()
