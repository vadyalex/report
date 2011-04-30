import subprocess

COMPILE_COMMAND = "/usr/texbin/pdflatex -interaction=nonstopmode report.tex"

process = subprocess.Popen(COMPILE_COMMAND, shell=True, stdout=subprocess.PIPE)
for line in process.stdout:
    print line
process.wait()

OPEN_COMMAND = "open report.pdf"

subprocess.Popen(OPEN_COMMAND, shell=True, stdout=subprocess.PIPE).wait()

  