import os

badhash = "c1a4be04b972b6c17db242fc37752ad517c29402"
goodhash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

cmd = f"git bisect start {badhash} {goodhash} && git bisect run python myscript.py"

status = os.system(cmd)

if status != 0:
    print("Bisecting failed.")
    os.system("git bisect reset")
    exit(1)
else:
    print("Bisecting completed successfully.")
    os.system("git bisect reset")
    exit(0)
    
