"""
Program #4: Image Comparison
COSC 1306, Spring 2016
This program determines the three closest images
to a base image using Euclidean and Hamming distance.
"""

from PIL import Image
import numpy as np

# Function that generates a histogram for an image
def image_histogram(im):

    im_vals1 = np.zeros(256)
    im_vals2 = np.zeros(256)
    im_vals3 = np.zeros(256)

    r,g,b = im.split()

    pixels_r = list(r.getdata())
    pixels_g = list(g.getdata())
    pixels_b = list(b.getdata())
    pix_r = np.array(pixels_r)
    pix_g = np.array(pixels_g)
    pix_b = np.array(pixels_b)
    for idx in range (0, len(pix_r)):
        im_vals1[pix_r[idx]] += 1
        im_vals2[pix_g[idx]] += 1
        im_vals3[pix_b[idx]] += 1

    histogram = list(im_vals1) + list(im_vals2) + list(im_vals3)
    return histogram

""""
2) Function that computes the Euclidean distance between two images' histograms
"""

# Set function name and parameters
def euclidean_distance(s1, s2):
    # Assigns the variable total to 0
    total = 0
    # Iterates through each element in the histogram
    for i in range(len(s1)):
        # Calculates (xn - yn)**2 and adds it to the total
        total += (s1[i] - s2[i]) ** 2
    # Calculates the square root of the total to give the Euclidean distance
    eu_dist = total ** 0.5
    # Returns the Euclidean distance
    return eu_dist

"""
3) Function taht determines the Hamming distance between two images' histograms
"""

# Set function name and parameters
def hamming_distance(s1, s2):
    # Assigns the variable ham_dist to 0
    ham_dist = 0
    # Iterates through each element in the histogram
    for i in range(len(s1)):
        # Checks if the two elements are equal
        if s1[i] != s2[i]:
            # If the two elements are not equal, add 1 to the Hamming distance
            ham_dist = ham_dist + 1
    # Returns the hamming distance
    return ham_dist

"""
1) Compute sum of 0.jpg's histogram and report the result
"""

# Opens 0.jpg and sets it as a variable
img0 = Image.open("0.jpg")
# Generates the histogram of 0.jpg and sets it as a variable
histogram0 = image_histogram(img0)
# Calculates the sum of the histogram of 0.jpg
sum0 = sum(histogram0)
# Reports the result
print("Sum of 0.jpg's histogram:", sum0)

"""
4) Compare 50 images and find 3 closest images with Euclidean and Hamming distance
"""

# Generates a histogram for every image and saves them in a list
histograms = []
for i in range(1000):
    img = Image.open(str(i)+".jpg")
    histograms.append(image_histogram(img))

# Sets table to an empty list to create the table
table = []
# Sets first row of table as description of columns
table.append(["Image", "Closest using Euclidean", "Closest using Hamming",
              "Which among the 2 is most similar to the original photo"])

# Assigns i to zero as start of while loop
i = 0
# Loops through the histogram of each image and checks for which are closest
while i < 999:
    # Creates a temporary list to add to the table later
    temp = []
    # Appends the image number being compared to the temporary list
    temp.append(i)
    # Assigns 3 variables for top 3 closest images using Euclidean distance to high values
    eu1, eu2, eu3 = 50000, 50000, 50000
    # Assigns 3 variables for the image number of the 3 closest images
    eu1Num, eu2Num, eu3Num = 0, 0, 0
    # Assigns 3 variables for top 3 closest images using Hamming distance to high values
    ham1, ham2, ham3 = 800, 800, 800
    # Assigns 3 variables for the image number of the 3 closest images
    ham1Num, ham2Num, ham3Num = 0, 0, 0
    # For loop that iterates through each histogram
    for j in range(0, 999):
        # Assigns variable eu_dist to the Euclidean distance between 2 histograms
        eu_dist = euclidean_distance(histograms[i], histograms[j])
        # Set condition for eu_dist so that it does not give the base image as a result
        if eu_dist > 0:
            # If-else statements that determine top 3 closest images
            if eu_dist < eu1:
                eu3 = eu2
                eu2 = eu1
                eu1 = eu_dist
                eu3Num = eu2Num
                eu2Num = eu1Num
                eu1Num = j
            elif eu_dist < eu2:
                eu3 = eu2
                eu2 = eu_dist
                eu3Num = eu2Num
                eu2Num = j
            elif eu_dist < eu3:
                eu3 = eu_dist
                eu3Num = j
        # Assigns variable eu_dist to the Hamming distance between 2 histograms
        ham_dist = hamming_distance(histograms[i], histograms[j])
        # Set condition for eu_dist so that it does not give the base image as a result
        if ham_dist > 0:
            # If-else statements that determine top 3 closest images
            if ham_dist < ham1:
                ham3 = ham2
                ham2 = ham1
                ham1 = ham_dist
                ham3Num = ham2Num
                ham2Num = ham1Num
                ham1Num = j
            elif ham_dist < ham2:
                ham3 = ham2
                ham2 = ham_dist
                ham3Num = ham2Num
                ham2Num = j
            elif ham_dist < ham3:
                ham3 = ham_dist
                ham3Num = j
    # Appends results to the table
    temp.append(str(eu1Num) + ", " + str(eu2Num) + ", " + str(eu3Num))
    temp.append(str(ham1Num) + ", " + str(ham2Num) + ", " + str(ham3Num))
    # If statement that determines which method was closer to the base image in my opinion
    # and appends it to the temp list
    if eu1 < ham1 * 10:
        sim = "I think " + str(eu1Num) + ", " + str(eu2Num) + ", and " + str(eu3Num) + " are more similar to " + str(i)
        temp.append(sim)
    else:
        sim = "I think " + str(ham1Num) + ", " + str(ham2Num) + ", and " + str(ham3Num) + " are more similar to " \
              + str(i)
        temp.append(sim)
    # Appends the temporary list to the table
    table.append(temp)
    # Adds 49 to get the second image and adds 50 for subsequent images
    if i == 0:
        i += 49
    else:
        i += 50
# Prints table
for i in range(len(table)):
    for j in range(len(table[i])):
        print("%*.70s" %(25, table[i][j]), end=" ")
    print()
