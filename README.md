# Unclosed File Resource Leak in Python

This repository demonstrates a common but easily overlooked error in Python: forgetting to close files after opening them.  Leaving files open can lead to resource exhaustion and data corruption. The `bug.py` file showcases the error; `bugSolution.py` provides the corrected version.

**Problem:** The `function_with_unclosed_file` function opens a file but fails to close it. This can lead to issues such as:

* **Resource exhaustion:**  Multiple unclosed files can consume system resources.
* **Data corruption:**  Changes made to the file may not be flushed to disk.
* **Program instability:**  The program might crash or become unresponsive.

**Solution:**  Always use a `with` statement to ensure that files are automatically closed even if errors occur.  This makes the code cleaner and more robust.