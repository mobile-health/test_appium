cd $PYENV_VIRTUAL_ENV
path=$(find . -type d -name "robotframework_appiumlibrary*")
broken='selenium<4,>=2.47.1'
fixed='selenium>=2.47.1'
sed -i "s/$broken/$fixed/g" $path/requires.txt