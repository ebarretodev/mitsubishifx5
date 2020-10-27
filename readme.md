# mitsubishifx5  

FX5CPU read D Registers library

Library exclusive to read D registers from FX5 CPU.

This communication provide a easily way to read D registers from PLC.
using the methods presents here.



### PLC Settings

To use this library you need to set up the PLC FX5 to receive this data:

<img src="D:\GenesisDev\002_Programas\PLC Connect\image\Step1.png" style="zoom:50%;" />

1. In **Navigation tab > Parameter > FX5UCPU > Module Parameter > Ethernet Port**

2. Set the **IP**, **Subnet Mask** and **Default Gateway** if necessary, and change the **Comunication Data Code** to ASCII ( no difference for this library if select **X,Y HEX **or **X,Y OCT**)

3. Double click on **External Device Configuration** to open next Screen.

   

![](D:\GenesisDev\002_Programas\PLC Connect\image\Step2.png)

4. Add a new **SLMP Connection Module**
5. Confirm the use for **TCP Protocol**
6. And select the **PORT** number for PLC receive this data.



### Module methods

##### Connect and Disconnect

To connect to PLC you need to invoke the follwings methods:

```python
#import modules
from mitsubishifx5 import connectPLC, disconnectPLC

#define IP Address and Local Port from PLC
dest = ('192.168.3.250', 3000)

#Connect method
connectPLC(dest)

#Disconnect method
disconnectPLC(dest)
```



##### Read D registers from PLC

After connecting to PLC it's possible to read devices from it using this code:

```python
#Reading value from D100
a = read_D(100)
print(a)
```

##### Write D registers to PLC

After connecting to PLC it's possible to read devices from it using this code:

```python
#Writing value int(200) to D102
b = write_D(103, 200)
print(b) #returns the value was setted
```

