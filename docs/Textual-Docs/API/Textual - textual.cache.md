---
title: "Textual - textual.cache"
source: "https://textual.textualize.io/api/cache/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.cache

Cache classes are dict-like containers used to avoid recalculating expensive operations such as rendering.

You can also use them in your own apps for similar reasons.

## FIFOCache [¶](https://textual.textualize.io/api/cache/#textual.cache.FIFOCache "Permanent link")

```
FIFOCache()
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[CacheKey, CacheValue]`

A simple cache that discards the first added key when full (First In First Out).

This has a lower overhead than LRUCache, but won't manage a working set as efficiently. It is most suitable for a cache with a relatively low maximum size that is not expected to do many lookups.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `maxsize` [¶](https://textual.textualize.io/api/cache/#textual.cache.FIFOCache\(maxsize\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Maximum size of cache before discarding items. | *required* |

### clear [¶](https://textual.textualize.io/api/cache/#textual.cache.FIFOCache.clear "Permanent link")

```
clear()
```

Clear the cache.

### get [¶](https://textual.textualize.io/api/cache/#textual.cache.FIFOCache.get "Permanent link")

```
get(: CacheKey) -> CacheValue | None
```
```
get(
    : CacheKey, : DefaultValue
) -> CacheValue | DefaultValue
```

```
get(, =None)
```

Get a value from the cache, or return a default if the key is not present.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `key` [¶](https://textual.textualize.io/api/cache/#textual.cache.FIFOCache.get\(key\) "Permanent link") | `CacheKey` | Key | *required* |
| #### `default` [¶](https://textual.textualize.io/api/cache/#textual.cache.FIFOCache.get\(default\) "Permanent link") | `DefaultValue \| None` | Default to return if key is not present. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `CacheValue \| DefaultValue \| None` | Either the value or a default. |

### keys [¶](https://textual.textualize.io/api/cache/#textual.cache.FIFOCache.keys "Permanent link")

```
keys()
```

Get cache keys.

### set [¶](https://textual.textualize.io/api/cache/#textual.cache.FIFOCache.set "Permanent link")

```
set(, )
```

Set a value.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `key` [¶](https://textual.textualize.io/api/cache/#textual.cache.FIFOCache.set\(key\) "Permanent link") | `CacheKey` | Key. | *required* |
| #### `value` [¶](https://textual.textualize.io/api/cache/#textual.cache.FIFOCache.set\(value\) "Permanent link") | `CacheValue` | Value. | *required* |

## LRUCache [¶](https://textual.textualize.io/api/cache/#textual.cache.LRUCache "Permanent link")

```
LRUCache()
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[CacheKey, CacheValue]`

A dictionary-like container with a maximum size.

If an additional item is added when the LRUCache is full, the least recently used key is discarded to make room for the new item.

The implementation is similar to functools.lru\_cache, which uses a (doubly) linked list to keep track of the most recently used items.

Each entry is stored as \[PREV, NEXT, KEY, VALUE\] where PREV is a reference to the previous entry, and NEXT is a reference to the next value.

Note that stdlib's @lru\_cache is implemented in C and faster! It's best to use @lru\_cache where you are caching things that are fairly quick and called many times. Use LRUCache where you want increased flexibility and you are caching slow operations where the overhead of the cache is a small fraction of the total processing time.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `maxsize` [¶](https://textual.textualize.io/api/cache/#textual.cache.LRUCache\(maxsize\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Maximum size of the cache, before old items are discarded. | *required* |

### maxsize [¶](https://textual.textualize.io/api/cache/#textual.cache.LRUCache.maxsize "Permanent link")

```
maxsize
```

### clear [¶](https://textual.textualize.io/api/cache/#textual.cache.LRUCache.clear "Permanent link")

```
clear()
```

Clear the cache.

### discard [¶](https://textual.textualize.io/api/cache/#textual.cache.LRUCache.discard "Permanent link")

```
discard()
```

Discard item in cache from key.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `key` [¶](https://textual.textualize.io/api/cache/#textual.cache.LRUCache.discard\(key\) "Permanent link") | `CacheKey` | Cache key. | *required* |

### get [¶](https://textual.textualize.io/api/cache/#textual.cache.LRUCache.get "Permanent link")

```
get(: CacheKey) -> CacheValue | None
```
```
get(
    : CacheKey, : DefaultValue
) -> CacheValue | DefaultValue
```

```
get(, =None)
```

Get a value from the cache, or return a default if the key is not present.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `key` [¶](https://textual.textualize.io/api/cache/#textual.cache.LRUCache.get\(key\) "Permanent link") | `CacheKey` | Key | *required* |
| #### `default` [¶](https://textual.textualize.io/api/cache/#textual.cache.LRUCache.get\(default\) "Permanent link") | `DefaultValue \| None` | Default to return if key is not present. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `CacheValue \| DefaultValue \| None` | Either the value or a default. |

### grow [¶](https://textual.textualize.io/api/cache/#textual.cache.LRUCache.grow "Permanent link")

```
grow()
```

Grow the maximum size to at least `maxsize` elements.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `maxsize` [¶](https://textual.textualize.io/api/cache/#textual.cache.LRUCache.grow\(maxsize\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | New maximum size. | *required* |

### keys [¶](https://textual.textualize.io/api/cache/#textual.cache.LRUCache.keys "Permanent link")

```
keys()
```

Get cache keys.

### set [¶](https://textual.textualize.io/api/cache/#textual.cache.LRUCache.set "Permanent link")

```
set(, )
```

Set a value.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `key` [¶](https://textual.textualize.io/api/cache/#textual.cache.LRUCache.set\(key\) "Permanent link") | `CacheKey` | Key. | *required* |
| #### `value` [¶](https://textual.textualize.io/api/cache/#textual.cache.LRUCache.set\(value\) "Permanent link") | `CacheValue` | Value. | *required* |