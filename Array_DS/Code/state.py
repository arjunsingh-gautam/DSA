# In this we learn about state variable in linear scan
# state: It reflects the state of all visited values till now like running,current_index,max_value etc.

arr=[1,34,32,193]
running_sum=0 # state_variable
for i in range(len(arr)):
    running_sum+=arr[i]
    print(f"Current Index:{i}\tRunning Sum:{running_sum}")