# V1.0
## Backlight switching Mosfet
P Channel Mosfet chosen in stead of N Channel
Workaround: Replaced with a NPN Transistor

## I2C

- Device Adress Pins A0-A2 are floating, should be either high or low
- SDA and SCL must be pulled HIGH not low
- PINOut for I2C Expander Chip entirely wrong :/ Datasheet was read incorrectly