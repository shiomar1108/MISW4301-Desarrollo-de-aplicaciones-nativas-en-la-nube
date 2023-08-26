# Proyecto-202314  

Equipo Tupperware

## Tabla de contenido



## Estructura de las carpetas del Proyecto

.
├── .github
│   └── workflows
│       ├── ci_pipeline.yml
│       ├── evaluator_entrega1.yml
│       └── evaluator_entrega2.yml
├── _old
│   └── README.md
├── offers
│   ├── src
│   │   ├── blueprint
│   │   │   ├── __init__.py
│   │   │   └── resources.py
│   │   ├── commands
│   │   │   ├── __init__.py
│   │   │   ├── base_command.py
│   │   │   ├── create.py
│   │   │   ├── delete.py
│   │   │   ├── get.py
│   │   │   ├── list.py
│   │   │   └── reset.py
│   │   ├── errors
│   │   │   ├── __init__.py
│   │   │   └── errors.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── models.py
│   │   ├── utilities
│   │   │   ├── __init__.py
│   │   │   └── utilities.py
│   │   ├── validators
│   │   │   ├── __init__.py
│   │   │   └── validators.py
│   │   ├── __init__.py
│   │   └── main.py
│   ├── test
│   │   ├── blueprints
│   │   │   └── test_resources.py
│   │   ├── commands
│   │   │   ├── test_create.py
│   │   │   ├── test_delete.py
│   │   │   ├── test_get.py
│   │   │   └── test_list.py
│   │   ├── __init__.py
│   │   └── conftest.py
│   ├── .env.database
│   ├── .env.development
│   ├── .env.template
│   ├── .env.test
│   ├── Dockerfile
│   ├── Pipfile
│   └── Pipfile.lock
├── posts
│   ├── src
│   │   ├── blueprint
│   │   │   ├── __init__.py
│   │   │   ├── api.py
│   │   │   └── vistas.py
│   │   ├── commands
│   │   │   ├── __init__.py
│   │   │   ├── base_command.py
│   │   │   ├── create.py
│   │   │   ├── delete.py
│   │   │   ├── get.py
│   │   │   ├── query.py
│   │   │   └── reset.py
│   │   ├── errors
│   │   │   ├── __init__.py
│   │   │   └── errors.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   └── config.py
│   │   ├── validators
│   │   │   ├── __init__.py
│   │   │   └── validators.py
│   │   └── main.py
│   ├── test
│   │   ├── commands
│   │   │   ├── test_create.py
│   │   │   ├── test_delete.py
│   │   │   ├── test_get.py
│   │   │   └── test_query.py
│   │   ├── __init__.py
│   │   └── conftest.py
│   ├── .env.database
│   ├── .env.development
│   ├── .env.test
│   ├── Dockerfile
│   ├── Pipfile
│   └── Pipfile.lock
├── routes
│   ├── src
│   │   ├── blueprint
│   │   │   ├── __init__.py
│   │   │   └── resources.py
│   │   ├── commands
│   │   │   ├── __init__.py
│   │   │   ├── base_command.py
│   │   │   ├── create.py
│   │   │   ├── delete.py
│   │   │   ├── get.py
│   │   │   ├── query.py
│   │   │   ├── reset.py
│   │   │   └── update.py
│   │   ├── errors
│   │   │   ├── __init__.py
│   │   │   └── errors.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── models.py
│   │   ├── queries
│   │   │   ├── __init__.py
│   │   │   ├── base_query.py
│   │   │   └── detail.py
│   │   ├── utilities
│   │   │   ├── __init__.py
│   │   │   └── utilities.py
│   │   ├── validators
│   │   │   ├── __init__.py
│   │   │   └── validators.py
│   │   ├── __init__.py
│   │   └── main.py
│   ├── test
│   │   ├── blueprints
│   │   │   └── test_resources.py
│   │   ├── commands
│   │   │   ├── test_create.py
│   │   │   ├── test_delete.py
│   │   │   ├── test_get.py
│   │   │   └── test_query.py
│   │   ├── __init__.py
│   │   └── conftest.py
│   ├── .env.database
│   ├── .env.development
│   ├── .env.template
│   ├── .env.test
│   ├── Dockerfile
│   ├── Pipfile
│   └── Pipfile.lock
├── users
│   ├── src
│   │   ├── blueprint
│   │   │   ├── __init__.py
│   │   │   └── resources.py
│   │   ├── commands
│   │   │   ├── __init__.py
│   │   │   ├── authenticate.py
│   │   │   ├── base_command.py
│   │   │   ├── create.py
│   │   │   ├── reset.py
│   │   │   └── update.py
│   │   ├── errors
│   │   │   ├── __init__.py
│   │   │   └── errors.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── models.py
│   │   ├── queries
│   │   │   ├── __init__.py
│   │   │   ├── base_query.py
│   │   │   └── detail.py
│   │   ├── utilities
│   │   │   ├── __init__.py
│   │   │   └── utilities.py
│   │   ├── validators
│   │   │   ├── __init__.py
│   │   │   └── validators.py
│   │   ├── __init__.py
│   │   └── main.py
│   ├── test
│   │   ├── blueprints
│   │   │   └── test_resources.py
│   │   ├── commands
│   │   │   ├── test_authenticate.py
│   │   │   ├── test_create.py
│   │   │   └── test_update.py
│   │   ├── commands
│   │   │   └── test_detail.py
│   │   ├── __init__.py
│   │   └── conftest.py
│   ├── .env.database
│   ├── .env.development
│   ├── .env.test
│   ├── Dockerfile
│   ├── Pipfile
│   └── Pipfile.lock
├── .gitignore
├── LICENSE
├── README.md
├── config.yaml
└── docker-compose.yml


## Despliegue de Produccion


## Despliegue de Deesarrollo


## Despliegue de Pruebas Unitarias