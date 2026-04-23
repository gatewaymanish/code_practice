import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Executed {func.__name__} in {end-start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Finished slow function")

slow_function()

# output
# Executed slow_function in 2.0023 seconds



def require_role(role_name):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get("role") != role_name:
                raise PermissionError(f"Unauthorized! {role_name} role required.")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def delete_user_account(user, account_id):
    print(f"Account {account_id} deleted by {user['name']}.")

# Test
current_user = {"name": "Manny", "role": "admin"}
delete_user_account(current_user, 123)  
# Output: Account 123 deleted by Manny.



# 1. Define the decorator
def simple_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# 2. Apply it using the @ symbol
@simple_decorator
def say_hello():
    print("Hello!")

# 3. Call the function
say_hello()