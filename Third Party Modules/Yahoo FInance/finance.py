# from setuptools import find_namespace_packages
import yfinance
import pandas

rk = yfinance.download("RKFORGE.NS")
print(rk)