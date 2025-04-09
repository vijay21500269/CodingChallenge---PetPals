import os

def load_db_properties():
    props = {}
    try:
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "db.properties")
        print("Loading DB properties from:", path)
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    props[key.strip()] = value.strip()
    except FileNotFoundError:
        print("db.properties file not found at path.")
    except Exception as e:
        print(f"Error loading database properties: {e}")
    return props
