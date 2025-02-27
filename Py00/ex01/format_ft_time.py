from time import time, strftime

date = time()

print("Seconds since January 1, 1970:", f"{date:,}", "or", f"{date:.3}", "in scientific notation")
print(strftime("%b %d %Y"))
