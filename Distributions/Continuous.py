import numpy as np
from scipy.special import gamma, betainc, beta
import matplotlib.pyplot as plt
from Base import Base


class Student_t(Base):

    def __init__(self):
        pass

    def pdf(self, t, df):
        '''

        :param t: student t value
        :param v: degrees of freedom
        :return:
        '''

        y = (gamma((df + 1) / 2) / (np.sqrt(v * np.pi) * gamma(df / 2))) * ((1 + ((t**2) / df)) ** (-1 * ((df + 1) / 2)))

        return y

    def cdf(self, t, df):

        x_t = df / (t**2 + df)
        y = 1 - betainc(df/2, 0.5, x_t)
        if t < 0:
            y = y * -1

        y = (y + 1) * 0.5

        return y


    def sample(self):
        pass


class F(Base):

    def __init__(self):
        pass

    def pdf(self, x, df_1, df_2):

        f = np.sqrt(((df_1 * x)**df_1 * df_2**df_2) / ((df_1 * x + df_2)**(df_1 + df_2))) / (x * beta(df_1/2, df_2/2))

        return f

    def cdf(self, x, df_1, df_2):

        sub = (df_1 * x) / (df_1 * x + df_2)

        y = betainc(df_1/2, df_2/2, sub)

        return y


### F-distribution testing
FObj = F()

x_range = 5
x = np.linspace(0.0001, x_range, 10000)

y = np.zeros(x.shape)
y_cdf = np.zeros(x.shape)
y_cdf_emp = np.zeros(x.shape)

df_1 = 10
df_2 = 10

for i in range(x.shape[0]):
    y[i] = FObj.pdf(x[i], df_1, df_2)
    y_cdf[i] = FObj.cdf(x[i], df_1, df_2)
    if i == 0:
        y_cdf_emp[i] = y[i]
    else:
        y_cdf_emp[i] = y[i] * (x[i] - x[i-1]) + y_cdf_emp[i-1]


s = np.random.f(df_1, df_2, size=1000000)

plt.plot(x, y)
plt.hist(s, bins=100, density=True)
plt.plot(x, y_cdf, label='Theoretical')
plt.plot(x, y_cdf_emp, label='Empirical')
plt.legend()
plt.show()

### Student-t testing
# Student_tObj = Student_t()
#
# x_range = 100
# x = np.linspace(-x_range, x_range, 10000)
#
# y = np.zeros(x.shape)
# y_cdf = np.zeros(x.shape)
# y_cdf_emp = np.zeros(x.shape)
#
# v = 5
#
# for i in range(x.shape[0]):
#     y[i] = Student_tObj.pdf(x[i], v)
#     y_cdf[i] = Student_tObj.cdf(x[i], v)
#     if i == 0:
#         y_cdf_emp[i] = y[i]
#     else:
#         y_cdf_emp[i] = y[i] * (x[i] - x[i-1]) + y_cdf_emp[i-1]
#
#
# s = np.random.default_rng().standard_t(v, size=1000000)
#
# plt.plot(x, y)
# plt.hist(s, bins=100, density=True)
# plt.plot(x, y_cdf, label='Theoretical')
# plt.plot(x, y_cdf_emp, label='Empirical')
# plt.legend()
# plt.show()