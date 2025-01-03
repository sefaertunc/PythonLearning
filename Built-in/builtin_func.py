print("*abs()")
a = -5
print(f"abs(-5): {abs(a)}")
#################################
print("\n*all() & any()")
all_any_list = [1, None]
print(f"all_any_list: {all_any_list}")
if all(all_any_list):
    print("All: All elements are true")
elif any(all_any_list):
    print("Any: Some elements are true")
else:
    print("!All & ! Any: All elements are false")
#################################
print("\n*ascii()")
ascii_list = [1,None,'a']
print(f"ascii([1,None,'a']): {ascii(ascii_list)} <- str")
#################################
print("\n*bin()")
sample_bin = bin(10)
print(f"bin(10): {sample_bin}")
#################################
print("\n*bool()")
print(f"bool([]): {bool([])}")
print(f"bool(None): {bool(None)}")
#################################
print("\n*breakpoint() & pdb.set_trace()")
print("sample_pdb = 5")
print("pdb.set_trace()")
print("sample_pdb*2")
#################################
print("\n*callable()")
def callable_func(): pass
print(f"callable(callable_func): {callable(callable_func)}")
#################################
print("\n*chr()")
print(f"chr(97):{chr(97)}")
#################################
print("\n*@classmethod")
print("class Sample:\n"
      "  @classmethod\n"
      "  def count(cls):\n"
      "    return cls.count\n"
      "sample = Sample()\n"
      "sample.count()\n")
#################################
