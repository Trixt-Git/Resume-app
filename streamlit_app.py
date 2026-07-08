with open("app.py") as f:
    exec(compile(f.read(), "app.py", "exec"))
