import pkg_resources

packages = [
    "certifi",
    "click",
    "colorama",
    "Flask",
    "importlib-metadata",
    "itsdangerous",
    "Jinja2",
    "joblib",
    "MarkupSafe",
    "numpy",
    "scikit-learn",
    "scipy",
    "threadpoolctl",
    "typing-extensions",
    "Werkzeug",
    "wincertstore",
    "zipp",
    "gunicorn"
]

for package in packages:
    try:
        version = pkg_resources.get_distribution(package).version
        print(f"{package}=={version}")
    except pkg_resources.DistributionNotFound:
        print(f"{package} is not installed")
