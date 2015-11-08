# Makes a virtual environment with the appropriate packages
if [ ! -d "venv" ] ; then
    virtualenv venv
fi
source venv/bin/activate
pip install numpy scipy scikit-learn pandas
