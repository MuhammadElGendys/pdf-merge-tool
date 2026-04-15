# PDF Auto-Merger (No External Libraries)
 
This is a lightweight Windows console application written in C# that merges PDF files **without using any external libraries**.
 
Instead of manipulating PDF structure directly, it uses the built‑in **Microsoft Print to PDF** virtual printer to combine multiple PDFs into a single output file.
 
---
 
## Features
 
- Reads a folder path from the user
- Detects all PDF files named sequentially (`0.pdf`, `1.pdf`, `2.pdf`, ...)
- Sorts them numerically
- Sends them to the Windows print pipeline in order
- Produces a merged PDF in the same folder
 
No dependencies, no NuGet packages, no external PDF libraries.
 
---
 
## How It Works
 
Windows includes a virtual printer called **Microsoft Print to PDF**.
This app prints each PDF in order, creating a single combined output file.
 
Because this uses the OS print subsystem:
 
- A **Save As** dialog may appear unless the printer is configured to auto-save
- The merge is done by printing pages sequentially, not by editing PDF structure
 
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
 
1. Build the project in Visual Studio or `dotnet build`
2. Run the executable
3. Enter the folder path containing your numbered PDFs
4. The app will print them to the **Microsoft Print to PDF** printer
5. Save the merged output (default suggestion: `merged.pdf`)
 
---
 
## Limitations
 
- Requires **Microsoft Print to PDF** (installed by default on Windows 10/11)
- A save dialog may appear unless auto-save is configured
- Not suitable for server environments or background automation
- Does not support PDFs with non-numeric filenames
 
---
 
## Why No PDF Libraries?
 
You asked specifically for a solution **without installing libraries**.
C# does not include native PDF manipulation APIs, so this method is the closest you can get while staying dependency‑free.
 
If you ever want a cleaner, more reliable merge, consider using:
 
- PdfSharp
- iText7
- QuestPDF
 
I can generate versions using those as well.
 
---
 
## License
 
Free to use, modify, and adapt.
