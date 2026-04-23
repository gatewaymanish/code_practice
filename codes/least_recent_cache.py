from abc import ABC, abstractmethod
from collections import OrderedDict

# Step 1: Define the interface
class CacheInterface(ABC):
    @abstractmethod
    def get(self, key: str) -> str:
        """Retrieve an item from the cache."""
        pass

    @abstractmethod
    def put(self, key: str, value: str) -> None:
        """Insert or update an item in the cache."""
        pass

    @abstractmethod
    def show_cache(self) -> None:
        """Display current cache contents."""
        pass


# Step 2: Implement LRU Cache
class LRUCache(CacheInterface):
    def __init__(self, capacity: int = 3):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: str) -> str:
        if key not in self.cache:
            return f"{key} not found in cache"
        else:
            # Move accessed item to the end (most recently used)
            self.cache.move_to_end(key)
            return f"Accessed {key}: {self.cache[key]}"

    def put(self, key: str, value: str) -> None:
        if key in self.cache:
            # Update existing item and mark as most recently used
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            # Pop the least recently used item (first item)
            removed_key, removed_value = self.cache.popitem(last=False)
            print(f"Evicted {removed_key}: {removed_value}")

    def show_cache(self) -> None:
        print("Cache:", dict(self.cache))


# Step 3: Example usage
if __name__ == "__main__":
    lru = LRUCache(capacity=3)

    lru.put("item1", "AAA")
    lru.put("item2", "BBB")
    lru.put("item3", "CCC")
    lru.show_cache()

    print(lru.get("item1"))   # Access item1 → moves to end
    lru.put("item4", "DDD")   # Evicts least recently used (item2)
    lru.show_cache()

    print(lru.get("item2"))   # item2 was evicted
    print(lru.get("item3"))   # Access item3 → moves to end
    lru.put("item5", "EEE")   # Evicts least recently used (item1)
    lru.show_cache()




# 2nd way to implement LRU Cache using a dictionary and a doubly linked list

from abc import ABC, abstractmethod
import random
import string

# Step 1: Define the interface
class CacheInterface(ABC):
    @abstractmethod
    def access_item(self, key: str) -> str:
        """Access an item by key, replacing least accessed if not found."""
        pass

    @abstractmethod
    def show_cache(self) -> None:
        """Display current cache contents."""
        pass

    @abstractmethod
    def show_tracker(self) -> None:
        """Display current tracker counts."""
        pass


# Step 2: Implement LFU Cache
class LFUCache(CacheInterface):
    def __init__(self, capacity: int = 3):
        self.capacity = capacity
        self.cache = {}
        self.tracker = {}

        # Initialize with item1, item2, item3
        for i in range(1, capacity + 1):
            key = f"item{i}"
            value = self._generate_value()
            self.cache[key] = value
            self.tracker[key] = 0

    def _generate_value(self) -> str:
        """Helper to generate random string values."""
        return ''.join(random.choices(string.ascii_letters, k=5))

    def access_item(self, key: str) -> str:
        if key in self.cache:
            self.tracker[key] += 1
            return f"Accessed {key}: {self.cache[key]}"
        else:
            # Replace least accessed item
            least_accessed = min(self.tracker, key=self.tracker.get)
            del self.cache[least_accessed]
            del self.tracker[least_accessed]

            new_value = self._generate_value()
            self.cache[key] = new_value
            self.tracker[key] = 1
            return f"{key} not found. Replaced {least_accessed} with {key}: {new_value}"

    def show_cache(self) -> None:
        print("Cache:", self.cache)

    def show_tracker(self) -> None:
        print("Tracker:", self.tracker)


# Step 3: Example usage
if __name__ == "__main__":
    cache_system = LFUCache(capacity=3)

    cache_system.show_cache()
    cache_system.show_tracker()

    print(cache_system.access_item("item1"))   # Access existing
    print(cache_system.access_item("item4"))   # Replace least accessed
    print(cache_system.access_item("item2"))   # Access existing
    print(cache_system.access_item("item5"))   # Another replacement

    cache_system.show_cache()
    cache_system.show_tracker()