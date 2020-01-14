"""
@author: Anirudh Sharma
"""

def exception_examples():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("a/b:", a/b)
        print("a+b:", a+b)
    except ValueError:
        print("Could not convert to a number")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except:
        print("Something went wrong")
    finally:
        print("Always executes!!!")
        
    
exception_examples()
    

def get_ratios(L1, L2):
    """
    Assumes: L1 and L2 are lists of equal length
    Returns: A list containing L1[i]/L2[i]
    """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index] / L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) # nan - not a number
        except:
            raise ValueError("Bad argument occurred")
    return ratios

a = [6, 4, -2, 7]
b = [2, 6, 0, 8]
print(get_ratios(a, b))