Minimization expansion
This addition to the AI Privacy Toolkit was done as a part of the Data Protection Technologies course at UvA and extends the minimization module. This expansion aims to implement k-anonymity in data minimization. If a dataset has k-anonymity, it means that each subject is indistinguishable from at least k-1 other subjects with respect to quasi-identifiers. This makes it harder to connect specific individuals to their sensitive information. The reason for this implementation is that the current minimization is done with respect to the model accuracy. Generalisations are made to increase data privacy; thus, there should be an option to make generalisations to achieve a target level of data privacy. For this expansion, k-anonymity was chosen because it is a simple way to measure data privacy. However, k-anonymity remains vulnerable to homogeneity attacks, but this expansion can serve as a proof of concept, and additional data privacy measurements can be added in future work.

apt/minimization/minimiser_expansion
This new file contains functions to calculate k-anonymity

- k_anonymity(data):
This function returns the k-anonymity of the input data. It does this by retrieving the number of entries for each feature combination (combinations with 0 entries are not counted). The returned value is the number of entries for the combination with the fewest entries.

- has_k_anonymity(data, target_k):
This function returns a boolean indicating whether the input dataset has k-anonymity, based on the input target_k value. It does this by calculating the dataset's k-anonymity using the k_anonymity function. It returns a boolean indicating whether the target_k has been reached.

## apt/minimization/minimizer
The minimizer contains all of its original functionality. It can still generalise data with respect to a target accuracy. The new functionality uses the minimiser_expansion file to add a feature that lets you generalise data with respect to a target k-anonymity. Two optional parameters are added to the GeneralizeToRepresentative initialization, 'mode' and 'target_k'. 'mode' has two values: ACCURACY_MODE and K_ANONYMITY_MODE, with the default value being ACCURACY_MODE. The target_k parameter is used to determine whether the dataset has reached the appropriate k-anonymity.

If mode=ACCURACY_MODE, then the minimizer runs as it did originally. If mode=K_ANONYMITY_MODE, the minimiser generalises with respect to the k-anonymity. If the dataset has not achieved the target k-anonymity, further generalisations are made until the target is reached. If the k-anonymity exceeds the target, generalisations are reduced until the target k-anonymity is reached. 

What this essentially aims to do is achieve 2 goals: the main goal is to reach the target k-anonymity, and the secondary goal is to obtain the highest possible model accuracy while achieving the target k-anonymity.

## notebooks/testing_expansion
This notebook provides an example of how to use the new functionality. It demonstrates that the original minimization functionality remains intact, tested at a target accuracy of 90%, and that the new functionality is tested at a target k-anonymity of 2.