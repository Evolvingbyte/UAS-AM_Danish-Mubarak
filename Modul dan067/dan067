def invers22(m):
    a, b = m[0]
    c, d = m[1]

    det = a * d - b * c
    if det == 0:
        return None
    return [[d / det, -b / det], 
            [-c / det, a / det]]


def invers33(m):
    a, b, c = m[0]
    d, e, f = m[1]
    g, h, i = m[2]

    det = (a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g))
    if det == 0:
        return None

    adj = [[(e*i-f*h), -(b*i-c*h), (b*f-c*e)],
           [-(d*i-f*g), (a*i-c*g), -(a*f-c*d)],
           [(d*h-e*g), -(a*h-b*g), (a*e-b*d)]]

    hasil = []
    for baris in adj:
        hasil.append([x/det for x in baris])
    return hasil


def tampilkan(m):
    for baris in m:
        print(baris)
