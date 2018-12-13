FROM python:3

WORKDIR /opt/mcurrency_bank_account

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "mcurrency_bank_account/app.py" ]

EXPOSE 5000