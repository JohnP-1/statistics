import numpy as np


def t_value_1sided(mu, s, n, mu_0):

    return (mu - mu_0) / (s / np.sqrt(n))


def t_value_2sided(mu_1, mu_2, s_pooled, n_1, n_2):

    return (mu_1 - mu_2) / (s_pooled * np.sqrt((1 / n_1) + (1 / n_2)))


def f_value(s_1, s_2):

    return (s_1 ** 2) / (s_2 ** 2)


def chi_squared_value(obs, exp):

    return np.sum(((obs - exp) ** 2) / exp)


### t_value_1sided

mu = 5
s = 2
n = 50
mu_0 = 5

t = t_value_1sided(mu, s, n, mu_0)
print(f't-value = {t}')


### t_value_2sided

mu_1 = 5
mu_2 = 3
s_pooled = 2
n_1 = 50
n_2 = 3

t = t_value_2sided(mu_1, mu_2, s, n_1, n_2)
print(f't-value = {t}')


### F_value

s_1 = 4
s_2 = 4

f = f_value(s_1, s_2)
print(f'f-value = {f}')


### Chi_squared_value

obs = np.array([1, 2, 3])
exp = np.array([1, 100, 3])
chi_squared = chi_squared_value(obs, exp)
print(f'chi_squared-value = {chi_squared}')