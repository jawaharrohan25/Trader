
import pyotp

secret = "QTWO233MANXJF3J6ZTWIVYZHZEYILR6N"

totp = pyotp.TOTP(secret)

print(totp.now())