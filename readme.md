# mitsubishifx5  

FX5CPU read/write D&M  Registers library

This library provide a easily way to read/write D&M registers from PLC models iQ-F or iQ-R.


### PLC Settings

To use this library you need to set up the PLC FX5 to receive this data:

<img src="https://github.com/ebarretodev/mitsubishifx5/blob/master/image/Step1.png" style="zoom:50%;" />

1. In **Navigation tab > Parameter > FX5UCPU > Module Parameter > Ethernet Port**

2. Set the **IP**, **Subnet Mask** and **Default Gateway** if necessary, and change the **Comunication Data Code** to ASCII ( no difference for this library if select **X,Y HEX **or **X,Y OCT**)

3. Double click on **External Device Configuration** to open next Screen.

   

![](https://github.com/ebarretodev/mitsubishifx5/blob/master/image/Step2.png)

4. Add a new **SLMP Connection Module**
5. Confirm the use for **TCP Protocol**
6. And select the **PORT** number for PLC receive this data.



### class

```python
#import modules
from mitsubishifx5 import PLC

#Create a object PLC to control, set 'FX5CPU' or 'RCPU'
fx5 = PLC('FX5CPU', '192.168.3.250', '3000')
```



##### Connect and Disconnect

To connect to PLC you need to invoke the follwings methods:

```python
#Connect method
fx5.connectPLC(dest)

#Disconnect method
fx5.disconnectPLC(dest)
```



##### Read D and M registers from PLC

After connecting to PLC it's possible to read devices from it using this code, the methods response the value was reading if successful, or error code from communication:

```python
#Reading value from D100
a = fx5.read_D(100)
print(a)
#Reading value from M100, response as 0 if False or 1 if True
b = fx5.read_M(100)
print(b)
```

##### Write D and M registers to PLC

After connecting to PLC it's possible to read devices from it using this code, the methods response the same value was setting if successful, or error code from communication:

```python
#Writing value int(200) to D102
c = write_D(103, 200)
print(b) #returns the value was setted
#Writing value int(1) to M100 -> 1 = True/0 = False
d = fx5.write_M(100, 1)
print(d)
```

