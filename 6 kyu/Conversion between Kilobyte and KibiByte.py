from decimal import Decimal, ROUND_HALF_UP

def round_half_up(n, decimals=3):
    d = Decimal(n).quantize(Decimal(f'1.{"0"*decimals}'), rounding=ROUND_HALF_UP)
    return d.normalize()

def memorysize_conversion(memorysize):
    # defining the given unit
    words = memorysize.split()
    unit = words[1]
    
    # following logic, depending on the given unit
    number = float(words[0])
    match unit:
        case "kB":
            final = round_half_up((number * 10**3) / 2**10)
            return str(final) + " KiB"

        case "MB":
            final = round_half_up((number * 10**6) / 2**20)
            return str(final) + " MiB"

        case "GB":
            final = round_half_up((number * 10**9) / 2**30)
            return str(final) + " GiB"

        case "TB":
            final = round_half_up((number * 10**12) / 2**40)
            return str(final) + " TiB"

        case "KiB":
            final = round_half_up((number * 2**10) / 10**3)
            return str(final) + " kB"

        case "MiB":
            final = round_half_up((number * 2**20) / 10**6)
            return str(final) + " MB"

        case "GiB":
            final = round_half_up((number * 2**30) / 10**9)
            return str(final) + " GB"

        case "TiB":
            final = round_half_up((number * 2**40) / 10**12)
            return str(final) + " TB"
    return "nothing"