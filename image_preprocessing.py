from PIL import Image
import os
import albumentations as A
import matplotlib.pyplot as plt
from torchvision import transforms


def image_resize():
    targetDir = './jaguar'
    files = os.listdir(targetDir)
    for name in files:
        image_dir = './jaguar/' + name
        image = Image.open(image_dir)
        image_resize = image.resize((255,255))

        try:
            image_resize.save('./jaguar_re/' + name)
        except:
            continue

def image_aug():
    transform = A.Compose([
        A.HorizontalFlip(p=1),
    ])

    targetDir = './ex'
    files = os.listdir(targetDir)
    for name in files:
        image_dir = './ex/' + name
        image = plt.imread(image_dir)

        transformed = transform(image=image)
        transformed_image = transformed['image']

        image = transforms.ToPILImage()(transformed_image)
        image.save(os.path.join("./ex/", name.split('.')[0] + '_hor.jpg'))

def rename():
    targetDir = './leopard_aug'
    files = os.listdir(targetDir)
    index = 2989
    for name in files:
        index += 1
        image_dir = './leopard_aug/' + name
        image = Image.open(image_dir)

        image.save('./leopard_name/leopard_' + str(index) + '.jpg')


if __name__ == '__main__':
    image_aug()