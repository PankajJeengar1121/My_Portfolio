# root/build.sh
echo "--- Starting Build Process ---"

# Use the --break-system-packages flag to bypass the PEP 668 error
python3.12 -m pip install --upgrade pip
python3.12 -m pip install -r requirements.txt --break-system-packages

echo "--- Collecting Static Files ---"
# Ensure the staticfiles directory is created
python3.12 manage.py collectstatic --noinput --clear

echo "--- Build Finished Successfully ---"
