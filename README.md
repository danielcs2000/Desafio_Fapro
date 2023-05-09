# Desafio Fapro


## Install requirements

``` bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run app


``` bash
make run
```

Go to http://127.0.0.1:8000

## Run tests

``` bash
make test
```


## App description:

- La API debe estar desarrollada en Python utilizando la librería "requests" u otra similar.
- Para la API puedes usar el Framework que mas te guste.
- No se puede utilizar Selenium debido al alto consumo de recursos que estas herramientas implican.
- La API debe permitir consultar el valor de la Unidad de Fomento para una fecha específica, la cual debe ser ingresada como parámetro en la solicitud.
- La fecha mínima que se puede consultar es el 01-01-2013, y no hay fecha máxima, ya que la tabla se actualiza constantemente.
- La API debe devolver el valor de la Unidad de Fomento correspondiente a la fecha consultada.
- La respuesta de la API debe estar en formato JSON.
