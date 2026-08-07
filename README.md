# PDF Auto-Merger

This is a lightweight python application written in py that merges PDF files **locally**.

Instead of manipulating PDF structure online, it uses python code on your local pc to combine multiple PDFs into a single output file.

---

## Features

- Reads a folder path from the user
- Detects all PDF files that should be named by user as the following sequential (`0.pdf`, `1.pdf`, `2.pdf`, ...)
- Sorts them numerically
- Produces a merged PDF in the same folder

---

## How It Works (development)

required dependencies
```bash
pip install -r requirements.txt
```

---

## File Naming Requirements

Your PDFs must be named like this:

0.pdf
1.pdf
2.pdf
3.pdf


The program sorts them numerically and merges them in that order.

---

## Usage

1. Download the executable file from this repo.
2. Run the executable.
3. Enter the folder path containing your numbered PDFs.
4. The app will process them to be one file
5. Save the merged output (default suggestion: `merged.pdf`)

---

## Limitations

- Requires the following libraries: 

---

## License

Free to use, modify, and adapt.