# The following code will only execute
# successfully when compression is complete

import kagglehub

# Download latest version
path = kagglehub.dataset_download("dilshan49/got10k-mini-1")

print("Path to dataset files:", path)

