
follow the instruction
  # create new directry called basedir
  mkdir basedir
  # get into that path
  cd microwork
  # clone the code
  git clone https://github.com/samiabat/microworks/
  # get into this new directory
  cd microworks
  # create the venv called myenv
  python3 -m venv myenv
  # activate the venv
  source myenv/bin/activate
# install the requirements
  pip install -r requirements.txt
# run the server
  python manage.py runserver
  
