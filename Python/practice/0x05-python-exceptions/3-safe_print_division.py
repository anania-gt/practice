def safe_print_division(a, b):
    try:
        result = a/b
    except (ZeroDivisionError,TypeError):
        result = None
    finally:
        print(f"Inside result = {result}")
    
safe_print_division(10, 0)