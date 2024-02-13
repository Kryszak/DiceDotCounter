![Build Status](https://github.com/Kryszak/DiceDotCounter/actions/workflows/test.yml/badge.svg)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/bd82336d23064d3899d8da5b3613769f)](https://app.codacy.com/gh/Kryszak/DiceDotCounter/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

# DiceDotCounter
Simple python script to detect number of dots on die shown to camera with OpenCV.

# Development
1. Activate virtual environment with
`source ./venv.sh`
2. Install required dependencies with
`pip install -r requirements.txt`
3. Run script with 
`python counter/main.py`
4. To run tests:
`python -m unittest discover -s tests -p "*_test.py" -v`
