import numpy as np

# To generate random numbers
    # use np.random
random_number = np.random.rand()

print(random_number, "\n")
    # Output : A random value between 0 and 1


# To create a random number generator
    # use np.random.default_rng()
rng = np.random.default_rng()

random_number = rng.random()

print(random_number, "\n")
    # Output : A random value between 0 and 1


# To create a random array
    # use rng.random((rows, columns))
rng = np.random.default_rng()

arr = rng.random((2, 3))

print(arr, "\n")
    # Output :
    # [[random random random]
    #  [random random random]]


# To generate random integers
    # use rng.integers(low, high, size)
rng = np.random.default_rng()

arr = rng.integers(1, 10, size=5)

print(arr, "\n")
    # Output : 5 random integers from 1 to 9


# To generate random integers in a 2D array
    # use rng.integers(low, high, size=(rows, columns))
rng = np.random.default_rng()

arr = rng.integers(1, 10, size=(2, 3))

print(arr, "\n")
    # Output : A 2 × 3 array of random integers


# To generate random numbers from a normal distribution
    # use rng.normal(mean, standard_deviation, size)
rng = np.random.default_rng()

arr = rng.normal(0, 1, size=5)

print(arr, "\n")
    # Output : 5 random values from a normal distribution
    # mean = 0, standard deviation = 1


# To randomly select values from an array
    # use rng.choice()
rng = np.random.default_rng()

arr = np.array([10, 20, 30, 40, 50])

print(rng.choice(arr, size=3), "\n")
    # Output : 3 randomly selected values


# To set a seed for reproducible random numbers
    # use np.random.default_rng(seed)
rng = np.random.default_rng(42)

print(rng.integers(1, 10, size=5), "\n")
    # Output : [1 7 6 4 4]
    # Same seed → same sequence of random numbers


# To find the mean
    # use np.mean()
arr = np.array([10, 20, 30, 40, 50])

print(np.mean(arr), "\n")
    # Output : 30.0


# To find the median
    # use np.median()
arr = np.array([10, 20, 30, 40, 50])

print(np.median(arr), "\n")
    # Output : 30.0


# To find the standard deviation
    # use np.std()
arr = np.array([10, 20, 30, 40, 50])

print(np.std(arr), "\n")
    # Output : 14.142135623730951


# To find the variance
    # use np.var()
arr = np.array([10, 20, 30, 40, 50])

print(np.var(arr), "\n")
    # Output : 200.0


# To sort an array
    # use np.sort()
arr = np.array([40, 10, 30, 50, 20])

print(np.sort(arr), "\n")
    # Output : [10 20 30 40 50]


# To find the position of the minimum value
    # use np.argmin()
arr = np.array([40, 10, 30, 50, 20])

print(np.argmin(arr), "\n")
    # Output : 1
    # Minimum value 10 is at index 1


# To find the position of the maximum value
    # use np.argmax()
arr = np.array([40, 10, 30, 50, 20])

print(np.argmax(arr), "\n")
    # Output : 3
    # Maximum value 50 is at index 3


# To perform conditional operations
    # use np.where()
arr = np.array([10, 20, 30, 40, 50])

result = np.where(arr > 25, 1, 0)

print(result, "\n")
    # Output : [0 0 1 1 1]
    # 1 if condition is True, otherwise 0


# To check conditions on array elements
    # use boolean conditions
arr = np.array([10, 20, 30, 40, 50])

print(arr[arr > 25], "\n")
    # Output : [30 40 50]


# To create an array containing missing values
    # use np.nan
arr = np.array([10, 20, np.nan, 40, 50])

print(arr, "\n")
    # Output : [10. 20. nan 40. 50.]


# To check for missing or NaN values
    # use np.isnan()
arr = np.array([10, 20, np.nan, 40, 50])

print(np.isnan(arr), "\n")
    # Output : [False False  True False False]


# To ignore NaN values while calculating statistics
    # use np.nanmean()
arr = np.array([10, 20, np.nan, 40, 50])

print(np.nanmean(arr), "\n")
    # Output : 30.0


# To find the sum while ignoring NaN values
    # use np.nansum()
arr = np.array([10, 20, np.nan, 40, 50])

print(np.nansum(arr), "\n")
    # Output : 120.0