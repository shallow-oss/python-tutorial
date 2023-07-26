import numpy as np
import io
from io import BytesIO

data = "1, 2, 3\n4, 5, 6"

print(np.genfromtxt(BytesIO(data.encode()), delimiter=","))
