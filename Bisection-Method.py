def bisection_method(a, b, func, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        print("Bisection method fails.")
        return None
    else:
        iter_count = 0
        while ((b - a) >= tol) and (iter_count < max_iter):
            mid = a + (b - a) / 2.0

            if func(mid) == 0.0:
                break
            elif func(mid) * func(a) < 0:
                b = mid
            else:
                a = mid
            iter_count += 1

        return mid

# Test function
def func(x):
    return x * x - x - 1

# Test the function
root = bisection_method(1, 2, func)
if root is not None:
    print("Root of the function is : ", "%.6f" % root)