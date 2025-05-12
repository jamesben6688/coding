class Classifier:
    def is_above_threshold(self, x, threshold):
        return 1 if x >= threshold else -1

    def has_error(self, label, should_be_label):
        return 0 if label == should_be_label else 1

    def train(self, x, y):
        # Step 1: Sort x and create pairs of (x, y)
        n = len(x)
        sorted_pairs = sorted(zip(x, y))  # Sort x and keep corresponding y values

        # Step 2: Initialize the variables for minimum errors and best threshold
        min_error_count = float('inf')
        best_threshold = None

        # Step 3: Iterate through sorted values to evaluate thresholds
        # We will consider every x_i as a possible threshold and calculate the error count
        # for that threshold.

        # First, initialize the error count by assuming the threshold is lower than any x.
        error_count = 0

        # Initialize two arrays, one to count errors when threshold is > xi
        # and the other for errors when threshold <= xi.
        prefix_errors = [0] * (n + 1)  # prefix_errors[i] counts errors for x[:i] below threshold
        suffix_errors = [0] * (n + 1)  # suffix_errors[i] counts errors for x[i:] above threshold

        # Fill prefix_errors (cumulative errors for x[0] to x[i-1])
        for i in range(n):
            xi, yi = sorted_pairs[i]
            prediction = self.is_above_threshold(xi, sorted_pairs[0][0])  # Arbitrary low threshold initially
            prefix_errors[i + 1] = prefix_errors[i] + self.has_error(prediction, yi)

        # Fill suffix_errors (cumulative errors for x[i:] considering xi as threshold)
        for i in range(n - 1, -1, -1):
            xi, yi = sorted_pairs[i]
            prediction = self.is_above_threshold(xi, sorted_pairs[-1][0])  # arbitrary max threshold initially
            suffix_errors[i] = suffix_errors[i + 1] + self.has_error(prediction, yi)

        # Iterate through possible thresholds and calculate errors for each threshold
        for i in range(1, n + 1):
            threshold = sorted_pairs[i - 1][0]
            current_error = prefix_errors[i] + suffix_errors[i]

            if current_error < min_error_count:
                min_error_count = current_error
                best_threshold = threshold

        return best_threshold
