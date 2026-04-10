## Solution-1

- Pehle string ke character alphanumeric hai kya check by traversing it
- Agar alphanumeric hai to usse lowercase mai convert karke string main add karo
  - newstr=[] toh append karo
  - newstr="" toh concatenate karke reassign to same str
- Phir str ko uske reverse(using slicing) check karo ki dono barabar hai kya
  - if barabar -> return true
  - else -> return False
