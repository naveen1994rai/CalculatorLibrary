#Startup script for Calculator app.

#install python packages
package_check = "$(pip list | grep 'pytest pytest-cov flake8')"
pip_install = "$(pip install -r requirements.txt)"
linting_check = "$(flake8 --statistics)"
unit_test= "$(pytest -v --cov)"

echo "Checking for required python packages and installing  if not present"
echo

echo "$package_check"
if [ $? 
