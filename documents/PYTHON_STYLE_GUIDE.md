# Python Style Guide — Train Simulation Project

This guide adapts [PEP 8](https://peps.python.org/pep-0008/), the official Python style guide, for our train simulation codebase. When this document is silent on something, defer to PEP 8 itself. When the two conflict, this document wins for our project (per PEP 8's own guidance that project-specific conventions take precedence).

The goal is the same one PEP 8 states: code is read far more often than it's written, so we optimize for readability and consistency across the simulation engine, physics models, scheduling logic, and UI/rendering layers.

---

## 1. Code Layout

### Indentation
- Use **4 spaces** per indentation level. Never tabs.
- For wrapped function calls (e.g. constructing a `TrainConsist` with many cars, or a long `Schedule.add_stop(...)` call), prefer hanging indent:

```python
# Good
train = Locomotive(
    unit_id="BNSF-4521",
    horsepower=4400,
    max_speed_mph=70,
    weight_tons=210,
)

# Good — aligned with opening delimiter
route = build_route(origin_station, destination_station,
                     via=["Junction A", "Junction B"])
```

### Line Length
- Max **79 characters** for code; **72** for docstrings/comments.
- If the team agrees, we may extend code lines to 99 characters for readability in signal-logic or physics formulas — but docstrings/comments still wrap at 72.
- Prefer wrapping inside parentheses/brackets/braces over backslash continuation. Backslashes are acceptable for chained `with` statements when needed (e.g. opening multiple simulation config files).

### Blank Lines
- **Two** blank lines around top-level classes and functions (`class Train:`, `class Track:`, `def simulate_tick():`).
- **One** blank line between methods inside a class (e.g. between `Train.accelerate()` and `Train.brake()`).
- Use blank lines sparingly inside functions to separate logical steps — e.g. separate "compute traction force" from "apply braking force" from "update position" within a physics tick function.

### Imports
- One import per line; group and separate with a blank line in this order:
  1. Standard library (`math`, `dataclasses`, `enum`)
  2. Third-party (`numpy`, `pygame`, `pydantic`)
  3. Local modules (`from train_sim.physics import friction`, `from train_sim.signals import BlockSignal`)
- Prefer absolute imports (`from train_sim.rolling_stock import Locomotive`) over deep relative imports, except within tightly-coupled subpackages (e.g. `signals/`).
- Avoid wildcard imports (`from train_sim.core import *`) — they hide where `Track`, `Switch`, or `Station` actually come from.

### Module-Level Dunders
- Place `__all__`, `__version__`, etc. after the module docstring, before imports (except `from __future__` imports).

---

## 2. String Quotes
- Pick single or double quotes and be consistent within a module (e.g. `'stopped'` vs `"stopped"` for train state strings). Use the other quote style to avoid escaping (`"train's brakes"` instead of `'train\'s brakes'`).
- Triple-quoted docstrings always use `"""`.

---

## 3. Whitespace

Avoid extraneous whitespace:

```python
# Good
speed_mph = clamp(current_speed, 0, max_speed)
signal_states = {block_id: signal.state for block_id, signal in blocks.items()}

# Bad
speed_mph = clamp( current_speed , 0, max_speed )
```

- No space before `(` in a call or `[` in an indexing/slice:
  `track.get_segment(index)`, not `track.get_segment (index)`.
- Always one space around `=`, `==`, `+=`, `and`, `or`, `not`, `in`, `is`:
  `if train.state is TrainState.BRAKING:`
- No spaces around `=` for keyword args or default values (unless annotated):

```python
def accelerate(self, delta_time, throttle=1.0):
    ...

def accelerate(self, delta_time: float, throttle: float = 1.0):
    ...
```

- Slices: treat `:` as a low-priority operator, equal spacing on both sides, omit spacing when a parameter is omitted:
  `upcoming_stops = schedule.stops[current_index:current_index + 3]`

---

## 4. Comments and Docstrings

- Comments are complete sentences, capitalized, explaining **why**, not restating **what**:

```python
# Bad — restates the obvious
speed += acceleration * dt  # add acceleration times dt to speed

# Good — explains intent
speed += acceleration * dt  # Euler integration step for velocity
```

- Write docstrings for every public class, function, and method — `Train`, `Track`, `Signal`, `Schedule`, `simulate_tick()`. Non-public helpers (`_apply_rolling_resistance`) don't need a full docstring but should have a short comment if the logic isn't obvious.

```python
def calculate_braking_distance(speed_mps: float, deceleration: float) -> float:
    """Return the distance in meters needed to stop from the given speed.

    Uses standard kinematic deceleration; does not account for grade,
    adhesion, or emergency brake application delay.
    """
    return speed_mps ** 2 / (2 * deceleration)
```

---

## 5. Naming Conventions

| Element | Convention | Example |
|---|---|---|
| Modules/packages | `lowercase`, short | `physics.py`, `signals/`, `rolling_stock.py` |
| Classes | `CapWords` | `Locomotive`, `TrackSegment`, `BlockSignal`, `ScheduleEntry` |
| Functions/methods | `lower_case_with_underscores` | `apply_brakes()`, `get_next_signal()`, `update_position()` |
| Variables | `lower_case_with_underscores` | `current_speed_mph`, `train_length_m` |
| Constants | `UPPER_CASE_WITH_UNDERSCORES` | `MAX_TRACK_GRADE`, `DEFAULT_SIGNAL_SPACING_M`, `EMERGENCY_DECEL_MPS2` |
| Non-public / internal | leading underscore | `_compute_curve_resistance()`, `_pending_signals` |
| Type variables | `CapWords`, short | `T`, `RollingStockT` |
| Exceptions | `CapWords` + `Error` suffix | `InvalidRouteError`, `SignalConflictError`, `CouplingError` |

Additional notes:
- Always name the first argument of instance methods `self` and of classmethods `cls`.
- Avoid `l`, `O`, `I` as single-character variable names — easy to confuse with `1`/`0` (relevant since track/signal IDs are alphanumeric and easy to typo already).
- Use `class_` rather than `clss` if you need a variable named after a reserved word (e.g. a rolling-stock `class_` field like "freight" vs "passenger").
- Prefer descriptive names over abbreviations in domain logic: `braking_distance_m` over `bd`, `signal_aspect` over `sa`. Physics/math-heavy code (e.g. `dt`, `v0`, `a`) may use short conventional names *locally within a function*, but public APIs should be descriptive.

---

## 6. Programming Recommendations

- **`None` checks:** always `is` / `is not`, never `==`.
  `if next_signal is None:` not `if next_signal == None:`
- **Booleans:** `if train.is_stopped:` not `if train.is_stopped == True:`
- **Exceptions:** catch specific exceptions (`except TrackNotFoundError:`), not bare `except:`. Derive custom exceptions from `Exception`, and suffix error types with `Error` (`SwitchMisalignedError`).
- **Lambdas:** use `def` for anything bound to a name.

```python
# Bad
compute_grade_penalty = lambda grade: grade * 0.05

# Good
def compute_grade_penalty(grade: float) -> float:
    return grade * 0.05
```

- **Type comparisons:** use `isinstance(rolling_stock, Locomotive)`, not `type(x) is Locomotive`.
- **Empty sequence checks:** `if not scheduled_stops:` rather than `if len(scheduled_stops) == 0:`.
- **Return consistency:** if a function like `find_next_station()` can return a `Station` or nothing, be explicit — always `return None` on the empty path, don't just fall off the end.
- **Resource management:** use `with` for anything with a lifecycle — opening a track-layout config file, a save-state file, or a network connection to a multiplayer dispatch server.

```python
with open("layouts/main_line.json") as layout_file:
    track_layout = json.load(layout_file)
```

---

## 7. Type Annotations

Since simulation code (physics, scheduling, signal logic) benefits heavily from clear types, we encourage PEP 484-style annotations on public functions and dataclasses:

```python
from dataclasses import dataclass

@dataclass
class TrackSegment:
    segment_id: str
    length_m: float
    max_speed_mph: int
    grade_percent: float = 0.0


def time_to_stop(speed_mps: float, deceleration_mps2: float) -> float:
    """Return seconds required to stop given constant deceleration."""
    return speed_mps / deceleration_mps2
```

- One space after `:` in an annotation, none before.
- Spaces around `=` when a default value accompanies an annotation:
  `def set_speed(self, target_mph: float = 0.0) -> None:`
- Always space around `->`.

---

## 8. Project-Specific Notes

These extend PEP 8 for our simulation codebase specifically:

- **Units in names.** Because the sim mixes imperial (mph, tons) and metric (m/s², meters) depending on subsystem, suffix ambiguous quantities with units: `speed_mph`, `speed_mps`, `distance_m`, `mass_kg`. Don't leave a bare `speed` or `distance` where the unit isn't obvious from context.
- **Simulation tick functions** (`update()`, `simulate_tick()`, `step()`) should take `dt` (delta time in seconds) as an explicit parameter rather than reading a global clock, to keep physics deterministic and testable.
- **State enums** for train/signal state should use `enum.Enum` with `CapWords` class names and `UPPER_CASE` members:

```python
from enum import Enum

class SignalAspect(Enum):
    STOP = "stop"
    APPROACH = "approach"
    CLEAR = "clear"
```

- **IDs** (train IDs, track segment IDs, station codes) are strings, not ints, even when numeric-looking, to avoid accidental arithmetic on identifiers.

---

## References
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
- [PEP 484 – Type Hints](https://peps.python.org/pep-0484/)
