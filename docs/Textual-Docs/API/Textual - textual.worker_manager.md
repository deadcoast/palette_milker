---
title: "Textual - textual.worker_manager"
source: "https://textual.textualize.io/api/worker_manager/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.worker\_manager

Contains `WorkerManager`, a class to manage [workers](https://textual.textualize.io/guide/workers) for an app.

You access this object via [App.workers](https://textual.textualize.io/api/app/#textual.app.App.workers " workers") or [Widget.workers](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.workers " workers").

## WorkerManager [¶](https://textual.textualize.io/api/worker_manager/#textual.worker_manager.WorkerManager "Permanent link")

```
WorkerManager()
```

An object to manager a number of workers.

You will not have to construct this class manually, as widgets, screens, and apps have a worker manager accessibly via a `workers` attribute.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `app` [¶](https://textual.textualize.io/api/worker_manager/#textual.worker_manager.WorkerManager\(app\) "Permanent link") | `[App](https://textual.textualize.io/api/app/#textual.app.App " App (textual.app.App)")` | An App instance. | *required* |

### add\_worker [¶](https://textual.textualize.io/api/worker_manager/#textual.worker_manager.WorkerManager.add_worker "Permanent link")

```
add_worker(, =True, =True)
```

Add a new worker.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `worker` [¶](https://textual.textualize.io/api/worker_manager/#textual.worker_manager.WorkerManager.add_worker\(worker\) "Permanent link") | `[Worker](https://textual.textualize.io/api/worker/#textual.worker.Worker " Worker (textual.worker.Worker)")` | A Worker instance. | *required* |
| #### `start` [¶](https://textual.textualize.io/api/worker_manager/#textual.worker_manager.WorkerManager.add_worker\(start\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Start the worker if True, otherwise the worker must be started manually. | `True` |
| #### `exclusive` [¶](https://textual.textualize.io/api/worker_manager/#textual.worker_manager.WorkerManager.add_worker\(exclusive\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Cancel all workers in the same group as `worker`. | `True` |

### cancel\_all [¶](https://textual.textualize.io/api/worker_manager/#textual.worker_manager.WorkerManager.cancel_all "Permanent link")

```
cancel_all()
```

Cancel all workers.

### cancel\_group [¶](https://textual.textualize.io/api/worker_manager/#textual.worker_manager.WorkerManager.cancel_group "Permanent link")

```
cancel_group(, )
```

Cancel a single group.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `node` [¶](https://textual.textualize.io/api/worker_manager/#textual.worker_manager.WorkerManager.cancel_group\(node\) "Permanent link") | `[DOMNode](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode " DOMNode (textual.dom.DOMNode)")` | Worker DOM node. | *required* |
| #### `group` [¶](https://textual.textualize.io/api/worker_manager/#textual.worker_manager.WorkerManager.cancel_group\(group\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | A group name. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[[Worker](https://textual.textualize.io/api/worker/#textual.worker.Worker " Worker (textual.worker.Worker)")]` | A list of workers that were cancelled. |

### cancel\_node [¶](https://textual.textualize.io/api/worker_manager/#textual.worker_manager.WorkerManager.cancel_node "Permanent link")

```
cancel_node()
```

Cancel all workers associated with a given node

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `node` [¶](https://textual.textualize.io/api/worker_manager/#textual.worker_manager.WorkerManager.cancel_node\(node\) "Permanent link") | `[DOMNode](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode " DOMNode (textual.dom.DOMNode)")` | A DOM node (widget, screen, or App). | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[[Worker](https://textual.textualize.io/api/worker/#textual.worker.Worker " Worker (textual.worker.Worker)")]` | List of cancelled workers. |

### start\_all [¶](https://textual.textualize.io/api/worker_manager/#textual.worker_manager.WorkerManager.start_all "Permanent link")

```
start_all()
```

Start all the workers.

### wait\_for\_complete [¶](https://textual.textualize.io/api/worker_manager/#textual.worker_manager.WorkerManager.wait_for_complete "Permanent link")

```
wait_for_complete(=None)
```

Wait for workers to complete.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `workers` [¶](https://textual.textualize.io/api/worker_manager/#textual.worker_manager.WorkerManager.wait_for_complete\(workers\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[Worker](https://textual.textualize.io/api/worker/#textual.worker.Worker " Worker (textual.worker.Worker)")] \| None` | An iterable of workers or None to wait for all workers in the manager. | `None` |