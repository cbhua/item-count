# Item Count Algorithms 

This is the project about counting the number of items in images by algorithms. This is a working on project, will update time by time. 

# Features

- [x] OpenCV Based Algorithm 

  Item detection based on methods provided by [OpenCV](https://opencv.org/) package, include *image grayscale*, *image binarization*, *edge detector* and *drawing edges*. 

- [x] Convolutional Neural Network Based Algorithm

  Item detection based on OpenCV method will meet the problem that the accuracy is poor if items get together. To improve this, we prefer to use some methods based on machine learning, the most basic model is CNN. 

# Requirements

``` Python
Python Version: 3.8 or later
Python Packages: PyTorch
```

# How to use

[Download](https://github.com/cbhua/project-item-count/archive/main.zip) or [Clone](https://github.com/cbhua/project-item-count.git) this repository.

## OpenCV Based Algorithm

Run the Jupyter Notebook file to generate the counting result. 

You can choose your input image at `Load Data` part: 

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

![Input Image](/opencv-based/img/input1.png)

![Output Image](/opencv-based/img/output1.png)
