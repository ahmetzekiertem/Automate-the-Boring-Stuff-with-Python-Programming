import smtlib

conn = smtlib.SMTP('smtp.gmail.com', 587)
type(conn)


conn.ehlo()
