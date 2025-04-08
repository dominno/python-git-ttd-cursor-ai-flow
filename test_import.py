import passgen

print("Successfully imported passgen")
print(f"Version: {passgen.__version__}")

password = passgen.generate()
print(f"Generated password: {password}") 