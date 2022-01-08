
follow the instruction
step1
  # create new directry called basedir
  mkdir basedir
  # get into that path
  cd microwork
  # clone the code
  git clone https://github.com/samiabat/microworks/
  # get into this new directory
  cd microworks
  # create virtual environment
step2
  # create the venv called myenv
  python3 -m venv myenv
  # activate the venv
  source myenv/bin/activate
# install the requirements
step3
  pip install -r requirements.txt
# run the server
step4
  python manage.py runserver
  
