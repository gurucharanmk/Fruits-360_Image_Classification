# Fruits-360_Image_Classification


### Overview

[Fruits 360 dataset](https://www.kaggle.com/moltean/fruits): A dataset of images containing fruits and vegetables by [Mihai Oltean](https://www.kaggle.com/moltean) includes below fruits and vegetables.

  
~~~~
Apples (different varieties: Crimson Snow, Golden, Golden-Red, Granny Smith, Pink Lady, Red, Red Delicious), Apricot, Avocado, Avocado ripe, Banana (Yellow, Red, Lady Finger), Beetroot Red, Blueberry, Cactus fruit, Cantaloupe (2 varieties), Carambula, Cauliflower, Cherry (different varieties, Rainier), Cherry Wax (Yellow, Red, Black), Chestnut, Clementine, Cocos, Corn (with husk), Cucumber (ripened), Dates, Eggplant, Fig, Ginger Root, Granadilla, Grape (Blue, Pink, White (different varieties)), Grapefruit (Pink, White), Guava, Hazelnut, Huckleberry, Kiwi, Kaki, Kohlrabi, Kumsquats, Lemon (normal, Meyer), Lime, Lychee, Mandarine, Mango (Green, Red), Mangostan, Maracuja, Melon Piel de Sapo, Mulberry, Nectarine (Regular, Flat), Nut (Forest, Pecan), Onion (Red, White), Orange, Papaya, Passion fruit, Peach (different varieties), Pepino, Pear (different varieties, Abate, Forelle, Kaiser, Monster, Red, Stone, Williams), Pepper (Red, Green, Orange, Yellow), Physalis (normal, with Husk), Pineapple (normal, Mini), Pitahaya Red, Plum (different varieties), Pomegranate, Pomelo Sweetie, Potato (Red, Sweet, White), Quince, Rambutan, Raspberry, Redcurrant, Salak, Strawberry (normal, Wedge), Tamarillo, Tangelo, Tomato (different varieties, Maroon, Cherry Red, Yellow, not ripened, Heart), Walnut, Watermelon.
~~~~
  

### Implementation details

| Feature | Brief Explanation |
| ------ | ------ |
| Base Model Architecture | Resnet50 from [ResNet](https://arxiv.org/abs/1512.03385) family, implementation from [PyTorch](https://pytorch.org/)|
| Learning Rate Finder | [Learning rate finder](https://arxiv.org/abs/1506.01186) implementation from [FastAI](https://www.fast.ai/) |
| Learning rate and Momentum scheduler| [One cycle policy](https://arxiv.org/abs/1803.09820) implementation from [FastAI](https://www.fast.ai/) to achieve superconvergence |
| Loss function| [Focal Loss](https://arxiv.org/pdf/1708.02002.pdf) due to imbalanced dataset |
| Dataset | Dataset [Fruits 360 dataset](https://www.kaggle.com/moltean/fruits) from [Mihai Oltean](https://www.kaggle.com/moltean) |

  
  

### Results

| Model | Metrics(Accuracy) | Epochs |
| ------ | ------ | ------ |
| Resnet50 | 99.6121 % | 12 |

  
#### Focal Loss

![Alt text](https://github.com/gurucharanmk/Fruits-360_Image_Classification/blob/main/images/loss.png )

#### Inference

![Alt text](https://github.com/gurucharanmk/Fruits-360_Image_Classification/blob/main/images/results.png )

  

## License

This project is licensed under the [MIT License](https://github.com/gurucharanmk/Fruits-360_Image_Classification/blob/main/LICENSE)opening the **file explorer** on the left corner of the navigation bar.
