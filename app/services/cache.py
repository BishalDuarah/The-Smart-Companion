# app/services/cache.py

cache = {}

def get_cached(task):
    return cache.get(task)

def set_cache(task, steps):
    cache[task] = steps
