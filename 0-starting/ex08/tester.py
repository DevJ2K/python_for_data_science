from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm, ft_tqdm_responsive

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in ft_tqdm_responsive(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()
