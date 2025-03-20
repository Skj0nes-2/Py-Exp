
# Definitions - Establish definitions / Import definitions
def loadarr(name:str ):
    import numpy as np
    try:
        arr = np.load(f"{str(name)}.npy")
    except FileNotFoundError:
        arr = np.array([])
        np.save(str(name), arr)
    except Exception as e:
        print(f"Array {str(name)} failed to load!\nErr: {e}")
        arr = np.array([])
    return arr
      
def savearr(name:str, arr):
    import numpy as np
    try:
        np.save(str(name), arr)
    except Exception as e:
        print(f"Array {str(name)} failed to save!\nErr: {e}")
        
def autoPath(name):
    from os import path
    currentFile = path.realpath(__file__)
    currentFileName = path.basename(__file__)
    currentFilePath = currentFile.rstrip(currentFileName)
    path = f"{currentFilePath}{name}" 
    return path 

# Imports - Import Modules
import numpy as np

# Input - Take input from user

# Variables - Establish variables
mem = autoPath('mem')

# Load - Load persistent memory
arr = loadarr(mem) # Load array

# Main - Logic / Modify temporary memory / Modify persistent memory


# Output - Show Result / Write result to file
print(arr[1])

# Save - Save persistent memory
savearr(mem, arr) # Save array