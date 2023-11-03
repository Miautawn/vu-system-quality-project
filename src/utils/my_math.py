def add(a, b):
    return a + b


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            next_term = fib[i - 1] + fib[i - 2]
            fib.append(next_term)
        return fib


def parse_config_file(config):
    if config is None:
        return None
    if "server" in config:
        server_config = config["server"]
        if "host" in server_config and "port" in server_config:
            host = server_config["host"]
            port = server_config["port"]
            if validate_host(host) and validate_port(port):
                if "database" in config:
                    db_config = config["database"]
                    if "name" in db_config and "username" in db_config:
                        db_name = db_config["name"]
                        username = db_config["username"]
                        if validate_db_name(db_name) and validate_username(username):
                            return True
    return False
