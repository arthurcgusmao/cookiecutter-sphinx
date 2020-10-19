# Cookiecutter Sphinx

A generic Cookiecutter template for Sphinx documentation.


## Usage

Make sure you have [cookiecutter](https://github.com/cookiecutter/cookiecutter) installed:

```console
pip install cookiecutter
```

Download and create project structure:

```console
cookiecutter https://github.com/arthurcgusmao/cookiecutter-sphinx
```

After running the command above, cookiecutter will prompt you for:

1. `project_name`: Name of the project, to be inserted in the `info.yaml` file;
2. `author_name`: Name of author or organization, to be inserted in the `info.yaml` file;
3. `docs_dir`: Relative path of the directory where documentation will be created;
4. `module_dir`: Relative path of the module where your source code should be;
5. `info_file`: Relative path of a metadata file of the project;
6. `year`: Current year, to be inserted in the `info.yaml` file;
7. `version`: Initial version of the project, to be inserted in the `info.yaml` file.

The created files will have the structure below:

```text
.
├── docs
│   ├── _static
│   ├── _templates
│   ├── conf.py
│   ├── .gitignore
│   ├── index.rst
│   └── Makefile
└── info.yaml
```


## License

Cookiecutter Sphinx is licensed under the [Apache License, Version 2.0](./LICENSE).
