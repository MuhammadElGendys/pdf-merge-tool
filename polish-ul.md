# PDF Merger — Polish Checklist

Status: **Core functionality complete (~90% of original scope).** This list is for
after-beta refinement, roughly ordered by priority.

## Before calling it "beta" (blocker)

- [ ] Replace bare `except:` with `except Exception as e:` and print `e` so
      failures are actually debuggable instead of silently generic.

## High-value robustness (do soon after beta)

- [ ] **Empty folder / no PDFs found**: if `pdf_list` ends up empty after the
      `os.listdir()` filter, warn the user and exit instead of proceeding into
      `MergingPDFs()` with nothing to merge.
- [ ] **Corrupted / non-PDF file with `.pdf` extension**: `merge.append()` will
      throw — decide whether to skip-and-warn per file, or fail the whole run.
- [ ] **Permission errors on write**: e.g. `merged.pdf` already open in another
      program, or folder is read-only. Catch and give a clear message.
- [ ] **Overwrite protection**: if `merged.pdf` already exists in the folder,
      decide: overwrite silently, ask for confirmation, or auto-rename
      (`merged (1).pdf`)?

## Input validation gaps

- [ ] `extract_number()` assumes exactly one number per filename — confirm this
      is acceptable, or tighten the regex if filenames could have version
      numbers, dates, etc. that aren't the merge index.
- [ ] Decide fate of asking the user for an expected PDF count — either drop the
      question permanently, or bring it back purely as a sanity check
      (`if user_input_files_number != len(pdf_list): warn`).
- [ ] What happens if two files extract to the *same* number (e.g. `"2.pdf"` and
      `"02.pdf"`)? Currently undefined behavior — sort is stable but silently
      picks one order.

## Code quality / structure

- [ ] Rename `LongSeparetor`, `MidSeparetor`, `ShortSeparetor` →
      `long_separator`, etc. (typo fix + PEP8 snake_case convention).
- [ ] Reconsider `global` usage in `GetUserInput()` — could return a tuple
      `(path, pdf_list)` instead, avoiding implicit shared state.
- [ ] Add a `main()` function wrapping the `try/except` call sequence, instead
      of bare top-level script calls — standard Python convention, makes the
      script importable/testable later.

## Nice-to-haves (optional, only if I want to keep growing this)

- [ ] Progress feedback while merging (e.g. `print(f"Adding {pdf}...")` per file).
- [ ] Let user specify a custom output filename instead of hardcoded `merged.pdf`.
- [ ] `argparse` support so it can run non-interactively (e.g.
      `python merge.py --folder "C:\path"`), useful if I ever want to
      automate/schedule it.
- [ ] Package as a standalone `.exe` via `pyinstaller` if I want to hand this
      to a non-technical user without them installing Python.

---
*Search terms for each item are in the conversation history where each topic
was first discussed — revisit those messages when tackling a specific item.*