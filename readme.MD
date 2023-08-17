py -m venv venv

venv/Scripts/activate.bat

pip install -r requirements.txt

python ask_bard.py --cookie "my_cookie_value" --question "What's the capital of France?"
