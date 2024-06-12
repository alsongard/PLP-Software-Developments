def foo():
    from package_folder import A
    print("Invoking foo() from mod1.py")
    print(f"[mod1.py] foo() / A = {A}")