## Overview

This package provides functions for mapping IEEE 802.11 channels to
frequencies and back. See the Code API for more details.

## IEEE 802.11 channels table

  -- --------------------------------------------------- -- --------------- -- ------------- --
     <tablestyle="text-align: center;">**Band**         **Frequency**      **Channel**   
     <rowstyle="background-color: #FFFFE0;">2.4GHz      2412.0 MHz         1             
     <rowstyle="background-color: #FFFFE0;">2.4GHz      2417.0 MHz         2             
     <rowstyle="background-color: #FFFFE0;">2.4GHz      2422.0 MHz         3             
     <rowstyle="background-color: #FFFFE0;">2.4GHz      2427.0 MHz         4             
     <rowstyle="background-color: #FFFFE0;">2.4GHz      2432.0 MHz         5             
     <rowstyle="background-color: #FFFFE0;">2.4GHz      2437.0 MHz         6             
     <rowstyle="background-color: #FFFFE0;">2.4GHz      2442.0 MHz         7             
     <rowstyle="background-color: #FFFFE0;">2.4GHz      2447.0 MHz         8             
     <rowstyle="background-color: #FFFFE0;">2.4GHz      2452.0 MHz         9             
     <rowstyle="background-color: #FFFFE0;">2.4GHz      2457.0 MHz         10            
     <rowstyle="background-color: #FFFFE0;">2.4GHz      2462.0 MHz         11            
     <rowstyle="background-color: #FFFFE0;">2.4GHz      2467.0 MHz         12            
     <rowstyle="background-color: #FFFFE0;">2.4GHz      2472.0 MHz         13            
     <rowstyle="background-color: #FFFFE0;">2.4GHz      2484.0 MHz         14            
     <rowstyle="background-color: #E0E0FF;">3.6GHz      3657.5 MHz         131           
     <rowstyle="background-color: #E0E0FF;">3.6GHz      3660.0 MHz         132           
     <rowstyle="background-color: #E0E0FF;">3.6GHz      3662.5 MHz         132           
     <rowstyle="background-color: #E0E0FF;">3.6GHz      3665.0 MHz         133           
     <rowstyle="background-color: #E0E0FF;">3.6GHz      3667.5 MHz         133           
     <rowstyle="background-color: #E0E0FF;">3.6GHz      3670.0 MHz         134           
     <rowstyle="background-color: #E0E0FF;">3.6GHz      3672.5 MHz         134           
     <rowstyle="background-color: #E0E0FF;">3.6GHz      3677.5 MHz         135           
     <rowstyle="background-color: #E0E0FF;">3.6GHz      3680.0 MHz         136           
     <rowstyle="background-color: #E0E0FF;">3.6GHz      3682.5 MHz         136           
     <rowstyle="background-color: #E0E0FF;">3.6GHz      3685.0 MHz         137           
     <rowstyle="background-color: #E0E0FF;">3.6GHz      3687.5 MHz         137           
     <rowstyle="background-color: #E0E0FF;">3.6GHz      3689.5 MHz         138           
     <rowstyle="background-color: #E0E0FF;">3.6GHz      3690.0 MHz         138           
     <rowstyle="background-color: #FFE0E0;">5GHz        4915.0 MHz         183           
     <rowstyle="background-color: #FFE0E0;">5GHz        4920.0 MHz         184           
     <rowstyle="background-color: #FFE0E0;">5GHz        4925.0 MHz         185           
     <rowstyle="background-color: #FFE0E0;">5GHz        4935.0 MHz         187           
     <rowstyle="background-color: #FFE0E0;">5GHz        4940.0 MHz         188           
     <rowstyle="background-color: #FFE0E0;">5GHz        4945.0 MHz         189           
     <rowstyle="background-color: #FFE0E0;">5GHz        4960.0 MHz         192           
     <rowstyle="background-color: #FFE0E0;">5GHz        4980.0 MHz         196           
     <rowstyle="background-color: #FFE0E0;">5GHz        5035.0 MHz         7             
     <rowstyle="background-color: #FFE0E0;">5GHz        5040.0 MHz         8             
     <rowstyle="background-color: #FFE0E0;">5GHz        5045.0 MHz         9             
     <rowstyle="background-color: #FFE0E0;">5GHz        5055.0 MHz         11            
     <rowstyle="background-color: #FFE0E0;">5GHz        5060.0 MHz         12            
     <rowstyle="background-color: #FFE0E0;">5GHz        5080.0 MHz         16            
     <rowstyle="background-color: #FFE0E0;">5GHz        5170.0 MHz         34            
     <rowstyle="background-color: #FFE0E0;">5GHz        5180.0 MHz         36            
     <rowstyle="background-color: #FFE0E0;">5GHz        5190.0 MHz         38            
     <rowstyle="background-color: #FFE0E0;">5GHz        5200.0 MHz         40            
     <rowstyle="background-color: #FFE0E0;">5GHz        5210.0 MHz         42            
     <rowstyle="background-color: #FFE0E0;">5GHz        5220.0 MHz         44            
     <rowstyle="background-color: #FFE0E0;">5GHz        5230.0 MHz         46            
     <rowstyle="background-color: #FFE0E0;">5GHz        5240.0 MHz         48            
     <rowstyle="background-color: #FFE0E0;">5GHz        5260.0 MHz         52            
     <rowstyle="background-color: #FFE0E0;">5GHz        5280.0 MHz         56            
     <rowstyle="background-color: #FFE0E0;">5GHz        5300.0 MHz         60            
     <rowstyle="background-color: #FFE0E0;">5GHz        5320.0 MHz         64            
     <rowstyle="background-color: #FFE0E0;">5GHz        5500.0 MHz         100           
     <rowstyle="background-color: #FFE0E0;">5GHz        5520.0 MHz         104           
     <rowstyle="background-color: #FFE0E0;">5GHz        5540.0 MHz         108           
     <rowstyle="background-color: #FFE0E0;">5GHz        5560.0 MHz         112           
     <rowstyle="background-color: #FFE0E0;">5GHz        5580.0 MHz         116           
     <rowstyle="background-color: #FFE0E0;">5GHz        5600.0 MHz         120           
     <rowstyle="background-color: #FFE0E0;">5GHz        5620.0 MHz         124           
     <rowstyle="background-color: #FFE0E0;">5GHz        5640.0 MHz         128           
     <rowstyle="background-color: #FFE0E0;">5GHz        5660.0 MHz         132           
     <rowstyle="background-color: #FFE0E0;">5GHz        5680.0 MHz         136           
     <rowstyle="background-color: #FFE0E0;">5GHz        5700.0 MHz         140           
     <rowstyle="background-color: #FFE0E0;">5GHz        5745.0 MHz         149           
     <rowstyle="background-color: #FFE0E0;">5GHz        5765.0 MHz         153           
     <rowstyle="background-color: #FFE0E0;">5GHz        5785.0 MHz         157           
     <rowstyle="background-color: #FFE0E0;">5GHz        5805.0 MHz         161           
     <rowstyle="background-color: #FFE0E0;">5GHz        5825.0 MHz         165           
  -- --------------------------------------------------- -- --------------- -- ------------- --
