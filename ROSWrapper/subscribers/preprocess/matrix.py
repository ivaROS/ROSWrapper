import numpy as np
def multiArray_to_np(multi_array_msg, shape=None):
    """Convert the multi array message to numpy matrix.
    Now only convert to the float64 data
    """
    if shape is None:
        # TODO: reconstruct the array according to the stored dimension.
        # see for example:  https://gist.github.com/jarvisschultz/7a886ed2714fac9f5226
        raise NotImplementedError
    else:
        array = np.array(multi_array_msg.data).reshape(shape)

    return array
     