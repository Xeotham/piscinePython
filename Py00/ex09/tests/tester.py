from time import sleep
from tqdm import tqdm
from ft_package import Loading

for elem in Loading.ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()
