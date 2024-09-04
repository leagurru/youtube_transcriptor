Script en python 3.12 para obtener la transcripción en el lenguaje ES de un video en youtube
si se indica otro parámetro se intenta realizar la traducción al lenguaje indicado
Se invoca desde la línea de comandos (indicando el id del video y el lenguaje de la transcripción 'es' como parámetro)
opcionalmente se puede indicar un lenguaje para traducir la transcripción

Ejemplo:
python3 youtube_transcriptor.py OuuO3l37653o es en
python3 youtube_transcriptor.py OuuO3l37653o es 

Instalación:
virtualenv venv
pip install -r requirements.txt
