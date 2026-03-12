
# LeetCode 535. Encode and Decode TinyURL
# Python 3 solution that preserves one to one mapping across calls

class Codec:
    def __init__(self):
        self.prefix = "http://tinyurl.com/"
        self.long_to_key = {}          # maps long URL to short key
        self.key_to_long = {}          # maps short key to long URL
        self.counter = 1               # auto increment id for new URLs
        self.alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def _id_to_key(self, num: int) -> str:
        # Convert an integer id to a base62 key
        if num == 0:
            return "0"
        base = 62
        chars = []
        while num > 0:
            num, rem = divmod(num, base)
            chars.append(self.alphabet[rem])
        return "".join(reversed(chars))

    def encode(self, longUrl: str) -> str:
        # Return an existing short URL if already encoded
        if longUrl in self.long_to_key:
            return self.prefix + self.long_to_key[longUrl]
        # Create a new unique key and persist the mapping
        key = self._id_to_key(self.counter)
        self.counter += 1
        self.long_to_key[longUrl] = key
        self.key_to_long[key] = longUrl
        return self.prefix + key

    def decode(self, shortUrl: str) -> str:
        # Extract key from the short URL then look up original
        key = shortUrl.rsplit("/", 1)[-1]
        return self.key_to_long.get(key, "")
