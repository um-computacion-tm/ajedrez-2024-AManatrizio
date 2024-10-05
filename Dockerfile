FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-AManatrizio.git

WORKDIR /ajedrez-2024-AManatrizio

RUN pip install -r requirements.txt

CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python main.py"]


# Instrucciones para construir y ejecutar la imagen:
# docker buildx build -t ajedrez-2024-amanatrizio .
# docker run -i ajedrez-2024-amanatrizio
