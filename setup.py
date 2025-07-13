
# ---

## 🔹 6. `setup.py`

# ```python
# setup.py

from setuptools import setup, find_packages

setup(
    name='cam2text',
    version='0.1.0',
    description='Convert CCTV/video footage into readable activity text logs',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    author='Sarvesh Upasani',
    author_email='upasanisarvesh45.com',
    url='https://github.com/sarveshprjs/cam2text',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
