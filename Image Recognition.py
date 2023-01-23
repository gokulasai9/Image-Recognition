from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import imagenet_utils

root = Tk()
root.geometry("900x720")
root.title("Image Captioning")


def open_image():
    global my_img_label, my_img2,a
    filename = filedialog.askopenfilename(
        initialdir='/', title="title", filetypes=(("All files", "*.*"), ("Txt file", "*.txt")))
    im = Image.open(filename)
    im = im.resize((440,440))
    mobile1 = tf.keras.applications.mobilenet_v2.MobileNetV2()
    anyone = tf.keras.applications.DenseNet201
    img = image.load_img(filename,target_size=(224,224))
    resized_img = image.img_to_array(img)
    final_img = np.expand_dims(resized_img,axis=0)
    final_img = tf.keras.applications.mobilenet.preprocess_input(final_img)
    predictions1 = mobile1.predict(final_img)
    result = imagenet_utils.decode_predictions(predictions1)
    m = Image.open(filename)
    my_img1 = m.resize((400, 400))
    my_img2 = ImageTk.PhotoImage(my_img1)
    my_img_label = Label(image=my_img2)
    my_img_label.pack()
    a = result[0][0][1]
    pred_label.config(text=a)

select = Label(root, text="Select A Image", font="Raleway")
select.pack()
select_button = Button(root, text="predict", command=open_image)
select_button.pack()
pred_label = Label(root,text="")
pred_label.pack()
root.mainloop()