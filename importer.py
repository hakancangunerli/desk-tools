def importer():
    packages = ['quantstats', 'plotext', 'yfinance', 'importlib', "terminaltables", "google", "webbrowser"]
    import importlib
    import subprocess
    for package in packages:
        try:
            importlib.import_module(package)
        except ImportError:
            print(f"{package} not found, installing...")
            subprocess.call(['pip', 'install', package])