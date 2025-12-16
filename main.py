from mean_var_std import calculation


result = calculation([1,4,7,8,5,2,3,6,9])

# Print the result
print("== Result ==\n")
for key in (["Mean", "Variance", "Standard Deviation", "Max", "Min", "Sum"]):
    print(key.capitalize()), "\n"
    print(f"Columns: {result[key][0]}")
    print(f"Rows:    {result[key][1]}")
    print(f"All:     {result[key][2]}\n")
