
cd /d %~dp0
call C:\dev\pyenv\Scripts\activate.bat

pip install pip-review
pip-review
pip-review --auto
pip-review --local --interactive

pip freeze > .\requirements.txt
pip download -d .\whl -r .\requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com