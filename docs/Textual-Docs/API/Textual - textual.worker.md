---
title: "Textual - textual.worker"
source: "https://textual.textualize.io/api/worker/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.worker

This module contains the `Worker` class and related objects.

See the guide for how to use [workers](https://textual.textualize.io/guide/workers).

## WorkType [¶](https://textual.textualize.io/api/worker/#textual.worker.WorkType "Permanent link")

```
WorkType = Union[
    Callable[[], Coroutine[None, None, ResultType]],
    Callable[[], ResultType],
    Awaitable[ResultType],
]
```

Type used for [workers](https://textual.textualize.io/guide/workers/).

## active\_worker [¶](https://textual.textualize.io/api/worker/#textual.worker.active_worker "Permanent link")

```
active_worker = ContextVar('active_worker')
```

Currently active worker context var.

## DeadlockError [¶](https://textual.textualize.io/api/worker/#textual.worker.DeadlockError "Permanent link")

Bases:

The operation would result in a deadlock.

## NoActiveWorker [¶](https://textual.textualize.io/api/worker/#textual.worker.NoActiveWorker "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

There is no active worker.

## Worker [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker "Permanent link")

```
Worker(
    ,
    ,
    *,
    ="",
    ="default",
    ="",
    =True,
    =False
)
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[ResultType]`

A class to manage concurrent work (either a task or a thread).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `node` [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker\(node\) "Permanent link") | `[DOMNode](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode " DOMNode (textual.dom.DOMNode)")` | The widget, screen, or App that initiated the work. | *required* |
| ### `work` [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker\(work\) "Permanent link") |  | A callable, coroutine, or other awaitable object to run in the worker. | *required* |
| ### `name` [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Name of the worker (short string to help identify when debugging). | `''` |
| ### `group` [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker\(group\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The worker group. | `'default'` |
| ### `description` [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker\(description\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Description of the worker (longer string with more details). | `''` |
| ### `exit_on_error` [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker\(exit_on_error\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Exit the app if the worker raises an error. Set to `False` to suppress exceptions. | `True` |
| ### `thread` [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker\(thread\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Mark the worker as a thread worker. | `False` |

### cancelled\_event [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.cancelled_event "Permanent link")

```
cancelled_event = Event()
```

A threading event set when the worker is cancelled.

### completed\_steps [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.completed_steps "Permanent link")

```
completed_steps
```

The number of completed steps.

### error [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.error "Permanent link")

```
error
```

The exception raised by the worker, or `None` if there was no error.

### is\_cancelled [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.is_cancelled "Permanent link")

```
is_cancelled
```

Has the work been cancelled?

Note that cancelled work may still be running.

### is\_finished [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.is_finished "Permanent link")

```
is_finished
```

Has the task finished (cancelled, error, or success)?

### is\_running [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.is_running "Permanent link")

```
is_running
```

Is the task running?

### node [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.node "Permanent link")

```
node
```

The node where this worker was run from.

### progress [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.progress "Permanent link")

```
progress
```

Progress as a percentage.

If the total steps is None, then this will return 0. The percentage will be clamped between 0 and 100.

### result [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.result "Permanent link")

```
result
```

The result of the worker, or `None` if there is no result.

### state [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.state "Permanent link")

```
state
```

The current state of the worker.

### total\_steps [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.total_steps "Permanent link")

```
total_steps
```

The number of total steps, or None if indeterminate.

### StateChanged [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.StateChanged "Permanent link")

```
StateChanged(, )
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

The worker state changed.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `worker` [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.StateChanged\(worker\) "Permanent link") |  | The worker object. | *required* |
| #### `state` [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.StateChanged\(state\) "Permanent link") |  | New state. | *required* |

### advance [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.advance "Permanent link")

```
advance(=1)
```

Advance the number of completed steps.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `steps` [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.advance\(steps\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Number of steps to advance. | `1` |

### cancel [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.cancel "Permanent link")

```
cancel()
```

Cancel the task.

### run [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.run "Permanent link")

```
run()
```

Run the work.

Implement this method in a subclass, or pass a callable to the constructor.

Returns:

| Type | Description |
| --- | --- |
| `ResultType` | Return value of the work. |

### update [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.update "Permanent link")

```
update(=None, =-1)
```

Update the number of completed steps.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `completed_steps` [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.update\(completed_steps\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | The number of completed seps, or `None` to not change. | `None` |
| #### `total_steps` [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.update\(total_steps\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | The total number of steps, `None` for indeterminate, or -1 to leave unchanged. | `-1` |

### wait [¶](https://textual.textualize.io/api/worker/#textual.worker.Worker.wait "Permanent link")

```
wait()
```

Wait for the work to complete.

Raises:

| Type | Description |
| --- | --- |
|  | If the Worker raised an exception. |
|  | If the Worker was cancelled before it completed. |

Returns:

| Type | Description |
| --- | --- |
| `ResultType` | The return value of the work. |

## WorkerCancelled [¶](https://textual.textualize.io/api/worker/#textual.worker.WorkerCancelled "Permanent link")

Bases:

The worker was cancelled and did not complete.

## WorkerError [¶](https://textual.textualize.io/api/worker/#textual.worker.WorkerError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

A worker related error.

## WorkerFailed [¶](https://textual.textualize.io/api/worker/#textual.worker.WorkerFailed "Permanent link")

```
WorkerFailed(error)
```

Bases:

The worker raised an exception and did not complete.

## WorkerState [¶](https://textual.textualize.io/api/worker/#textual.worker.WorkerState "Permanent link")

Bases: `[Enum](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum")`

A description of the worker's current state.

### CANCELLED [¶](https://textual.textualize.io/api/worker/#textual.worker.WorkerState.CANCELLED "Permanent link")

```
CANCELLED = 3
```

Worker is not running, and was cancelled.

### ERROR [¶](https://textual.textualize.io/api/worker/#textual.worker.WorkerState.ERROR "Permanent link")

```
ERROR = 4
```

Worker is not running, and exited with an error.

### PENDING [¶](https://textual.textualize.io/api/worker/#textual.worker.WorkerState.PENDING "Permanent link")

```
PENDING = 1
```

Worker is initialized, but not running.

### RUNNING [¶](https://textual.textualize.io/api/worker/#textual.worker.WorkerState.RUNNING "Permanent link")

```
RUNNING = 2
```

Worker is running.

### SUCCESS [¶](https://textual.textualize.io/api/worker/#textual.worker.WorkerState.SUCCESS "Permanent link")

```
SUCCESS = 5
```

Worker is not running, and completed successfully.

## get\_current\_worker [¶](https://textual.textualize.io/api/worker/#textual.worker.get_current_worker "Permanent link")

```
get_current_worker()
```

Get the currently active worker.

Raises:

| Type | Description |
| --- | --- |
|  | If there is no active worker. |

Returns:

| Type | Description |
| --- | --- |
|  | A Worker instance. |