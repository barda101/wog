FROM python:3-alpine
COPY GuessGame.py /GuessGame.py
COPY e2e.py /e2e.py
COPY MemoryGame.py /MemoryGame.py
COPY Scores.txt /Scores.txt
COPY main.py /main.py
COPY MainScores.py /MainScores.py
COPY Score.py /Score.py
COPY Live.py /Live.py
COPY CurrencyRouletteGame.py /CurrencyRouletteGame.py
COPY MainGame.py /MainGame.py
COPY Utils.py /Utils.py
CMD ["python", "/MainGame.py"]