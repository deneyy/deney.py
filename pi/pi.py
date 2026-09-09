import mpmath

OUTPUT_FILE = "pi.txt"
CHUNK = 1000  # how many extra digits to compute per iteration

def main():
    written = "3"
    with open(OUTPUT_FILE, "w") as f:
        f.write("3.")
        f.flush()

    digits_after_decimal = 0

    while True:
        digits_after_decimal += CHUNK
        mpmath.mp.dps = digits_after_decimal + 10  # a little extra precision headroom

        pi_str = mpmath.nstr(mpmath.pi, digits_after_decimal + 5, strip_zeros=False)
        pi_str = pi_str.replace("3.", "", 1)

        new_digits = pi_str[:digits_after_decimal][len(written) - 1:]

        with open(OUTPUT_FILE, "a") as f:
            f.write(new_digits)
            f.flush()

        written += new_digits

if __name__ == "__main__":
    main()