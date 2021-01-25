# Item Count Algorithms 

This is the project about counting the number of items in images. 

# Features

There are two algorithms so far: 

1. OpenCV Based Algorithm

2. CNN Based Algorithm

# Requirements

``` Python
Python Version: 3.8 or later
Python Packages: PyTorch
```

# How to use

Download or Clone this repository.

## OpenCV Based 

Run the Jupyter Notebook file to generate the counting result. 

You can control your input image at `Load Data` part: 

``` Python
# Load Data

img = cv2.imread("[You image name].jpg") 
```

And the result will be output at `Show Results` part:

``` Python
# Show Results

cv2.imwrite('[Output name].jpg', img)
```

Examples are in `img` folder: 

![Input Image](img/input1.png)

![Output Image](img/output1.png)
