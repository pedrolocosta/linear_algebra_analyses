k-nearest neighbors (KNN) algorithm

The k-nearest neighbors (KNN) algorithm is a popular distance-based 
machine learning algorithm that can be used to perform both 
classification and regression tasks.

How it works
If we wanted to classify a new observation (represented by the question 
mark) into one of two classes, we would simply find the closest observation 
and assign its class to our new point. The distance used to compare the 
two observations can be Euclidean or Manhattan K-NN works on the same 
principle.

See how the k-NN algorithm works:
	• Step 1: We select the number (k) of neighbors we want to see.
	
    • Step 2: We calculate the distance between the new observation and 
    the other points in our data. By default, the Euclidean distance is 
    selected, but we can also use the Manhattan, Minkowski, or Hamming 
    distances.
	
    • Step 3: We order the distances from smallest to largest and 
    consider the k nearest neighbors.
	
    • Step 4: Finally, we attribute our new observation to the majority 
    class.

It is possible to import the KNN algorithm from the sklearn library but I 
will build my own as an experience.
