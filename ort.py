import matplotlib.pyplot as plt

data =[[10,10,10,10,10,10,10,10,10,10,5,10,10,10,10],
       [10,10,10,10,10,10,10,10,10,9,6,5,10,10,10],
       [10,10,10,10,10,10,10,10,9,9,9,6,5,10,10],
       [10,10,10,10,10,10,10,9,9,1,9,9,6,5,10],
       [10,10,10,10,10,10,9,9,9,9,9,9,6,5,10],
       [10,10,10,10,10,9,9,9,9,1,9,9,6,5,10],
       [10,10,10,10,9,9,9,9,9,9,9,6,5,5,10],
       [10,10,10,9,9,9,9,1,9,9,9,6,5,5,10],
       [10,10,9,1,9,1,9,9,9,9,6,5,5,10,10],
       [10,5,6,9,9,9,9,9,9,9,6,5,10,10,10],
       [10,10,5,6,6,6,6,6,6,6,5,10,10,10,10],
       [10,10,10,5,5,5,5,5,5,5,10,10,10,10,10]]

plt.imshow(data, cmap = 'nipy_spectral')
plt.show()

#this code is totoally not scuffed and totally not copied off of byju's future school